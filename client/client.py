import streamlit as st
import requests
from random import shuffle 

from constants import ENDPOINT
from utils import WordList

@st.cache_data
def init_(x):
    st.session_state['index']=0
    topic_response = requests.get(f"{ENDPOINT}/topics/")
    st.session_state['topics']=[t['topic'] for t in topic_response.json()]
   
@st.cache_data 
def get_pairs(request_string):
    response = requests.get(request_string)
    pair_list = response.json()
    shuffle(pair_list)
    # st.session_state['pair_list'] = pair_list
    st.session_state['index'] = 0
    return pair_list

def get_chapters(topic):
    response = requests.get(f"{ENDPOINT}/chapters/{topic}")
    return [ch['chapter'] for ch in response.json()]

def change_index(delta):
    st.session_state.index = (st.session_state.index + delta) % len(st.session_state.pair_list)
    return 1

def data_selection():
    
    with st.sidebar:
        hide = st.radio("Hide:", ("left", "right"))
        
    st.divider()
    
    with st.sidebar:
        #topic_name = st.radio("Topic:", ("englisch", "geografie", "czech"))
        topic_name = st.radio("Topic:", st.session_state['topics'])
    
    # get chapters depending on selected topic:
    available_chapters = get_chapters(topic_name)
    with st.sidebar:
        #chapter_name = st.radio("Kapitel:", ("unit 1", "kapitel 1", "verbs unit 2"))
        chapter_name = st.radio("Kapitel:", available_chapters)   
        
    request_string = f"{ENDPOINT}/pairs/topic/{topic_name}/chapter/{chapter_name}"
    
    return request_string, hide


def setup():
    pass 

def main():
    init_(1)
    st.title('learning app')
    st.text('hello')
    
    request_string, hide = data_selection()
    st.session_state['pair_list'] = get_pairs(request_string)
    st.text(f"list: {st.session_state['pair_list'][0]} hide: {hide}")
    # index_list = [k for k in len(pair_list)]
    st.text(f"index {st.session_state.index}")

    # depending on which side is hidden:
    word_list = WordList(
        left_word=st.session_state.pair_list[st.session_state.index]['left'], 
        right_word=st.session_state.pair_list[st.session_state.index]['right'], 
        hidden_side=hide
        )

    col1, col2 = st.columns(2)
    with col1:
        st.header(word_list.display()[0])
        st.button(
            label="back", 
            on_click=change_index, 
            args=[-1], 
            use_container_width=True)
        
    with col2:
        st.header(word_list.display()[1])
        st.button(
            label="NEXT", 
            on_click=change_index, 
            args=[1],   
            use_container_width=True)
    
    
main()
    