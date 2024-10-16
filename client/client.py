import streamlit as st
import requests
from constants import ENDPOINT

    
def side():
    with st.sidebar:
        topic_name = st.radio("Topic:", ("englisch", "geografie"))
        
    with st.sidebar:
        chapter_name = st.radio("Kapitel:", ("unit 1", "kapitel 1"))
    
    request_String = f"{ENDPOINT}/pairs/topic/{topic_name}/chapter/{chapter_name}"
    st.text(request_String)
    response = requests.get(request_String)
    pair_list = response.json()
    
    col1, col2 = st.columns(2)

    counter = 0

    with col1:
        st.header(f"{pair_list[counter]['left']}")
    
    with col2:
        st.header(f"{pair_list[counter]['right']}")
    
    
    #st.session_state['pair_list'] = response.json()

def setup():
    
    # pair_list = requests()
    
    st.title('learning app')
    st.text('hello')
    #st.text(st.session_state.pair_list)
    
def main():
    setup()
    side()

main()
    