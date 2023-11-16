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

    col1, col2 = st.columns(2)

    # Coluna Brasil
    with col1:
        st.header('Brasil')
   
        mobile = pd.read_csv('data/modelos_celulares_5g.csv')
        mobile = mobile.groupby(['Fabricante']).size() 
        st.subheader('Qtd de celulares com 5G por fabricantes - 2022-2023')

        st.bar_chart(mobile)

        antenas = pd.read_csv('data/lista-de-antenas.csv')
        antenas = antenas.groupby(['Operadora']).size() 
        st.subheader('Antenas Instaladas Por Operadora - 2022-2023')

        st.bar_chart(antenas)


    with col2:
        st.header('South Korea')
   
        mobile = pd.read_csv('data/modelos_celulares_5g.csv')
        mobile = mobile.groupby(['Fabricante']).size() 
        st.subheader('Qtd de celulares com 5G por fabricantes - 2022-2023')

        st.bar_chart(mobile)

        antenas = pd.read_csv('data/lista-de-antenas.csv')
        antenas = antenas.groupby(['Operadora']).size() 
        st.subheader('Antenas Instaladas Por Operadora - 2022-2023')

        st.bar_chart(antenas)


    tab_titles = ('Brasil', 'South Korea')
    tab1, tab2 = st.tabs(tab_titles)

    with tab1:
        st.header('Brasil')
   
        mobile = pd.read_csv('data/modelos_celulares_5g.csv')
        mobile = mobile.groupby(['Fabricante']).size() 
        st.subheader('Qtd de celulares com 5G por fabricantes - 2022-2023')

        st.bar_chart(mobile)

        antenas = pd.read_csv('data/lista-de-antenas.csv')
        antenas = antenas.groupby(['Operadora']).size() 
        st.subheader('Antenas Instaladas Por Operadora - 2022-2023')

        st.bar_chart(antenas)


    with tab2:
        st.header('South Korea')
   
        mobile = pd.read_csv('data/modelos_celulares_5g.csv')
        mobile = mobile.groupby(['Fabricante']).size() 
        st.subheader('Qtd de celulares com 5G por fabricantes - 2022-2023')

        st.bar_chart(mobile)

        antenas = pd.read_csv('data/lista-de-antenas.csv')
        antenas = antenas.groupby(['Operadora']).size() 
        st.subheader('Antenas Instaladas Por Operadora - 2022-2023')

        st.bar_chart(antenas)

    return None


if __name__ == '__main__':
    main()
