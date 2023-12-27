from core.tools.rag import retriever

import os
os.environ["HTTP_PROXY"] = "http://localhost:7890"
os.environ["HTTPS_PROXY"] = "http://localhost:7890"
os.environ["OPENAI_PROXY"] = "http://localhost:7890"

if __name__ == "__main__":
    db = retriever.embed_document("./documents")
    retriever.save_db(db, "./faiss", "db")