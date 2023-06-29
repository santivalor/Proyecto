#CSS styles---------
import streamlit as st
import base64

def apply_styles():

        main_bg_ext = "png"
       
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open('img/background.png', "rb").read()).decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )



