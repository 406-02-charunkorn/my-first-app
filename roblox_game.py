import time
import streamlit as st

st.title("⏱️ เกมทาย Roblox จับเวลา")


# ====================================================
# 1. กำหนดค่าเริ่มต้น
# ====================================================

for i in range(1, 11):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

if "jumpscare" not in st.session_state:
    st.session_state.jumpscare = False


# ====================================================
# 2. ฟังก์ชันเริ่มเกมใหม่
# ====================================================

def reset_game():
    for i in range(1, 11):
        st.session_state[f"ans{i}_val"] = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False
    st.session_state.jumpscare = False


# ====================================================
# 3. ฟังก์ชัน Jumpscare
# ====================================================

def jumpscare():
    st.image(
        "jumpscare.jpg",
        use_container_width=True
    )


# ====================================================
# 4. แสดงผลคะแนน
# ====================================================

@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(
    ans1, ans2, ans3, ans4, ans5,
    ans6, ans7, ans8, ans9, ans10
):

    st.balloons()

    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower()
    u_ans7 = ans7.strip().lower()
    u_ans8 = ans8.strip().lower()
    u_ans9 = ans9.strip().lower()
    u_ans10 = ans10.strip().lower()


    # ข้อ 1
    if u_ans1 == "blox fruits":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")


    # ข้อ 2
    if u_ans2 == "99 nights the forest":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")


    # ข้อ 3
    if u_ans3 == "doors":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")


    # ข้อ 4
    if u_ans4 == "3008":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")


    # ข้อ 5
    if u_ans5 == "strongest battle grounds":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")


    # ข้อ 6
    if u_ans6 == "blade ball":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")


    # ข้อ 7
    if u_ans7 == "natural disaster survival":
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")


    # ข้อ 8
    if u_ans8 == "murder mystery":
        st.success("✅ ข้อ 8: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 8: ยังไม่ถูกต้อง (คุณตอบ '{u_ans8}')")


    # ข้อ 9
    if u_ans9 == "bedwars":
        st.success("✅ ข้อ 9: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 9: ยังไม่ถูกต้อง (คุณตอบ '{u_ans9}')")


    # ข้อ 10
    if u_ans10 == "anime defenders":
        st.success("✅ ข้อ 10: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 10: ยังไม่ถูกต้อง (คุณตอบ '{u_ans10}')")


    # คะแนนรวม
    st.info(f"🏆 ได้คะแนนรวม: {score}/10 คะแนน")


    # ระดับผู้เล่น
    if score >= 9:
        st.success("☠️ Master (อยู่มานาน)")

    elif score >= 7:
        st.warning("😈 Pro (เซียน Roblox)")

    elif score >= 5:
        st.warning("🤡 Regular (ผู้เล่นทั่วไป)")

    else:
        st.error("💩 Noob (มือใหม่ฝึกเล่น)")


# ====================================================
# 5. ปุ่มเริ่มเกม
# ====================================================

st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ====================================================
# 6. ระบบจับเวลา
# ====================================================

if "start" in st.session_state and not st.session_state.get("is_ended", False):

    time_left = int(
        120 - (time.time() - st.session_state.start)
    )

    if time_left > 0:

        st.error(
            f"⏳ เหลือเวลา: {time_left} วินาที"
        )

    else:

        st.session_state.is_ended = True
        st.session_state.jumpscare = True

        st.rerun()


st.divider()


# ====================================================
# 7. ช่องตอบคำถาม
# ====================================================

ans1 = st.text_input(
    "ข้อ 1: อยากเป็นราชาแห่งท้องทะเล ก็ต้องกินผลไม้ 🏴‍☠️",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: อยู่ในป่าให้นานที่สุดและสู้กับสัตว์ประหลาดกวาง 🦌",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: วิ่งเล่นชิวๆ ในโรงแรมผี 🚪",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: ร้านเฟอร์นิเจอร์ที่พนักงานพร้อมต้อนรับคุณ 👽",
    value=st.session_state.ans4_val
)

ans5 = st.text_input(
    "ข้อ 5: ไซตามะ และความแข็งแกร่ง 🥷",
    value=st.session_state.ans5_val
)

ans6 = st.text_input(
    "ข้อ 6: ใช้ดาบตีลูกบอล 🗡️⚽",
    value=st.session_state.ans6_val
)

ans7 = st.text_input(
    "ข้อ 7: หลบภัยธรรมชาติ 🏃‍♂️",
    value=st.session_state.ans7_val
)

ans8 = st.text_input(
    "ข้อ 8: หนีฆาตกรและตำรวจต้องช่วยเรา 🔪🔫",
    value=st.session_state.ans8_val
)

ans9 = st.text_input(
    "ข้อ 9: สงครามลอยฟ้าทำลายที่นอนศัตรู 🛌",
    value=st.session_state.ans9_val
)

ans10 = st.text_input(
    "ข้อ 10: ป้องกันฐานทัพด้วยตัวละครอนิเมะ 🏰",
    value=st.session_state.ans10_val
)


# ====================================================
# 8. บันทึกคำตอบ
# ====================================================

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7
st.session_state.ans8_val = ans8
st.session_state.ans9_val = ans9
st.session_state.ans10_val = ans10


# ====================================================
# 9. ปุ่มส่งคำตอบ
# ====================================================

if "start" in st.session_state and not st.session_state.get("is_ended", False):

    if st.button("📥 ส่งคำตอบ"):

        st.session_state.is_ended = True

        st.rerun()

    time.sleep(1)
    st.rerun()


# ====================================================
# 10. Jumpscare เมื่อหมดเวลา
# ====================================================

if st.session_state.get("jumpscare", False):

    jumpscare()


# ====================================================
# 11. แสดงผลคะแนน
# ====================================================

if st.session_state.get("is_ended", False):

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


# ====================================================
# 12. ชื่อผู้จัดทำ
# ====================================================

st.divider()

st.write(
    "นายชรัญกร เรืองเวชชัย เลขที่ 2 ม.4/6"
)
