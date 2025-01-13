from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from src.prompt import *
import os

app = Flask(__name__)

with open(r'C:\Users\afz31\RAG\api_key.txt', "r") as file:
    PINECONE_API_KEY = file.read()

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

embeddings = download_hugging_face_embeddings()


index_name="medical-chatbot"

#Loading the index
docsearch=Pinecone.from_existing_index(index_name, embeddings)


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model='TheBloke/Llama-2-7B-Chat-GGML',
                  config={'max_new_tokens':1024,
                          'temperature':0.8})


qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)

