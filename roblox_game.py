import time
import streamlit as st

st.title("⏱️ เกมทายRobloxจับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""
if "ans8_val" not in st.session_state:
    st.session_state.ans8_val = ""
if "ans9_val" not in st.session_state:
    st.session_state.ans9_val = ""
if "ans10_val" not in st.session_state:
    st.session_state.ans10_val = ""

# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog
    st.session_state.jumpscare = "" 


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
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
    
    # ตรวจข้อ 1
    if u_ans1 == "Blox Fruits":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "99 nights the forest":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ตรวจข้อ 3
    if u_ans3 == "doors":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 == "3008":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # ตรวจข้อ 5
    if u_ans5 == "storngest battle ground":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    # ตรวจข้อ 6
    if u_ans6 == "Blade Ball":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")

    # ตรวจข้อ 7
    if u_ans7 == "Natural Disaster Survival":
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")

    # ตรวจข้อ 8
    if u_ans8 == "Murder Mystery":
        st.success("✅ ข้อ 8: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 8: ยังไม่ถูกต้อง (คุณตอบ '{u_ans8}')")

    # ตรวจข้อ 9
    if u_ans9 == "BedWars":
        st.success("✅ ข้อ 9: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 9: ยังไม่ถูกต้อง (คุณตอบ '{u_ans9}')")

    # ตรวจข้อ 10
    if u_ans10 == "Anime Defenders":
        st.success("✅ ข้อ 10: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 10: ยังไม่ถูกต้อง (คุณตอบ '{u_ans10}')")
    
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 9  and score == 10:
        st.success("☠️ Master (อยู่มานาน)")
    elif score == 7 and score ==8:
        st.warning("😈 Pro (เซียนroblox)")
    elif score == 5 and score == 6:
        st.warning("🤡 Regular (ผู้เล่นทั่วไป)")
    else:
        st.error("💩 Noob (มือใหม่ฝึกเล่น)")

# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(120 - (time.time() - st.session_state.start))

       if time_left > 0:
    st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
else:
    st.session_state.is_ended = True
    st.session_state.jumpscare = True
    st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1:  อยากเป็นราชาแห่งท้องทะเล ก็ต้องกินผลไม้ 🏴‍☠️",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: อยู่ในป่าให้นานที่สุดเเละสู้กับสัตว์ประหลาดกวาง 🦌",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: วิ่งเล่นชิวๆในโรงแรมผี 🚪",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: ร้านฟอนิเจอร์ที่พนักงานพร้อมต้อนรับคุณ 👽 ",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: ไซตามะ และความแข็งแกร่ง 🥷",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6: ใช้ดาบตีลูกบอล 🗡️⚽️",
    value=st.session_state.ans6_val,
)
ans7 = st.text_input(
    "ข้อ 7: หลบภัยธรรมมะชาติ 🏃‍♂️",
    value=st.session_state.ans7_val,
)
ans8 = st.text_input(
    "ข้อ 8: หนีฆาตกรและะตำรวจต้องช่วยเรา 🔪🔫",
    value=st.session_state.ans8_val,
)           
ans9 = st.text_input(
    "ข้อ 9: สงครามลอยฟ้าทำลายที่นอนศัตรู 🛌",
    value=st.session_state.ans9_val,
)
ans10 = st.text_input(
    "ข้อ 10: ป้องกันฐานทัพด้วยตัวละครอนิเมะ 🏰",
    value=st.session_state.ans10_val,
)
# อัปเดตค่าล่าสุดเข้าตัวแปร
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

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Jumpscare ตอนหมดเวลา
if st.session_state.get("jumpscare", False):
    jumpscare()

# 6. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10)

st.divider()
st.write("นายชรัญกร เรืองเวชชัย เลขที่ 2 ม.4/6")
