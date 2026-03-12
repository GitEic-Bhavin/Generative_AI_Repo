# try:
#     # new / installed package provides langchain_classic
#     from langchain_classic.memory import ConversationBufferMemory
# except Exception:
#     # fallback for older langchain versions
#     from langchain.memory import ConversationBufferMemory

import streamlit as st
import pdfplumber
import io

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# OLLAMA (NO API KEY REQUIRED)
from langchain_ollama import ChatOllama, OllamaEmbeddings

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


st.header("My First ChatBot (Local Ollama RAG)")

# ==============================
# SIDEBAR
# ==============================

with st.sidebar:
    st.title("Your Documents")
    files = st.file_uploader(
        "Upload PDF Files",
        type="pdf",
        accept_multiple_files=True
    )
    process_button = st.button("Process & Embed")


# ==============================
# EXTRACT PDF TEXT
# ==============================

def extract_pdf_text(pdf_files):
    text = ""

    for pdf in pdf_files:
        pdf.seek(0)
        pdf_bytes = io.BytesIO(pdf.read())

        with pdfplumber.open(pdf_bytes) as opened_pdf:
            for page in opened_pdf.pages:
                text += page.extract_text() or ""

    return text


# ==============================
# CREATE VECTOR DB and Chuncks
# ==============================

def create_vector_store(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=20
    )

    chunks = splitter.split_text(text)

    st.subheader("Generated Chunks")
    st.write(f"Total chunks created: {len(chunks)}")

    # LOCAL EMBEDDINGS - Converts Chuncks into numbers and save it locally in vector db FAISS
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_db = FAISS.from_texts(chunks, embedding=embeddings)

    st.subheader("Vector DB Info")
    st.write("Total vectors stored:", vector_db.index.ntotal)

    return vector_db


# ==============================
# PROCESS BUTTON Press, Extract text from pdf and create chuncks and store in vector db 
# ==============================

if process_button:

    if files:
        with st.spinner("Reading PDF and generating embeddings..."):
            raw_text = extract_pdf_text(files)
            st.session_state.vector_db = create_vector_store(raw_text)

        st.success("Success! Your data is embedded locally 🚀")

    else:
        st.warning("Please upload at least one PDF.")


# ==============================
# USER QUESTION AREA
# ==============================

user_question = st.text_input("Type your questions here:")


# ==============================
# BUILD RAG CHAIN
# 
# ==============================

if "vector_db" in st.session_state:

    retriever = st.session_state.vector_db.as_retriever(
        # search_type="mmr",
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    # LOCAL LLM (OLLAMA)
    llm = ChatOllama(
        model="llama3",
        temperature=0.9 # Find related ans as temperature set nearest to 0.1 - 0.3 -  2-3 . if set to 1-2 , related ans too much. 
    )

# Create Instruction Template to give Instrunction to LLM how should it work.
# "system" - Give Instruction to LLM by Guidelines 1., 2. etc
# "Context" - Use local data provided only, Not go to Internet to search out of box data.
# RAG will not use.


    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant answering questions about a PDF document.\n\n"
            "Guidelines:\n"
            "1. Provide complete answers using ONLY the context.\n"
            "2. Include relevant details and explanations.\n"
            "3. If answer not found, say politely \"Ans has been not found within local LLM\".\n\n"
            "4. Use relevant details from contexts only. \n"
            "5. Use bullet point and paragraph. \n"
            "Context:\n{context}"
        ),
        ("human", "{question}")
    ])

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    if user_question:
        response = chain.invoke(user_question)
        st.write(response)
