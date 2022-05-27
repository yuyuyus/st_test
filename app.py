import streamlit as st
import datetime
import pandas as pd

#@st.cache(allow_output_mutation=True)

            
def problem():
    input1 = st.text_input('정답 단어')
    input2 = st.text_input('헷갈리게 하는 단어')
    #date=datetime.now().strftime('%Y-%m-%d')
    df=pd.DataFrame({
'정답': input1,
'헷갈': input2
})
    return df

'''
    if st.button('만들기'):
        option = st.radio("문제", ('미선택',input1, input2))
        if option == input1:
            st.success('정답입니다.')
''' 

problem()
if st.button('만들기'):
    st.table(df)


