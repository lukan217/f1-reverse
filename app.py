import streamlit as st
import pandas as pd

@st.cache
def load_data():
    df = pd.read_csv("df.csv")
    df['score'] = df['score'].round(8)
    return df
df = load_data()
st.title("f1分数解析")
st.write("能源大数据子赛道——污染源超限排放研判")
st.write("比赛地址: https://www.dcic-china.com/competitions/10024")
score = st.text_input('输入排行榜得分', '0.66484404126')
try:
    score = round(float(score),8)
    result = df[df.score==score].iloc[0]
    st.write("*************")
    st.write(f"你预测了{int(result['pred_num'])}个异常用户")
    st.write(f"预测对了{int(result['pred_true_num'])}个用户，预测错了{int(result['pred_num']-result['pred_true_num'])}个用户")
    dif = 144-int(result['pred_true_num'])
    if dif != 0:
        st.write(f"总共有144个异常用户，还差{dif}个异常用户没找到")
    else:
        st.write("居然全找到了！🐂🍺")
    st.write("*************")
except:
    st.write("输入有误请重试！")
st.write("预祝各位都能拿满分🎉！DF平台越办越棒！")
st.write("by szp")
