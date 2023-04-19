import pickle
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownTextSplitter
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.vectorstores import FAISS
import streamlit as st

loader = UnstructuredMarkdownLoader('schema.md')
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
texts = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings(openai_api_key = st.secrets["OPENAI_API_KEY"])
docsearch = FAISS.from_documents(texts, embeddings)

docsearch.save_local("faiss_index")

# with open("vectors.pkl", "wb") as f:
#     pickle.dump(docsearch, f)