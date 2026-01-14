import streamlit as st
import random

# 1. ページの設定（サイドバーをデフォルトで開く設定なども可能）
st.set_page_config(page_title="運勢占いデラックス", page_icon="🔮", layout="centered")

# --- サイドバーの設定 ---
st.sidebar.title("設定・メニュー")
user_name = st.sidebar.text_input("あなたの名前を教えてね", "ゲスト")
effect_option = st.sidebar.selectbox("演出を選んでね", ["風船（デフォルト）", "雪を降らせる", "どちらも！"])

st.sidebar.divider()
st.sidebar.write(f"こんにちは、{user_name}さん！")
st.sidebar.caption("このアプリはPythonとStreamlitで作られています。")

# --- メイン画面 ---
st.title("🔮 運勢占いデラックス")
st.write(f"{user_name}さんの今日の運勢とアドバイスをチェック！")

if st.button("占う！"):
    fortunes = [
        {"res": "超・大吉 🌟", "adv": "今日は無敵です！何か新しいことを始めてみては？"},
        {"res": "大吉 ✨", "adv": "最高の1日。身近な人に感謝を伝えるとさらに運気アップ！"},
        {"res": "中吉 ☀️", "adv": "安定した運気。ランチに好きなものを食べると吉です。"},
        {"res": "小吉 🍀", "adv": "小さな幸せが見つかる日。足元をよく見て歩こう。"},
        {"res": "末吉 🍃", "adv": "伸びしろあり！深呼吸をしてリラックスしましょう。"},
        {"res": "凶 ☔", "adv": "今日は早めに帰ってゆっくりお風呂に浸かりましょう。"}
    ]
    
    outcome = random.choice(fortunes)
    
    # 2. 演出の切り替え
    if effect_option == "風船（デフォルト）":
        st.balloons()
    elif effect_option == "雪を降らせる":
        st.snow()
    else:
        st.balloons()
        st.snow()
    
    # 3. 結果の表示
    st.divider()
    st.subheader(f"{user_name}さんの結果は... **{outcome['res']}** です！")
    st.info(f"💡 アドバイス: {outcome['adv']}")
    st.divider()
