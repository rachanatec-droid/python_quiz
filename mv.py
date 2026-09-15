import time
import streamlit as st

# Set up the page title and emoji
st.set_page_config(page_title="Good Morning! ☀️", page_icon="💖", layout="centered")

# Custom styling for a romantic, fun look
st.markdown(
    """
    <style>
    .big-title {
        font-size: 2.5rem;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
    }
    .sub-title {
        font-size: 1.3rem;
        text-align: center;
        color: #4f4f4f;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.markdown(
    '<p class="big-title">Good Morning, Handsome! ☀️</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-title">System check: Did you sleep well, or were you busy dreaming about me?</p>',
    unsafe_allow_html=True,
)

st.write("---")

# Session state to handle the playful "No" button dodge or responses
if "love_clicked" not in st.session_state:
    st.session_state.love_clicked = False

# The Big Question
st.markdown("### 💌 Quick Daily Questionnaire")
question = st.radio(
    "Be honest... do you love me?", ["Select an option...", "Yes, absolutely! 🥰", "Only a little bit 🤏", "Not telling 🤐"]
)

if question == "Yes, absolutely! 🥰":
    st.balloons()
    st.success(
        "Yay! Correct answer! 🎉 You've won infinite virtual hugs and kisses. Claim them later in person!"
    )
elif question == "Only a little bit 🤏":
    st.warning("Only a little bit?! Excuse me, I need to recalibrate this app. 😤")
elif question == "Not telling 🤐":
    st.error("Suspicious silence detected! Try again before I confiscate your coffee. ☕")

st.write("---")

# Bonus playful button
if st.button("Click for a secret morning message 💝"):
    with st.spinner("Decrypting maximum affection..."):
        time.sleep(1.5)
    st.info(
        "Reminder: You are stuck with me today, tomorrow, and until the coffee runs out. Have an amazing day, babe! ✨"
    )
