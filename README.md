# Project Title: RAG (Retrieval-Augmented Generation) Framework 📊

## Overview
The RAG framework is a Python-based project designed to facilitate Retrieval-Augmented Generation workflows, combining document retrieval and language generation. It includes functionality for handling documents, generating responses, and providing a web interface for user interaction. 🌐

## Features
- 🔎 Document retrieval and indexing.
- 🔄 Generation of responses using prompts.
- 🌐 Web interface for interaction.
- 🎨 Modular code structure for extensibility.

## File Structure
```
rag-main/
├── .gitignore               # Specifies files to ignore in version control
├── README.md                # Project documentation
├── app.py                   # Main application script for running the web app
├── requirements.txt         # Python dependencies for the project
├── setup.py                 # Setup script for packaging and installation
├── store_index.py           # Script for managing document indices
│
├── data/
│   └── Medical_book.pdf     # Sample document for retrieval
│
├── exp/
│   └── trials (1).ipynb     # Experimental Jupyter notebook
│
├── src/
│   ├── helper.py            # Helper functions for the project
│   └── prompt.py            # Prompt handling logic
│
├── static/
│   └── style.css            # CSS for styling the web interface
│
└── templates/
    └── chat.html            # HTML template for the chat interface
```

## Getting Started 🏃‍♂️

### Prerequisites
- 🔢 Python 3.8 or higher
- 🔢 pip (Python package manager)

### Installation 🔧
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd rag-main
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the project (optional):
   ```bash
   python setup.py install
   ```

### Usage 🌐
Run the application using:
```bash
python app.py
```
Access the web interface at `http://127.0.0.1:5000`.

### Experimental Notebooks 🔄
Open the Jupyter notebook in the `exp` directory for exploratory trials:
```bash
jupyter notebook exp/trials\ \(1\).ipynb
```

## Project Structure 🔀

### Key Components
1. **Application Logic**
   - `app.py`: Main entry point for the web application.
   - `store_index.py`: Handles document storage and indexing.

2. **Source Code**
   - `src/helper.py`: Contains helper functions for modularity.
   - `src/prompt.py`: Manages prompt-related operations.

3. **Web Interface**
   - `templates/chat.html`: HTML template for the chat interface.
   - `static/style.css`: CSS for styling the web interface.

4. **Data**
   - `data/Medical_book.pdf`: Example PDF document for testing retrieval functionality.

5. **Experimental Work**
   - `exp/trials (1).ipynb`: Jupyter notebook for experimental analysis and trials.

## Contribution 🔧
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git commit -m "Description of feature"
   git push origin feature-name
   ```
4. Submit a pull request.

## License 🔒
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments 🌟
Special thanks to all contributors and open-source projects that inspired this framework.

