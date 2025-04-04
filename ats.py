import streamlit as st 
import google.generativeai as genai 
import os 
import PyPDF2 as pdf 

from dotenv import load_dotenv 
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 

def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text=''
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

input_prompt = """Hey act like a skilled ATS with deep understanding of the job description and suggest me some keywords required. Also tell me how much accurate my resume with the job description.""" 

st.title("Application Tracking System")
st.text("Improve your resume ATS") 

jd = st.text_area("Paste the job description here")
uploaded_file = st.file_uploader("Upload your resume", type=['pdf'])

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)
