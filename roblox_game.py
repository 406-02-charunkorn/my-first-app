import time
import streamlit as st
import base64

st.title("⏱️ เกมทาย Roblox จับเวลา")


# =========================
# ตั้งค่าเริ่มต้น
# =========================
for i in range(1, 11):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""

if "game_started" not in st.session_state:
    st.session_state.game_started = False

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
    st.session_state.game_started = True
    st.session_state.is_ended = False
    st.session_state.jumpscare = False


# =========================
# แสดง Jumpscare
# =========================
def show_jumpscare():

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
def show_result_dialog():

    correct_answers = [
        "blox fruits",
        "steal an egg",
        "doors",
        "3008",
        "it girl",
        "blade ball",
        "rivals",
        "murder mystery",
        "bedwars",
        "grow a garden"
    ]

    user_answers = [
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val,
        st.session_state.ans5_val,
        st.session_state.ans6_val,
        st.session_state.ans7_val,
        st.session_state.ans8_val,
        st.session_state.ans9_val,
        st.session_state.ans10_val
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


# ==================================================
# JUMPSCARE
# ==================================================
if st.session_state.jumpscare:

    show_jumpscare()

    # แสดงผี 1.5 วินาที
    time.sleep(1.5)

    # ปิด Jumpscare
    st.session_state.jumpscare = False
    st.session_state.game_started = False
    st.session_state.is_ended = False

    # ลบเวลาเก่า
    if "start" in st.session_state:
        del st.session_state.start

    # กลับหน้าเริ่มเกม
    st.rerun()


# ==================================================
# สรุปคะแนน
# ==================================================
elif st.session_state.is_ended:

    show_result_dialog()

    st.write("")

    if st.button("🔄 เล่นใหม่", use_container_width=True):
        reset_game()
        st.rerun()


# ==================================================
# หน้าเริ่มเกม
# ==================================================
elif not st.session_state.game_started:

    st.write("กดปุ่มด้านล่างเพื่อเริ่มเกม")

    if st.button("🎮 เริ่มเล่นเกม", use_container_width=True):
        reset_game()
        st.rerun()


# ==================================================
# เกมกำลังเล่น
# ==================================================
else:

    # =========================
    # คำถาม
    # =========================

    st.text_input(
        "ข้อ 1: อยากเป็นราชาแห่งท้องทะเล ก็ต้องกินผลไม้ 🏴‍☠️",
        key="ans1_val"
    )

    st.text_input(
        "ข้อ 2: ขโมยไข่ของสัตว์แต่ละชนิดและวิ่งให้ไวที่สุด 🪺",
        key="ans2_val"
    )

    st.text_input(
        "ข้อ 3: วิ่งเล่นชิวๆ ในโรงแรมผี 🚪",
        key="ans3_val"
    )

    st.text_input(
        "ข้อ 4: ร้านเฟอร์นิเจอร์ที่พนักงานพร้อมต้อนรับคุณ 👽",
        key="ans4_val"
    )

    st.text_input(
        "ข้อ 5: เดินแฟชั่นโชว์ตามที่คุณแต่งตัว 💅🏿",
        key="ans5_val"
    )

    st.text_input(
        "ข้อ 6: ใช้ดาบตีลูกบอล 🗡️⚽",
        key="ans6_val"
    )

    st.text_input(
        "ข้อ 7: เกมยิงปืนมุมมองบุคคลที่ 1 (ยุคบุกเบิก) 🔫",
        key="ans7_val"
    )

    st.text_input(
        "ข้อ 8: หนีฆาตกรและตำรวจต้องช่วยเรา 🔪🔫",
        key="ans8_val"
    )

    st.text_input(
        "ข้อ 9: สงครามลอยฟ้าทำลายที่นอนศัตรู 🛌",
        key="ans9_val"
    )

    st.text_input(
        "ข้อ 10: ปลูกพืชและมีสัตว์เลี้ยง (ยุคบุกเบิก) 🌻",
        key="ans10_val"
    )


    # =========================
    # จับเวลา 120 วินาที
    # =========================

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
        st.session_state.game_started = False
        st.session_state.is_ended = False

        st.rerun()


    # =========================
    # ส่งคำตอบ
    # =========================

    if st.button(
        "📥 ส่งคำตอบ",
        use_container_width=True
    ):

        st.session_state.is_ended = True
        st.session_state.game_started = False

        st.rerun()


    # =========================
    # อัปเดตเวลา
    # =========================

    time.sleep(1)
    st.rerun()


# =========================
# เครดิต
# =========================
st.divider()

st.write(
    "นายชรัญกร เรืองเวชชัย เลขที่ 2 ม.4/6"
)
st.write(
    "นายรวิภัทร ฤทธิศร เลขที่ 6 ม.4/6"
)
st.write(
    "นายจารุภัทร อรุณสิทธิ์ เลขที่ 9 ม.4/6"
)
st.write(
    "นายนนทนัต อรัญญวนานนท์ เลขที่ 12 ม.4/6"
)
