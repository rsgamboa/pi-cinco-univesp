import streamlit as st
from pathlib import Path
import base64
import pandas as pd
import numpy as np

# Initial page config

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()

    return None

# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar

def cs_sidebar():

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=162 height=auto>](https://streamlit.io/)'''.format(img_to_bytes("logo-univesp-white.png")), unsafe_allow_html=True)
    st.sidebar.header('Projeto Integrador IV')
    
    st.sidebar.markdown('''
<small>Dashboard desenvolvida para analise de comparação do 5G entre Brasil e Korea doo Sul</small>
''', unsafe_allow_html=True)

    return None


# body

def cs_body():

    col1, col2 = st.columns(2)

    # Dashboard Left

   

    

    # Dashboard Right

 



    return None



    # Run main()

if __name__ == '__main__':
    main()
