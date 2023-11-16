import streamlit as st
from pathlib import Path
import base64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Initial page config
st.set_page_config(
    page_title='Dashboard 5G',
    layout="wide",
    initial_sidebar_state="expanded",
)
#CELULARES_URL = pd.read_csv('modelos_celulares_5g.csv')
#ANTENAS_URL = pd.read_csv('lista-de-antenas.csv')


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

    #col1, col2 = st.columns(2)

    # Dashboard Left
    #col1.subheader('Modelos de Celulares com 5G')
    # Carrega os dados do arquivo CSV
    #df = pd.read_csv('data/modelos_celulares_5g.csv')
    # Exibe a tabela
    #st.table(df)

    # Dashboard Right
    #col2.subheader('Antenas 5G Instaladas')
    # Carrega os dados do arquivo CSV
    #df = pd.read_csv('lista-de-antenas.csv')
    # Exibe a tabela
    #col2.table(df)

    mobile = pd.read_csv('data/modelos_celulares_5g.csv')
    mobile = mobile.groupby(['Fabricante']).size() 
    st.header('Qtd de celulares com 5G por fabricantes - 2022-2023')

    st.bar_chart(mobile)





    return None


if __name__ == '__main__':
    main()
