from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredHTMLLoader, UnstructuredMarkdownLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
import os

db = None

def get_db() -> FAISS:
    global db
    return db

def set_db(_db : FAISS):
    global db
    db = _db

def embed_document(folder : str) -> FAISS:
    documents = []
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    for f in os.listdir(folder):
        abs_file = os.path.join(folder, f)
        if f.lower().endswith(".pdf"):
            raw_documents = PyPDFLoader(abs_file).load()
        elif f.lower().endswith(".html"):
            raw_documents = UnstructuredHTMLLoader(abs_file).load()
        elif f.lower().endswith(".md"):
            raw_documents = UnstructuredMarkdownLoader(abs_file).load()        
        else:
            raw_documents = TextLoader(abs_file).load()
        documents.extend(text_splitter.split_documents(raw_documents))
    db = FAISS.from_documents(documents, OpenAIEmbeddings())
    return db

def save_db(db : FAISS, folder : str, path : str):
    db.save_local(folder, path)

def load_db(folder : str, path : str):
    db = FAISS.load_local(folder, OpenAIEmbeddings(), path)
    return db

def query(db : FAISS, question : str) -> str:
    if not db:
        return "Retriever service is not available."
    docs = db.similarity_search(question)
    return docs[0].page_content