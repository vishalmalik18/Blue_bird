import streamlit as st
from main import generate_response

st.title("🦉Blue Bird")

st.write("A assistant tell about bird you never know upload image ask it")

user_input_img = st.file_uploader(
    """taking user img"""
    "",
    type=["png","jpg","jpeg"],
    label_visibility="collapsed"
)

human_input = st.text_input(
    """taking human input"""
    "Ask a question about the bird"
)

if user_input_img is not None and human_input.strip():
    img_path = user_input_img.getvalue()
    response = generate_response(human_input=human_input,img_path=img_path)
    st.write(response)