import streamlit as st
import random

# 1. ページの設定
st.set_page_config(page_title="画像付き！運勢占いデラックス", page_icon="🔮")

# --- サイドバーの設定 ---
st.sidebar.title("設定")
user_name = st.sidebar.text_input("あなたの名前", "ゲスト")

# --- メイン画面 ---
st.title("🔮 画像付き！運勢占いデラックス")
st.write(f"{user_name}さんの今日の運勢を画像付きで占います。")

if st.button("占う！"):
    # 運勢、アドバイス、画像URLをセットにする
    # ※画像はパブリックなフリー素材のURLを指定しています
    fortunes = [
        {
            "res": "超・大吉 🌟", 
            "adv": "今日は無敵です！何か新しいことを始めてみては？",
            "img": "https://images.unsplash.com/photo-1535295972055-1c762f4483e5?w=500" # お祝いの光
        },
        {
            "res": "大吉 ✨", 
            "adv": "最高の1日。身近な人に感謝を伝えるとさらに運気アップ！",
            "img": "https://images.unsplash.com/photo-1490730141103-6cac27aaab94?w=500" # 美しい空
        },
        {
            "res": "中吉 ☀️", 
            "adv": "安定した運気。ランチに好きなものを食べると吉です。",
            "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500" # 美味しそうな料理
        },
        {
            "res": "小吉 🍀", 
            "adv": "小さな幸せが見つかる日。足元をよく見て歩こう。",
            "img": "https://images.unsplash.com/photo-1528183429752-a97d0bf99b5a?w=500" # 四つ葉のクローバー
        },
        {
            "res": "凶 ☔", 
            "adv": "今日は早めに帰ってゆっくりお風呂に浸かりましょう。",
            "img": "https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?w=500" # 雨の窓
        }
    ]
    
    outcome = random.choice(fortunes)
    
    st.balloons()
    
    # --- 結果の表示 ---
    st.divider()
    st.subheader(f"{user_name}さんの結果は... {outcome['res']}")
    
    # 画像の表示（captionで説明を入れ、use_container_widthで横幅を合わせる）
    st.image(outcome['img'], caption=f"今日のイメージ：{outcome['res']}", use_container_width=True)
    
    st.info(f"💡 アドバイス: {outcome['adv']}")
    st.divider()
