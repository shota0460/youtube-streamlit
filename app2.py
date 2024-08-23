import time
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


#アプリケーションのタイトルを表示
st.title('streamlit超入門')

st.write('インタラクティブなウィジェット')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

list()

if st.checkbox('ジャム'):
    img = Image.open('イメージ.jpg')
    st.image(img)

option = st.selectbox(
    'あなたが好きな数字は？',
    list(range(1,11))
)

'あなたの好きな数字は',option,'です。'

text = st.text_input('あなたの趣味を教えて欲しい')
condition = st.slider('あなたの今の調子は？', 0,100,50)
'あなたの趣味は',text,'です。'
'コンディション', condition