import pandas as pd
from PyPDF2 import PdfReader  # Changed from PdfFileReader to PdfReader
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#defining a function to extract text from pdf files
def extract_text_from_pdf(file):
    pdf = PdfReader(file)  # Changed from PdfFileReader to PdfReader
    text = ""
    for page in pdf.pages:  # This should still work with PdfReader
        text += page.extract_text()
    return text

#function to rank resume based on job description
def rank_resumes(resumes, job_description):
    # Extract text from job descriptiont
    documents = [job_description] + resumes
    # Create a TfidfVectorizer
    vectorizer = TfidfVectorizer().fit_transform(documents)
    # Compute cosine similarity
    vectors = vectorizer.toarray()

    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarity_scores = cosine_similarity(job_description_vector.reshape(1, -1), resume_vectors)
    return cosine_similarity_scores

#streamlit app
st.title("AI RESUME SCREENING & CANDIDATE RANKING SYSTEM")

#JOB DESCRIPTION INPUT
job_description = st.text_area("Enter job description")
#FILE UPLOADER
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Choose files", type=['pdf'], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")
    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)

    #rank resumes
    scores = rank_resumes(resumes, job_description)
    #convert scores to percentage
    percentage_scores = [round(score * 100, 2) for score in scores[0]]
    #display ranking
    results = pd.DataFrame({"resume": [file.name for file in uploaded_files], 
                           "match_percentage": percentage_scores})
    results = results.sort_values("match_percentage", ascending=False)
    st.write(results)

