import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="My Python Notes & Quiz",
    page_icon="🐍",
    layout="centered"
)

# 2. Sidebar Navigation
st.sidebar.title("📚 Navigation")
topic = st.sidebar.radio(
    "Go to:",
    ["Python Notes", "Take a 10-Question Quiz"]
)

# --- PANEL 1: NOTES ---
if topic == "Python Notes":
    st.title("🐍 Core Python Notes")
    st.write("Welcome to your learning dashboard! Select the quiz from the sidebar to test your skills.")
    st.markdown("""
    * **Tip 1:** Lists are mutable; tuples are immutable.
    * **Tip 2:** Use dictionary comprehensions for rapid key-value mapping.
    * **Tip 3:** Functions use `def` followed by the function name.
    """)

# --- PANEL 2: INTERACTIVE QUIZ ---
elif topic == "Take a 10-Question Quiz":
    st.title("🧠 10-Question Python Challenge")
    st.write("Test your basic-to-intermediate Python knowledge. Answer all questions below and submit!")

    # Define the 10 questions, options, and index of the correct answer
    quiz_data = [
        {"q": "1. What is the correct file extension for Python files?", "options": [".pt", ".py", ".pyt", ".pyw"], "answer": 1},
        {"q": "2. Which keyword is used to create a function in Python?", "options": ["function", "void", "def", "fun"], "answer": 2},
        {"q": "3. What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "5"], "answer": 1},
        {"q": "4. Which data structure is ordered, mutable, and allows duplicate members?", "options": ["List", "Tuple", "Set", "Dictionary"], "answer": 0},
        {"q": "5. How do you start a single-line comment in Python?", "options": ["//", "/*", "#", "<!--"], "answer": 2},
        {"q": "6. Which method removes any whitespace from both the beginning and the end of a string?", "options": ["strip()", "trim()", "ptrim()", "len()"], "answer": 0},
        {"q": "7. What does the len() function do?", "options": ["Converts to lowercase", "Finds data type", "Returns the number of items", "Generates random numbers"], "answer": 2},
        {"q": "8. Which of these is NOT a valid variable name?", "options": ["my_var", "myVar", "2myvar", "_myvar"], "answer": 2},
        {"q": "9. What is the correct way to import a module named 'math'?", "options": ["include math", "import math", "using math", "require math"], "answer": 1},
        {"q": "10. What is the output of print(bool(0))?", "options": ["True", "False", "None", "Error"], "answer": 1}
    ]

    # Initialize a form so components don't instantly trigger a refresh on every single click
    with st.form(key="quiz_form"):
        user_answers = []
        
        # Render each question dynamically
        for i, item in enumerate(quiz_data):
            st.markdown(f"##### {item['q']}")
            ans = st.radio(
                f"Choose one for Q{i+1}:", 
                options=item["options"], 
                index=None,         # Forces user to intentionally pick an answer
                key=f"q_{i}",
                label_visibility="collapsed"
            )
            user_answers.append(ans)
            st.divider()

        # Submit button inside the form
        submit_button = st.form_submit_button(label="Submit Answers")

    # Evaluate the results after submission
    if submit_button:
        score = 0
        unanswered = False
        
        # Calculate scores
        for i, item in enumerate(quiz_data):
            selected = user_answers[i]
            if selected is None:
                unanswered = True
            elif selected == item["options"][item["answer"]]:
                score += 1
        
        # Display feedback summary
        if unanswered:
            st.warning("⚠️ You missed some questions! Make sure to select an option for every question.")
        
        st.metric(label="Your Final Score", value=f"{score} / {len(quiz_data)}")
        
        if score == 10:
            st.balloons()
            st.success("🏆 Perfect score! Master status achieved!")
        elif score >= 7:
            st.success("🎉 Great job! You have a solid grasp of Python basics.")
        else:
            st.info("📚 A good attempt! Go back to the notes to brush up on a few concepts.")

st.divider()
st.caption("Created with ❤️ using Streamlit")
