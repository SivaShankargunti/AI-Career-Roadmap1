from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Career Roadmap")
st.header("AI-Powered Student Career Roadmap Generator")

name = st.text_input("Name")
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
target_role = st.text_input("Target Job Role")
career_goal = st.text_area("Career Goal")

def generate_roadmap(name, experience, target_role, career_goal):
    prompt = f"""
    Create a detailed career roadmap for {name}, a {experience} level student
    targeting the role {target_role}. Career goal: {career_goal}.
    Include skills, learning stages, tools, projects, timeline and motivation.
    """
    resp = model.generate_content(prompt)
    return resp.text

if st.button("Generate Roadmap"):
    with st.spinner("Generating..."):
        roadmap = generate_roadmap(name, experience, target_role, career_goal)
    st.markdown(roadmap)
