import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Welcome to our Movie Recommender App! (PSL Project 4)")
st.write("Authors: Justin Martin and Dillon Harding")

remote_image_url = 'https://raw.githubusercontent.com/jcm-art/uiuc_psl_public_streamlit/main/src/resources/front_page.png'

st.image(remote_image_url, use_column_width=True)

st.sidebar.success("Select a demo above.")