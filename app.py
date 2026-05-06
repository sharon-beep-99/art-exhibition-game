import streamlit as st

# 設定網頁標題與圖示
st.set_page_config(page_title="藝術知識大挑戰", page_icon="🎨")

# 1. 初始化遊戲狀態
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'score' not in st.session_state:
    st.session_state.score = 0

# 定義總關卡數
TOTAL_LEVELS = 5

# 側邊欄資訊
st.sidebar.title("🎨 策展人挑戰賽")
st.sidebar.write(f"目前進度：{st.session_state.level} / {TOTAL_LEVELS}")
st.sidebar.write(f"當前得分：{st.session_state.score}")

# 顯示進度條
progress_text = f"正在進行第 {st.session_state.level} 關"
st.progress(st.session_state.level / TOTAL_LEVELS)

# ---------------------------------------------------------
# 遊戲關卡邏輯
# ---------------------------------------------------------

# --- 第 1 關：藝術家辨識 ---
if st.session_state.level == 1:
    st.header("第一關：筆墨神韻")
    st.image("images/level1.jpg", caption="作品局部", use_container_width=True)
    st.write("觀察這幅畫作的筆觸，線條具有強烈的節奏感與草書意趣，這最可能是哪位畫家的風格？")
    
    ans = st.radio("選擇答案：", ["八大山人", "黃慎", "石濤", "王鐸"], index=None)
    
    if st.button("提交答案"):
        if ans == "八大山人":
            st.session_state.score += 20
            st.success("正確！這是八大山人典型的狂放寫意風格。")
        else:
            st.error("很遺憾，這題的正確答案是【八大山人】。")
        st.session_state.level += 1
        st.rerun()

# --- 第 2 關：作品異同比較 ---
elif st.session_state.level == 2:
    st.header("第二關：視覺偵探")
    st.write("請比較以下兩件作品，關於它們的敘述何者正確？")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/level2_a.jpg", caption="作品 A")
    with col2:
        st.image("images/level2_b.jpg", caption="作品 B")
        
    ans = st.radio("請選擇：", [
        "作品 A 使用了單點透視，作品 B 使用散點透視",
        "兩件作品的細節描繪完全相同",
        "作品 A 的墨色層次明顯比作品 B 豐富"
    ], index=None)
    
    if st.button("提交答案"):
        if "墨色層次" in ans: # 假設這是正確選項的關鍵字
            st.session_state.score += 20
            st.success("觀察入微！墨色層次的處理是兩者的核心差異。")
        else:
            st.error("再仔細看看，重點在於墨色層次的處理喔。")
        st.session_state.level += 1
        st.rerun()

# --- 第 3 關：基本資訊填充 ---
elif st.session_state.level == 3:
    st.header("第三關：歷史時空")
    st.image("images/level3.jpg", use_container_width=True)
    st.write("這件著名的青銅器文物，最初是在哪一個朝代被鑄造出來的？")
    
    ans = st.selectbox("請選擇朝代：", ["商代", "西周", "春秋", "戰國"], index=None)
    
    if st.button("提交答案"):
        if ans == "西周":
            st.session_state.score += 20
            st.success("沒錯！這展現了當時高超的鑄造技術。")
        else:
            st.error("答案應該是西周。")
        st.session_state.level += 1
        st.rerun()

# --- 第 4 關：材質與技法 ---
elif st.session_state.level == 4:
    st.header("第四關：細節之美")
    st.image("images/level4.jpg", caption="微距攝影局部", use_container_width=True)
    st.write("觀察畫面的「皴法」，這種像是由毛筆側面擦拭出來的質感，通常稱為什麼？")
    
    ans = st.radio("選擇答案：", ["披麻皴", "斧劈皴", "米點皴", "荷葉皴"], index=None)
    
    if st.button("提交答案"):
        if ans == "斧劈皴":
            st.session_state.score += 20
            st.success("正確！這種皴法常用於表現堅硬的山石質感。")
        else:
            st.error("這是典型的斧劈皴。")
        st.session_state.level += 1
        st.rerun()

# --- 第 5 關：策展與擺放 ---
elif st.session_state.level == 5:
    st.header("第五關：終極策展人")
    st.write("如果你要策劃一個關於「十七世紀跨文化交流」的展覽，下列哪一組作品最適合放在一起對比？")
    
    ans = st.radio("選擇組合：", [
        "黃檗僧畫像 與 日本黃檗畫派作品",
        "唐代金銀器 與 元代青花瓷",
        "北宋山水 與 現代抽象畫"
    ], index=None)
    
    if st.button("結算總分"):
        if "黃檗" in ans:
            st.session_state.score += 20
            st.success("專業的選擇！黃檗僧侶是十七世紀中日文化交流的重要載體。")
        else:
            st.error("考量到十七世紀的歷史脈絡，黃檗文化是更直接的切入點。")
        st.session_state.level += 1
        st.rerun()

# ---------------------------------------------------------
# 結算畫面
# ---------------------------------------------------------
elif st.session_state.level > TOTAL_LEVELS:
    st.balloons()
    st.header("🎊 挑戰完成！")
    st.write(f"你在這場藝術冒險中獲得了 **{st.session_state.score}** 分（總分 100）。")
    
    if st.session_state.score >= 80:
        st.success("太厲害了！你擁有專業策展人的水準！")
    elif st.session_state.score >= 60:
        st.info("很棒的表現，你對藝術品有很敏銳的觀察力。")
    else:
        st.warning("藝術的世界浩瀚無垠，繼續加油喔！")
    
    if st.button("重新開始挑戰"):
        st.session_state.level = 1
        st.session_state.score = 0
        st.rerun()