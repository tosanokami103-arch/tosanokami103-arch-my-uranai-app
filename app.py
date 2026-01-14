import streamlit as st
import random

# タイトル
st.title("🐍 Python Web占い")

# 説明文
st.write("ボタンを押して、今日の運勢を占ってみよう！")

# ボタン
if st.button("占う！"):
    results = ["大吉", "中吉", "小吉", "凶"]
    lucky_result = random.choice(results)
    
    # 結果表示
    st.balloons() # 風船を飛ばす演出！
    st.header(f"結果は... **{lucky_result}** です！")
