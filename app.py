import streamlit as st
import datetime
import pandas as pd


st.title('내가 찾은 단어 담벼락')

@st.cache(allow_output_mutation=True)

input1 = st.text_input('정답 단어')
    input2 = st.text_input('헷갈리게하는 단어')
    if st.button('만들기'):
        option = st.radio("문제", (input1, input2))
        if option == input1:
            st.success('정답입니다.')

            
def problem():
    input1 = st.text_input('정답 단어')
    input2 = st.text_input('헷갈리게하는 단어')
    if st.button('만들기'):
        option = st.radio("문제", (input1, input2))
        if option == input1:
            st.success('정답입니다.')

problem()



