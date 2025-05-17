from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
corpus = []
metadata = []

def add_document_chunks(chunks, doc_id):
    global corpus
    embeddings = model.encode(chunks)
    index.add(np.array(embeddings))
    corpus.extend(chunks)
    metadata.extend([doc_id] * len(chunks))

def search(query, k=5):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), k)
    results = [{"text": corpus[i], "doc_id": metadata[i]} for i in indices[0]]
    return results
