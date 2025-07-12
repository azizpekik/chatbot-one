import streamlit as st
import PyPDF2
import requests
import os

# Ganti dengan API KEY Gemini Anda
API_KEY = "AIzaSyCKx2VMnersSapyvOxBdwkKySwaKNrktb8"

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def gemini_chat(context, user_message):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=" + API_KEY
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": f"Konteks: {context}\n\nPertanyaan: {user_message}\nJawab hanya berdasarkan konteks di atas."}]}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        try:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            return "[Gagal mengambil jawaban dari Gemini API]"
    else:
        return f"[Error: {response.status_code}] {response.text}"

st.title("Chatbot Gemini - PDF Context Only (API Key di Kode)")

if "pdf_context" not in st.session_state:
    st.session_state["pdf_context"] = ""
if "history" not in st.session_state:
    st.session_state["history"] = []

uploaded_pdf = st.file_uploader("Upload file PDF sebagai konteks:", type=["pdf"])
if uploaded_pdf:
    st.session_state["pdf_context"] = extract_text_from_pdf(uploaded_pdf)
    st.success("PDF berhasil dibaca dan dijadikan konteks.")

if st.session_state["pdf_context"]:
    user_input = st.text_input("Tulis pertanyaan Anda:")
    if st.button("Kirim") and user_input:
        with st.spinner("Meminta jawaban ke Gemini..."):
            answer = gemini_chat(st.session_state["pdf_context"], user_input)
        st.session_state["history"].append((user_input, answer))

if st.session_state["history"]:
    st.write("## Riwayat Percakapan")
    for q, a in st.session_state["history"]:
        st.markdown(f"**Anda:** {q}")
        st.markdown(f"**Gemini:** {a}")
