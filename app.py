# AI Career Roadmap Generator

import os

from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY is not set in your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit page config
st.set_page_config(page_title="Career Roadmap")
st.header("AI-Powered Student Career Roadmap Generator")

# User inputs
name = st.text_input("Name")
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
target_role = st.text_input("Target Job Role")
career_goal = st.text_area("Career Goal")

def generate_roadmap(name, experience, target_role, career_goal):
    prompt = (
        f"Create a detailed career roadmap for {name}, a {experience} level student "
        f"targeting the role {target_role}. Career goal: {career_goal}. "
        "Include skills, learning stages, tools, projects, timeline and motivation."
    )
    resp = model.generate_content(prompt)
    return resp.text

# Generate button
if st.button("Generate Roadmap"):
    if not name or not target_role or not career_goal:
        st.warning("Please fill in all the fields before generating the roadmap.")
    else:
        with st.spinner("Generating..."):
            roadmap = generate_roadmap(name, experience, target_role, career_goal)
        st.markdown(roadmap)

