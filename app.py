import streamlit as st
from pathlib import Path
import base64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

# Initial page config
st.set_page_config(
    page_title='Dashboard 5G',
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()

    return None

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar

def cs_sidebar():

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=162 height=auto>](https://streamlit.io/)'''.format(img_to_bytes("logo-univesp-white.png")), unsafe_allow_html=True)
    st.sidebar.header('Projeto Integrador IV')
    
    st.sidebar.markdown('''
    <small>Esta Dashboard foi desenvolvida para analise de comparação da rede 5G entre Brasil e Korea do Sul, para o projeto integrador IV da UNIVESP.</small>
    ''', unsafe_allow_html=True)

    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small>Dashboard 5G v1.0 | Nov 2023 | Univesp</small>''', unsafe_allow_html=True)


    return None


# body

def cs_body():

    # qtd de celulares com 5G por fabricantes - 2022-2023
    qtdmf = pd.read_csv('data/modelos_celulares_5g.csv')
    qtdmf = qtdmf.groupby(['Fabricante']).size() 
    st.header('Celulares fabricados com 5G | 2022-2023', divider='gray')
    st.markdown('Brasil and South Korea')
    st.bar_chart(qtdmf)

      
    col1, col2 = st.columns(2)

    # Coluna Brasil
    with col1:
        st.subheader('Teste de Velocidade 5G', divider='gray')
        st.markdown('Brasil')
        x1 = np.random.randn(446) - 2
        x2 = np.random.randn(85)
        x3 = np.random.randn(23) + 2

        # Group data together
        hist_data = [x1, x2, x3]
                             
        group_labels = ['23mbps Upload', '85mbps Live', '446mbps Download']

        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])

        # Plot!
        st.plotly_chart(fig, use_container_width=True)


        # Evolucao Municipios 5G 
        st.subheader('Antenas 5G Instaladas', divider='gray')
        st.markdown('Brasil')
        evo = pd.read_csv('data/brasil-antenas-5g.csv')
        st.line_chart(evo, x="DATA", y=["CLARO-5G", "TIM-5G", "VIVO-5G", "ALGAR-5G", "TODAS-5G"])

    

    with col2:
        st.subheader('Teste de Velocidade 5G', divider='gray')
        st.markdown('South Korea')
        x1 = np.random.randn(968) - 2
        x2 = np.random.randn(120)
        x3 = np.random.randn(531) + 2

        # Group data together
        hist_data = [x1, x2, x3]

        group_labels = ['531mbps Upload', '120mbps Live', '968mbps Download']

        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])

        # Plot!
        st.plotly_chart(fig, use_container_width=True)
        
        # Evolucao Municipios 5G 
        st.subheader('Antenas 5G Instaladas', divider='gray')
        st.markdown('South Korea')
        evo = pd.read_csv('data/korea-antenas-5g.csv')
        st.line_chart(evo, x="DATA", y=["SKT-5G", "KT-5G", "TOTAL-5G"])

        
      

    return None


if __name__ == '__main__':
    main()
