import time
import streamlit as st
import base64

st.title("⏱️ เกมทาย Roblox จับเวลา")

# =========================
# เตรียมคำตอบ
# =========================
for i in range(1, 11):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""

# สถานะเกม
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

if "jumpscare" not in st.session_state:
    st.session_state.jumpscare = False


# =========================
# เริ่มเกมใหม่
# =========================
def reset_game():
    for i in range(1, 11):
        st.session_state[f"ans{i}_val"] = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False
    st.session_state.jumpscare = False


# =========================
# Jumpscare
# =========================
def jumpscare():
    with open("jumpscare.jpg", "rb") as f:
        image_data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .jumpscare {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: black;
            z-index: 999999;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .jumpscare img {{
            width: 100vw;
            height: 100vh;
            object-fit: contain;
        }}

        header {{
            visibility: hidden;
        }}
        </style>

        <div class="jumpscare">
            <img src="data:image/jpeg;base64,{image_data}">
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# สรุปคะแนน
# =========================
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(
    ans1, ans2, ans3, ans4, ans5,
    ans6, ans7, ans8, ans9, ans10
):

    correct_answers = [
        "blox fruits",
        "99 nights the forest",
        "doors",
        "3008",
        "strongest battle grounds",
        "blade ball",
        "natural disaster survival",
        "murder mystery",
        "bedwars",
        "anime defenders"
    ]

    user_answers = [
        ans1, ans2, ans3, ans4, ans5,
        ans6, ans7, ans8, ans9, ans10
    ]

    score = 0

    for user, correct in zip(user_answers, correct_answers):
        if user.strip().lower() == correct:
            score += 1

    st.write(f"🎯 คะแนนของคุณ: **{score}/10**")

    if score >= 9:
        st.success("☠️ Master (อยู่มานาน)")
    elif score >= 7:
        st.warning("😈 Pro (เซียน Roblox)")
    elif score >= 5:
        st.warning("🤡 Regular (ผู้เล่นทั่วไป)")
    else:
        st.error("💩 Noob (มือใหม่ฝึกเล่น)")


# =========================
# ปุ่มเริ่มเกม
# =========================
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# =========================
# คำถาม
# =========================
ans1 = st.text_input(
    "ข้อ 1: อยากเป็นราชาแห่งท้องทะเล ก็ต้องกินผลไม้ 🏴‍☠️",
    key="ans1_val"
)

ans2 = st.text_input(
    "ข้อ 2: อยู่ในป่าให้นานที่สุดและสู้กับสัตว์ประหลาดกวาง 🦌",
    key="ans2_val"
)

ans3 = st.text_input(
    "ข้อ 3: วิ่งเล่นชิวๆ ในโรงแรมผี 🚪",
    key="ans3_val"
)

ans4 = st.text_input(
    "ข้อ 4: ร้านเฟอร์นิเจอร์ที่พนักงานพร้อมต้อนรับคุณ 👽",
    key="ans4_val"
)

ans5 = st.text_input(
    "ข้อ 5: ไซตามะ และความแข็งแกร่ง 🥷",
    key="ans5_val"
)

ans6 = st.text_input(
    "ข้อ 6: ใช้ดาบตีลูกบอล 🗡️⚽",
    key="ans6_val"
)

ans7 = st.text_input(
    "ข้อ 7: หลบภัยธรรมชาติ 🏃‍♂️",
    key="ans7_val"
)

ans8 = st.text_input(
    "ข้อ 8: หนีฆาตกรและตำรวจต้องช่วยเรา 🔪🔫",
    key="ans8_val"
)

ans9 = st.text_input(
    "ข้อ 9: สงครามลอยฟ้าทำลายที่นอนศัตรู 🛌",
    key="ans9_val"
)

ans10 = st.text_input(
    "ข้อ 10: ป้องกันฐานทัพด้วยตัวละครอนิเมะ 🏰",
    key="ans10_val"
)


# =========================
# ระบบจับเวลา
# =========================
if (
    "start" in st.session_state
    and not st.session_state.get("is_ended", False)
    and not st.session_state.get("jumpscare", False)
):

    time_left = int(
        120 - (time.time() - st.session_state.start)
    )

    if time_left > 0:

        st.error(
            f"⏳ เหลือเวลา: {time_left} วินาที"
        )

    else:

        # เวลาหมด → Jumpscare
        st.session_state.jumpscare = True
        st.session_state.is_ended = False

        st.rerun()


# =========================
# ปุ่มส่งคำตอบ
# =========================
if (
    "start" in st.session_state
    and not st.session_state.get("is_ended", False)
    and not st.session_state.get("jumpscare", False)
):

    if st.button("📥 ส่งคำตอบ"):

        # กดส่งเองก่อนหมดเวลา
        st.session_state.is_ended = True

        st.rerun()

    # ทำให้เวลานับต่อ
    time.sleep(1)
    st.rerun()


# =========================
# แสดงผลลัพธ์
# =========================

# ถ้าเวลาหมด → แสดงผี
if st.session_state.get("jumpscare", False):

    jumpscare()

# ถ้ากดส่งคำตอบ → แสดงคะแนน
elif st.session_state.get("is_ended", False):

    show_result_dialog(
        ans1,
        ans2,
        ans3,
        ans4,
        ans5,
        ans6,
        ans7,
        ans8,
        ans9,
        ans10
    )


# =========================
# เครดิต
# =========================
st.divider()

st.write(
    "นายชรัญกร เรืองเวชชัย เลขที่ 2 ม.4/6"
)
