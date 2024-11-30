import streamlit as st
import requests
from random import shuffle 

from constants import ENDPOINT
from utils import WordPair

@st.cache_data
def init_(x):
    # this functi0on is called only once at the beginning
    # initiialize the index: TODO improve this
    st.session_state['index']=0
    
    # get all the topics for selection
    st.session_state['topics'] = get_topics(1)
    
@st.cache_data
def get_topics(x):
    # gets unique topics from database
    topic_response = requests.get(f"{ENDPOINT}/topics/")
    topic_list=[t['topic'] for t in topic_response.json()]
    topic_list.sort()
    return topic_list

def get_chapters(topic):
    response = requests.get(f"{ENDPOINT}/chapters/{topic}")
    response_list = [ch['chapter'] for ch in response.json()]
    response_list.sort()
    return response_list   

@st.cache_data 
def get_pairs(request_string):
    # gets called for each new request_Stiring - otherwise data cached
    response = requests.get(request_string)
    pair_list = response.json()
    shuffle(pair_list)
    st.session_state['index'] = 0
    return pair_list

def change_index(delta):
    st.session_state.index = (st.session_state.index + delta) % len(st.session_state.pair_list)
    return 1

def data_selection():
    with st.sidebar:
        hide = st.radio("Hide:", ("left", "right", "none"))
        
    st.divider()
    
    with st.sidebar:
        topic_name = st.radio("Topic:", st.session_state['topics'])
    
    # get chapters depending on selected topic:
    available_chapters = get_chapters(topic_name)
    with st.sidebar:
        chapter_name = st.radio("Kapitel:", available_chapters)   
        
    request_string = f"{ENDPOINT}/pairs/topic/{topic_name}/chapter/{chapter_name}"
    return request_string, hide
   

def display(word_pair, solver):
    
    pass 

def main():
    init_(5)
    st.title('learning app')
    st.text('hello')
    
    request_string, hide = data_selection()
    st.session_state['pair_list'] = get_pairs(request_string)
    st.text(f"list: {st.session_state['pair_list'][0]} hide: {hide}")
    # index_list = [k for k in len(pair_list)]
    st.text(f"index {st.session_state.index}")

    # depending on which side is hidden:
    word_pair = WordPair(
        left_word=st.session_state.pair_list[st.session_state.index]['left'], 
        right_word=st.session_state.pair_list[st.session_state.index]['right'], 
        hidden_side=hide
        )

    col1, col2 = st.columns(2)
    with col1:
        st.header(word_pair.display()[0])
        st.button(
            label="back", 
            on_click=change_index, 
            args=[-1], 
            use_container_width=True)
        
    with col2:
        st.header(word_pair.display()[1])
        st.button(
            label="next", 
            on_click=change_index, 
            args=[1],   
            use_container_width=True)
        st.button(
            label='solve')
    
    
main()
    