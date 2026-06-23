import streamlit as st


def style_base_home():
    st.markdown("""
    <style>

    /* Purple Background */
    [data-testid="stAppViewContainer"] {
        background-color: #5865F2 !important;
    }

    /* Main Content Area */
    .main {
        background-color: #5865F2 !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #5865F2 !important;
    }

    /* Column Styling */
    .stApp div[data-testid="stColumn"] {
        background-color: #E0E3FF !important;
        padding: 2.5rem !important;
        border-radius: 5rem !important;
    }

    </style>
    """, unsafe_allow_html=True)


def style_base_dashboard():
    st.markdown("""
    <style>

    [data-testid="stAppViewContainer"] {
        background-color: #E0E3FF !important;
    }

    .main {
        background-color: #E0E3FF !important;
    }

    </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    .block-container {
        padding-top: 1.5rem !important;
    }
                

    h1, h2 {
    font-family: 'Climate Crisis', sans-serif !important;
    font-size: 2rem !important;
    line-height: 0.9 !important;
    margin-bottom: 0rem !important;
    }

    h3, h4, p {
    font-family: 'Outfit', sans-sarif;
    }
                
    button{
    border-radius: 1.5rem !important;
    background: #5865F2 !important;
    color: white !important;
    padding: 10px 20px !important;
    border: none !important;
    transition: transform 0.25s ease-in-out !important;
    }

    button[kind="secondary"]{
    border-radius: 1.5rem !important;
    background: #EB459E !important;
    color: white !important;
    padding: 10px 20px !important;
    border: none !important;
    transition: transform 0.25s ease-in-out !important;
    }
                
    button[kind="tertiary"]{
    border-radius: 1.5rem !important;
    background: black !important;
    color: white !important;
    padding: 10px 20px !important;
    border: none !important;
    transition: transform 0.25s ease-in-out !important;
    }
                
    button:hover{
    transform: scale(1.05)
    }

    </style>
    """, unsafe_allow_html=True)