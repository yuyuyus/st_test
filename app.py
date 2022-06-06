import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


from pytrends.request import TrendReq

# get google trends data from keyword list
@st.cache(allow_output_mutation=True) #@st.cache(suppress_st_warning=True)
def get_data(keyword):
    keyword = [keyword]
    pytrend = TrendReq(hl='KR', tz=540)
    pytrend.build_payload(kw_list=keyword, geo='KR')
    df = pytrend.interest_over_time()
    if df.empty:    
        st.info('다른 단어를 검색하세요.')
    else:
        df.drop(columns=['isPartial'], inplace=True)
        df.reset_index(inplace=True)
        df.columns = ["날짜 및 기간(주)", "검색량"]
        df.set_index("날짜 및 기간(주)", inplace=True)
        
        fig, ax = plt.subplots()
        ax = df['검색량'].plot()

        ax.grid(alpha=0.3)
        ax.set(ylabel='search', xlabel='year')

        return st.pyplot(fig)

def get_data2(keyword2):
    keyword2 = [keyword2]
    pytrend = TrendReq(hl='KR', tz=540)
    pytrend.build_payload(kw_list=keyword2, geo='KR')
    df2 = pytrend.interest_over_time()
    df2.drop(columns=['isPartial'], inplace=True)
    df2.reset_index(inplace=True)
    df2.columns = ["날짜 및 기간(주)", "검색량"]
    df2.set_index("날짜 및 기간(주)", inplace=True)
    return df2

# sidebar
st.sidebar.write(''' # :chart_with_upwards_trend: 구글 검색량 확인하기''')

st.sidebar.markdown(
    '''
    :smile:
   지난 5년 동안 사람들이 구글과 유튜브에서 검색어를 검색한 빈도를 그래프로 확인해 봅니다. 
   시간 흐름에 따라 검색어에 대한 관심도가 가장 높을 때를 :100:으로 잡고 변화 양상을 보여줍니다. 
    ''')
keyword = st.sidebar.text_input("검색어1를 입력하세요.(필수)", help="그래프가 파란색으로 그려집니다.")
keyword2 = st.sidebar.text_input("검색어2를 입력하세요.(선택)", help="그래프가 주황색으로 그려집니다.")

if keyword:
    get_data(keyword)

