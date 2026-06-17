import streamlit as st

# 設定網頁標題與圖示
st.set_page_config(page_title="禹篆知識大挑戰", page_icon="👽️")

# 1. 核心設定：10道關卡的題庫
QUIZ_DATA = {
    1:  {"image": "images/level1.jpg",  "options": ["翼", "書", "皕", "竹"], "answer": "翼"},
    2:  {"image": "images/level2.jpg",  "options": ["件", "鳥", "仔", "得"], "answer": "仔"},
    3:  {"image": "images/level3.jpg",  "options": ["雙", "珪", "上", "船"], "answer": "船"},
    4:  {"image": "images/level4.jpg",  "options": ["蒸", "週", "川", "人"], "answer": "蒸"},
    5:  {"image": "images/level5.jpg",  "options": ["茶", "南", "泰", "世"], "answer": "南"},
    6:  {"image": "images/level6.jpg",  "options": ["衡", "小", "南", "期"], "answer": "衡"}, # 已修正選項，加入「衡」
    7:  {"image": "images/level7.jpg",  "options": ["今", "當", "至", "令"], "answer": "令"},
    8:  {"image": "images/level8.jpg",  "options": ["譔", "言", "評", "登"], "answer": "登"},
    9:  {"image": "images/level9.jpg",  "options": ["鳥", "島", "駕", "馬"], "answer": "島"},
    10: {"image": "images/level10.jpg", "options": ["目", "奄", "眠", "意"], "answer": "眠"}
}

TOTAL_LEVELS = len(QUIZ_DATA)

# 2. 初始化遊戲狀態
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'score' not in st.session_state:
    st.session_state.score = 0

# 3. 側邊欄資訊
st.sidebar.title("👽️ 禹篆挑戰賽")
display_level = min(st.session_state.level, TOTAL_LEVELS)
st.sidebar.write(f"目前進度：{display_level} / {TOTAL_LEVELS}")
st.sidebar.write(f"當前得分：{st.session_state.score}")

# 顯示進度條
if st.session_state.level <= TOTAL_LEVELS:
    st.progress(st.session_state.level / TOTAL_LEVELS)
else:
    st.progress(1.0)

# ---------------------------------------------------------
# 遊戲關卡邏輯
# ---------------------------------------------------------

if st.session_state.level <= TOTAL_LEVELS:
    current_num = st.session_state.level
    current_q = QUIZ_DATA[current_num]
    
    st.header(f"第 {current_num} 關")
    
    st.image(current_q["image"], caption="禹篆字形局部", use_container_width=True)
    st.write("觀察上述字形，這可能是以下哪個字？")
    
    ans = st.radio("選擇答案：", current_q["options"], index=None, key=f"q_{current_num}")
    
    btn_label = "結算總分" if current_num == TOTAL_LEVELS else "提交答案 & 下一關"
    
    if st.button(btn_label):
        if ans is None:
            st.warning("請先選擇一個答案再提交喔！")
        else:
            if ans == current_q["answer"]:
                st.session_state.score += 10
                st.success(f"太厲害了！答案確實是【{current_q['answer']}】！")
            else:
                st.error(f"可惜錯囉！正確答案是【{current_q['answer']}】。")
            
            st.session_state.level += 1
            st.rerun()

# ---------------------------------------------------------
# 結算畫面
# ---------------------------------------------------------
else:
    # 根據分數觸發不同特效
    if st.session_state.score >= 60:
        st.balloons() # 高分慶祝放氣球
    else:
        st.snow()     # 低分遺憾下雪（模擬下雨效果）
        
    st.header("🎊 挑戰完成！")
    st.write(f"你在這場禹篆探索冒險中獲得了 **{st.session_state.score}** 分（總分 100）。")
    
    if st.session_state.score >= 80:
        st.success("太神了！你簡直是古文字學大師，古人也甘拜下風！")
    elif st.session_state.score >= 60:
        st.info("很棒的表現！你對禹篆的神祕線條有很強的直覺與辨識力。")
    else:
        st.warning("禹篆字形神奇，能拿到這個分數已經不容易了，再接再厲！")
    
    if st.button("重新開始挑戰"):
        st.session_state.level = 1
        st.session_state.score = 0
        st.rerun()
