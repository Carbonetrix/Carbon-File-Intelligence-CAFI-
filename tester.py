import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader 
import os
# import fitz

import tempfile
import base64
import io
from docx import Document


st.set_page_config(layout="wide", page_title="Document Intelligence")

st.markdown("""
<style>
    .stButton > button {
        color: #000000;
        background-color: #2CD6FF;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #1C277F;
        color: #ffffff;
        transform: scale(1.05);
    }
    .stTextInput > div > div > input {
        border-radius: 4px;
    }
    .stSelectbox > div > div > select {
        border-radius: 4px;
    }
    .stFileUploader > div > div > button {
        color: #ffffff;
        background-color: #2CD6FF;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stFileUploader > div > div > button:hover {
        background-color: #2CD6FF;
    }
    .stExpander {
       
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stContainer {
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stChatMessage {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 0.5rem;
        margin-top: 0.5rem;
        display: flex;
        align-items: flex-start;
    }
    .stChatMessage.user {
        justify-content: flex-end;
        background-color: #ecfdff;
        width: 85%;
        float: right;
        border-radius: 25px 0px 25px 25px;
    }
    .stChatMessage.assistant {
        justify-content: flex-start;
        background-color: #f7f7f7;
        width: 85%;
        float: left;
        border-radius: 0px 25px 25px 25px;
    }
    .stChatMessage img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin: 0 10px;
    }
    .st-emotion-cache-eqffof {
    font-family: "Source Sans Pro", sans-serif;
        margin-bottom: 0px;
    }
</style>
""", unsafe_allow_html=True)

def page_setup():
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

def get_typeofpdf():
    st.sidebar.title("Carbon-File-Intelligence (CAFI)")
    #st.sidebar.write("<hr>", unsafe_allow_html=True)
    typepdf = st.sidebar.radio("Select media type:",
                               (
                                
                                "Video",
                                ))
    return typepdf


def summarize_content(content, file_type):
    # Only generate summary if it hasn't been generated yet
    if st.session_state.summary_text is None:
        generation_config = {
            "temperature": 0.7,
            "top_p": 1,
            "max_output_tokens": 1024,
        }
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)

        if file_type == "document":
            prompt = f"""
            Please provide a concise summary of the following document:

            {content}

            Summarize the main points and key information in a clear and organized manner.
            """
            response = model.generate_content(prompt)
        else:
            prompt = f"Please provide a detailed description and summary of this {file_type}."
            response = model.generate_content([content, prompt],)

        
        
        # Store the summary in session state
        st.session_state.summary_text=response.text
        

def main():
    page_setup()
    typepdf = get_typeofpdf()
    
    # Move uploader to sidebar
    with st.sidebar:
        st.subheader("Upload File")
        if typepdf == "Documents":
            uploaded_files = st.file_uploader("Choose one or more documents", type=['pdf', 'doc', 'docx', 'txt'], accept_multiple_files=True)
        elif typepdf == "Images":
            image_file = st.file_uploader("Upload your image file.", type=["jpg", "jpeg", "png"])
        elif typepdf == "Video":
            video_file = st.file_uploader("Upload your video", type=["mp4"])
        elif typepdf == "Audio":
            audio_file = st.file_uploader("Upload your audio", type=["mp3", "wav"])
    
    # Move model configuration after uploader
    # model_name, temperature, top_p, max_tokens = get_llminfo()
    
    # Create two columns for layout
    col1, col2 = st.columns([0.5, 0.5])
    
    # Initialize or reset session state for uploaded content and messages
    if "current_media_type" not in st.session_state or st.session_state.current_media_type != typepdf:
        st.session_state.uploaded_content = None
        st.session_state.file_type = None
        st.session_state.messages = []
        st.session_state.current_media_type = typepdf
        st.session_state.summary_text=None

    with col1:

        if typepdf == "Video" and video_file:
            st.video(video_file)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4",) as temp_file:
                temp_file.write(video_file.read())
                temp_file_path = temp_file.name

            st.session_state.uploaded_content = genai.upload_file(path=temp_file_path)
            st.session_state.file_type = "video"


            summarize_content(st.session_state.uploaded_content, "video")

            if st.session_state.summary_text is not None:
                with st.expander("Click to view the summary", expanded=False):
                    st.subheader("Video Summary")
                    st.info(st.session_state.summary_text)
                
        else:
            st.info(f"Please upload {typepdf.lower()}")

    
if __name__ == '__main__':
    # GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key="AIzaSyDziN0csVOFMGAw7AQwuKO6Z29eUfpFuC0")
    main()