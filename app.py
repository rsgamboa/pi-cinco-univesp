import streamlit as st
from pathlib import Path
import base64

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

    return None


# body

def cs_body():

    return None
    


    # Run main()

if __name__ == '__main__':
    main()
