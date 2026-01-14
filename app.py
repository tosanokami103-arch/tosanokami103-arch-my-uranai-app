import streamlit as st
import random

# ページのタイトル設定
st.set_page_config(page_title="運勢占いデラックス", page_icon="🔮")

st.title("🔮 運勢占いデラックス")
st.write("ボタンを押して、今日の運勢とアドバイスをチェック！")

if st.button("占う！"):
    # 運勢とアドバイスをセットにする
    fortunes = [
        {"res": "超・大吉 🌟", "adv": "今日は無敵です！何か新しいことを始めてみては？"},
        {"res": "大吉 ✨", "adv": "最高の1日。身近な人に感謝を伝えるとさらに運気アップ！"},
        {"res": "中吉 ☀️", "adv": "安定した運気。ランチに好きなものを食べると吉です。"},
        {"res": "小吉 🍀", "adv": "小さな幸せが見つかる日。足元をよく見て歩こう。"},
        {"res": "末吉 🍃", "adv": "伸びしろあり！深呼吸をしてリラックスしましょう。"},
        {"res": "凶 ☔", "adv": "今日は早めに帰ってゆっくりお風呂に浸かりましょう。"}
    ]
    
    # ランダムに1つ選ぶ
    outcome = random.choice(fortunes)
    
    # 風船を飛ばす演出
    st.balloons()
    
    # 結果の表示
    st.divider() # 線を引く
    st.subheader(f"結果は... **{outcome['res']}** です！")
    st.info(f"💡 アドバイス: {outcome['adv']}") # 青い枠でアドバイスを表示
    st.divider()
