import streamlit as st
from streamlit.logger import get_logger
from streamlit_shortcuts import button
import requests
from random import shuffle 

from constants import ENDPOINT
from utils import Pair 

@st.cache_data(show_spinner="Fetching data from API...")
def init_(x):
    # this functi0on is called only once at the beginning
    # initiialize the index: TODO improve this
    st.session_state['logger'].info("initialize app-state")
    st.session_state['index'] = 0
    st.session_state['solver'] = False
    st.session_state['hide'] = 'left'
    st.session_state['tags'] = get_tags()
    st.session_state['selected_tags'] = []
    st.session_state['pair_list'] = get_pairs(tag_list=[])
    return x

def debug_session_state():
    debug_str = f"index: {st.session_state['index']}"
    debug_str += f" tags: {len(st.session_state['selected_tags'])}"
    debug_str += f" pairs: {len(st.session_state['pair_list'])}"
    return debug_str
    
# @st.cache_data
def get_tags(x=1):
    # gets unique topics from database
    tag_response = requests.get(f"{ENDPOINT}/tags/")
    tag_list = tag_response.json()
    tag_list.sort()
    return tag_list

@st.cache_data(show_spinner="Fetching data from API...", ttl=3600) 
def get_pairs(tag_list):
    # gets called for each new request_Stiring - otherwise data cached
    st.session_state['logger'].info("get pairs from database:")
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
    st.session_state['logger'].info("TAG selection....")
    with st.sidebar:
        hide = st.radio("Hide:", ("left", "right", "none"))
        st.session_state['hide'] = hide
        
    st.divider()
    
    with st.sidebar:
        form = st.form(key = 'myform', clear_on_submit = False)
        with form:
            tags = st.multiselect(
                label="Tags", 
                options=st.session_state['tags'], 
                default=st.session_state['selected_tags']
                )    
            submit = form.form_submit_button('load pairs')
            if submit:
                tags.sort()
                st.session_state['selected_tags'] = tags
                #return tags, hide
    

def display_block(word_pair, solver):
    
    if solver == False:
        active_pair = word_pair.display(hidden_side=st.session_state['hide'])
    if solver == True:
        active_pair = word_pair.solve()
        
    col1, col2 = st.columns(2)   
    with col1:
        st.header(active_pair[0]) # word
        button(label='back', shortcut='Alt+ArrowLeft', on_click=change_index, args=[-1], use_container_width=True)
        
    with col2:
        st.header(active_pair[1]) # word
        button(label='next', shortcut='Alt+ArrowRight', on_click=change_index, args=[1], use_container_width=True)
    pass 

def main():
    
    st.session_state['logger'] = get_logger(__name__)
    
    init_(5)
    
    st.session_state['logger'].info('rerun main')  
    st.session_state['logger'].info(f"session state {debug_session_state()}")
    
    st.title('learning app')
        
    x = requests.get(f"{ENDPOINT}")
    if x.status_code==200:
        st.session_state['logger'].info(f"API ALIVE: {x.json()}")  
    
    st.text(f"session state: {debug_session_state()}")
    
    data_selection()
    st.session_state['pair_list'] = get_pairs(st.session_state['selected_tags'])
    
    word_pair = Pair(**st.session_state.pair_list[st.session_state.index])

    display_block(word_pair=word_pair, solver=st.session_state.solver)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        pass
    with c2:
        button(label='solve', shortcut='Alt+Enter', on_click=set_solver_true, use_container_width=True) 
        
    with c3:
        pass
    
        
main()

