import streamlit as st
import datetime
import pandas as pd

#@st.cache(allow_output_mutation=True)
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


'''
w1 = st.text_input('정답 단어')
w2 = st.text_input('헷갈리게 하는 단어')
date=datetime.now().strftime('%Y-%m-%d')
df=pd.DataFrame([date, w1, w2], columns=['날짜','정답','오답'])
#return df
st.table(df)

print('당신은 번호 '+str(number)+'번 '+name+'이며, 혈액형은 '+blood+'형인 '+gender+'입니다. 맞습니까? 맞으면 다음 단계로 넘어가세요.')
input_info=[number,name,blood,gender]
globals()['input_info_{}'.format(number)]= input_info
all_data.loc[number]=globals()['input_info_{}'.format(number)]
all_data= all_data.sort_index()
'''
