import streamlit as st
from streamlit_shortcuts import button, add_keyboard_shortcuts
import requests
from random import shuffle 

from constants import ENDPOINT
from utils import WordPair

@st.cache_data
def init_(x):
    # this functi0on is called only once at the beginning
    # initiialize the index: TODO improve this
    st.session_state['index'] = 0
    st.session_state['solver'] = False
    
    # get all the topics for selection
    tag_response = requests.get(f"{ENDPOINT}/tags/")
    tag_list = tag_response.json()
    tag_list.sort()
    st.session_state['tags'] = tag_list
    
# @st.cache_data
# def get_tags(x):
#     # gets unique topics from database
#     tag_response = requests.get(f"{ENDPOINT}/tags/")
#     tag_list = tag_response.json()
#     tag_list.sort()
#     return tag_list

@st.cache_data 
def get_pairs(tag_list):
    # gets called for each new request_Stiring - otherwise data cached
    response = requests.post(url=f"{ENDPOINT}/pair/pair_by_tags/", json={"tags": tag_list})
    pair_list = response.json()
    shuffle(pair_list)
    st.session_state['index'] = 0
    return pair_list

def change_index(delta):
    st.session_state.index = (st.session_state.index + delta) % len(st.session_state.pair_list)
    st.session_state.solver = False
    return 1

def set_solver_true():
    st.session_state.solver = True
    return 1

def data_selection():
    with st.sidebar:
        hide = st.radio("Hide:", ("left", "right", "none"))
        
    st.divider()
    
    with st.sidebar:
        tags = st.multiselect("Tags", st.session_state['tags'], st.session_state['tags'][0])

    return tags, hide
    
    # # get chapters depending on selected topic:
    # available_chapters = get_chapters(topic_name)
    # with st.sidebar:
    #     chapter_name = st.radio("Kapitel:", available_chapters)   
        
    # request_string = f"{ENDPOINT}/pairs/topic/{topic_name}/chapter/{chapter_name}"
    # return request_string, hide
   

def display_block(word_pair, solver):
    
    if solver == False:
        active_pair = word_pair.display()
    if solver == True:
        active_pair = word_pair.solve()
        
    col1, col2 = st.columns(2)   
    with col1:
        st.header(active_pair[0])
        # st.button(label="back", on_click=change_index, args=[-1], use_container_width=True)
        button(label='back', shortcut='Alt+ArrowLeft', on_click=change_index, args=[-1], use_container_width=True)
        
    with col2:
        st.header(active_pair[1])
        # st.button(label="next", on_click=change_index, args=[1], use_container_width=True)   
        button(label='next', shortcut='Alt+ArrowRight', on_click=change_index, args=[1], use_container_width=True)
    pass 

def main():
    init_(26)
    st.title('learning app')
    st.text('hello')
    x = requests.get(f"{ENDPOINT}")
    st.text(x.json()['message'])
    
    # st.text(st.session_state['index'])
    # st.text(st.session_state['tags'])
    selected_tags, hide = data_selection()
    st.text(selected_tags)
    st.session_state['pair_list'] = get_pairs(selected_tags)
    # response = requests.post(url=f"{ENDPOINT}/pair/pair_by_tags/", data=selected_tags)
    # pair_list = response.json()
    st.text(st.session_state['pair_list'][0])
    # st.text(f"list: {st.session_state['pair_list'][0]} hide: {hide}")
    # # index_list = [k for k in len(pair_list)]
    # st.text(f"index {st.session_state.index}")

    # # depending on which side is hidden:
    # word_pair = WordPair(
    #     left_word=st.session_state.pair_list[st.session_state.index]['left'], 
    #     right_word=st.session_state.pair_list[st.session_state.index]['right'], 
    #     hidden_side=hide
    #     )

    # display_block(word_pair=word_pair, solver=st.session_state.solver)
    
    # #st.button('solve', 'Alt+Space', on_click=set_solver_true)
    # c1, c2, c3 = st.columns(3)
    # with c1:
    #     pass
    # with c2:
    #     button(label='solve', shortcut='Alt+Enter', on_click=set_solver_true, use_container_width=True) 
        
    # with c3:
    #     pass
    
    
    
main()

