import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from dateutil.relativedelta import relativedelta

from pytrends.request import TrendReq

t = st.sidebar.select_slider('''
:heart: 기간 선택
''',
     options=['10년 전부터', '9년 전부터','8년 전부터','7년 전부터','6년 전부터','5년 전부터','4년 전부터','3년 전부터','2년 전부터','1년 전부터'])

t_int = int(''.join(list(filter(str.isdigit, t))))

now = datetime.datetime.now().date()
past =  datetime.datetime.now().date()-relativedelta(years= t_int)
time= str(past)+ ' ' + str(now)



# get google trends data from keyword list

def get_data1(keyword1):
    keyword = [keyword1]
    pytrend = TrendReq(hl='KR', tz=540)
    pytrend.build_payload(kw_list=keyword, geo='KR', timeframe=time)
    df = pytrend.interest_over_time()
    if df.empty:    
        st.info('검색어를 띄어 써서 다시 검색해 보세요. 또는 더 일반적인 낱말을 검색하세요.')
    else:
        df.drop(columns=['isPartial'], inplace=True)
        df.reset_index(inplace=True)
        df.columns = ["날짜 및 기간(주)"] + list(range(1,len(keyword)+1)) 
        df.set_index("날짜 및 기간(주)", inplace=True)
       
        return st.markdown(''' 
    ### 검색량 변화 그래프
    (:blue_book::검색어1) '''), st.line_chart(df, use_container_width=True)
    
    
    
    
def get_data2(keyword1, keyword2):
    keyword = [keyword1, keyword2]
    pytrend = TrendReq(hl='KR', tz=540)
    pytrend.build_payload(kw_list=keyword, geo='KR', timeframe=time)
    df = pytrend.interest_over_time()
    if df.empty:    
        st.info('검색어를 띄어 써서 다시 검색해 보세요. 또는 더 일반적인 낱말을 검색하세요.')
    else:
        df.drop(columns=['isPartial'], inplace=True)
        df.reset_index(inplace=True)
        df.columns = ["날짜 및 기간(주)"] + list(range(1,len(keyword)+1)) 
        df.set_index("날짜 및 기간(주)", inplace=True)
       
        return st.markdown(''' 
    ### 검색량 변화 그래프
    (:blue_book::검색어1   :orange_book::검색어2) '''), st.line_chart(df, use_container_width=True)

    
# sidebar
st.sidebar.write(''' # :chart_with_upwards_trend: 구글 검색량 확인하기''')

st.sidebar.markdown(
    '''
    :smile:
   지난 5년 동안 사람들이 구글과 유튜브에서 '특정 단어'를 검색한 빈도를 그래프로 확인해 봅니다. 
   시간 흐름에 따라 검색어에 대한 관심도가 가장 높을 때를 :100:으로 잡고 변화 양상을 보여줍니다. 
    ''')


n = st.sidebar.radio("검색어 개수",
     ('단어 1개', '단어 2개'), horizontal=True)

if n == '단어 1개':
    keyword1 = st.sidebar.text_input("검색어1를 입력하세요.", help="그래프가 파란색으로 그려집니다.")
    button= st.sidebar.button('검색하기')
    if button:
        if len(keyword1)==0:
            st.info('검색어를 입력하세요.')
        else: 
            get_data1(keyword1)

else:
    keyword1 = st.sidebar.text_input("검색어1를 입력하세요.", help="그래프가 파란색으로 그려집니다.")
    keyword2 = st.sidebar.text_input("검색어2를 입력하세요.", help="그래프가 주황색으로 그려집니다.")
    button= st.sidebar.button('검색하기')
    if button:
        if len(keyword1)==0 or len(keyword2)==0 :
            st.info('검색어 2개를 모두 입력하세요.')
        else: 
            get_data2(keyword1, keyword2)
            st.markdown('''	:warning: 만약 두 검색어 중 아래에 일직선으로 그려지는 그래프가 있다면 해당 검색어는 검색이 되지 않는 단어입니다.''')


