import streamlit as st
import requests

st.title("Document Research & Theme Chatbot")

st.header("Upload Document")
file = st.file_uploader("Choose a file", type=["pdf"])
ocr = st.checkbox("Run OCR?")
if file:
    files = {"file": file.getvalue()}
    try:
        res = requests.post("http://localhost:8000/upload/", files=files, params={"ocr": ocr})
        response_data = res.json()
        if "error" in response_data:
            st.error(f"Error: {response_data['error']}")
        else:
            st.success(f"Document uploaded successfully! Added {response_data.get('chunks_added', 0)} chunks.")
    except Exception as e:
        st.error(f"Error uploading document: {str(e)}")

st.header("Ask a Question")
query = st.text_input("Your query:")
if st.button("Submit"):
    try:
        res = requests.get("http://localhost:8000/query/", params={"query": query})
        response_data = res.json()
        if "error" in response_data:
            st.error(f"Error: {response_data['error']}")
        else:
            st.subheader("Answer")
            st.write(response_data.get("answer", "No answer available"))
            st.subheader("Citations")
            for cite in response_data.get("citations", []):
                st.write(f"{cite['doc_id']}: {cite['text'][:200]}")
    except Exception as e:
        st.error(f"Error processing query: {str(e)}")