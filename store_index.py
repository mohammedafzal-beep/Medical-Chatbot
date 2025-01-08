from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import PineconeVectorStore
from pinecone import Pinecone

with open(r'C:\Users\afz31\rag_chatbot\api_key.txt', "r") as file:
    PINECONE_API_KEY = file.read()


extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


#Initializing the Pinecone
pc=Pinecone(api_key=PINECONE_API_KEY)

index_name="medical-chatbot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch=PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)