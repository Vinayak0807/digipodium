import streamlit as st
import re

# Load the extracted text
with open('/mnt/data/physics_text.txt', 'r', encoding='utf-8') as text_file:
    pdf_text = text_file.read()

# Function to find the answer in the text
def find_answer(question, text):
    # Simple keyword matching (for demonstration purposes)
    pattern = re.compile(re.escape(question), re.IGNORECASE)
    matches = pattern.findall(text)
    if matches:
        # Return the context around the first match
        match_index = text.lower().find(question.lower())
        context_start = max(0, match_index - 100)  # 100 characters before the match
        context_end = min(len(text), match_index + 100 + len(question))  # 100 characters after the match
        return text[context_start:context_end]
    return "Answer not found."

# Streamlit app layout
st.title("Physics Answers")

# Input for the question
question = st.text_input("Enter your question:")

if question:
    # Find and display the answer
    answer = find_answer(question, pdf_text)
    st.write("**Answer:**", answer)
