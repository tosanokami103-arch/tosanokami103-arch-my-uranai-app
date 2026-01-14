import streamlit as st
import random

st.set_page_config(page_title="運勢占いデラックス", page_icon="🔮")

st.title("🔮 運勢占いデラックス")
st.write("今日のあなたの運命を、より詳しく占います。")

if st.button("運勢を占う！"):
    # 運勢とアドバイスをセットにする
    fortunes = [
        {"res": "超・大吉 🌟", "adv": "今日は無敵です！宝くじを買うなら今かも？"},
        {"res": "大吉 ✨", "adv": "最高の1日。身近な人に感謝を伝えるとさらに運気アップ！"},
        {"res": "中吉 ☀️", "adv": "安定した運気。ランチに好きなものを食べると吉。"},
        {"res": "小吉 🍀", "adv": "小さな幸せが見つかる日。足元をよく見て歩こう。"},
        {"res": "末吉 🍃", "adv": "伸びしろあり！新しい靴下を履くと気分が変わります。"},
        {"res": "凶 ☔", "adv": "今日は早めに帰ってゆっくりお風呂に浸かりましょう。"}
    ]
    
    # ランダムに1つ選ぶ
    outcome = random.choice(fortunes)
    
    # 演出
    st.balloons()
    
    # 表示を豪華にする
    st.divider() # 区切り線
    st.subheader(f"結果： {outcome['res']}")
    st.info(f"💡 アドバイス: {outcome['adv']}")
    st.divider()
