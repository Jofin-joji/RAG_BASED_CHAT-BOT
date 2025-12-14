# etl/load.py

from etl.extract import load_text_files
from etl.transform import chunk_text

def prepare_documents(data_path):
    raw_docs = load_text_files(data_path)
    all_chunks = []

    for doc in raw_docs:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)

    return all_chunks
