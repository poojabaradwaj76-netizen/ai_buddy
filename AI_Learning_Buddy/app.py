# -*- coding: utf-8 -*-
import streamlit as st
import sys
import os

# Ensure the parent directory is in python path to import offline_helper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import offline_helper

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern design: rounded cards, soft shadows, blue accents, purple buttons
st.markdown("""
<style>
    /* Styling general backgrounds and fonts */
    .reportview-container {
        background-color: #ffffff;
    }
    
    /* Elegant Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Custom card styles */
    .edu-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    
    .edu-header {
        color: #1e3a8a;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .accent-card {
        background-color: #eff6ff;
        border-left: 5px solid #3b82f6;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    
    .quote-card {
        background-color: #faf5ff;
        border-left: 5px solid #a855f7;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        font-style: italic;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background-color: #3b82f6;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR CONFIGURATION
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color:#1e3a8a; text-align:center;'>🤖 AI Learning Buddy</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b;'>Your 24/7 Offline Study Partner</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # About Section
    st.markdown("### 📘 About")
    st.markdown("""
    **AI Learning Buddy** is a fully functional, offline educational dashboard.
    It helps students understand difficult concepts in plain English, provides clear metaphors, conducts interactive multiple-choice tests, and grades explanations with zero internet requirement.
    """)
    
    # Key Features
    st.markdown("### ✨ Features")
    st.markdown("""
    * 🔍 **Topic Explainer**: Simplified breakdowns.
    * 📖 **Real-Life Examples**: Intuitive mental models.
    * ✏️ **Interactive Quizzes**: Test knowledge with 5 custom MCQs.
    * 📈 **Answer Evaluator**: Smart rule-based grader with feedback.
    * 🎓 **Full Sessions**: Complete learning guides.
    """)
    
    # Responsible AI Section
    st.markdown("### ⚠️ Responsible AI")
    st.markdown("""
    <div style='background-color:#fffbeb; border:1px solid #fef3c7; border-radius:8px; padding:15px; font-size:0.9em; color:#78350f;'>
    <strong>Keep in mind:</strong><br>
    • AI can make mistakes.<br>
    • Verify important information.<br>
    • Use AI to support learning.<br>
    • Do not depend entirely on AI during exams.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<div style='text-align:center; font-size:0.85em; color:#94a3b8;'>Developed by Pooja ❤️</div>", unsafe_allow_html=True)


# ==========================================
# MAIN PAGE HEADER
# ==========================================
st.markdown("<h1 style='color:#1e3a8a; font-size: 2.8rem; margin-bottom: 5px;'>🤖 AI Learning Buddy</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.25rem; color: #475569;'>Learn anything with your personal AI tutor.</p>", unsafe_allow_html=True)
st.markdown("---")


# ==========================================
# TOPIC & ACTIVITY SELECTION
# ==========================================
col1, col2 = st.columns([2, 1])

with col1:
    topic_input = st.text_input(
        "📚 What topic would you like to learn today?",
        placeholder="Enter a topic (Example: Binary Search)",
        help="Type any computer science, science, or general academic topic!"
    )

with col2:
    activity_selection = st.selectbox(
        "🎯 Select learning activity:",
        options=[
            "Explain Topic",
            "Real-Life Example",
            "Generate Quiz",
            "Evaluate My Answer",
            "Full Learning Session"
        ]
    )

# Clean and normalize topic name
topic = topic_input.strip()

# ==========================================
# CORE APPLICATION LOGIC
# ==========================================
if not topic:
    # Warm default state when no topic is entered
    st.info("👋 Hello! Please enter a topic above to begin your offline learning journey.")
    
    # Display some common predefined topics to guide the user
    st.markdown("### 💡 Recommended Topics to Try:")
    predefined_cols = st.columns(4)
    topics_list = ["Binary Search", "Binary Tree", "DBMS", "Python", "Photosynthesis", "Machine Learning", "Sorting", "Stack"]
    for i, t in enumerate(topics_list):
        with predefined_cols[i % 4]:
            if st.button(t, key=f"btn_{t}", use_container_width=True):
                # Triggering re-render with selected topic
                st.query_params["topic"] = t
                st.rerun()
else:
    st.markdown(f"### Current Study Target: **{topic.title()}**")
    
    # ------------------------------------------
    # ACTIVITY 1: EXPLAIN TOPIC
    # ------------------------------------------
    if activity_selection == "Explain Topic":
        with st.spinner("Analyzing topic details..."):
            explanation_md = offline_helper.explain_topic(topic)
            
            st.markdown(f"""
            <div class='edu-card'>
                <h3 class='edu-header'>🔍 Simplified Breakdown</h3>
                {explanation_md}
            </div>
            """, unsafe_allow_html=True)
            
            st.success("🎉 Concept unpacked! Read through the core parameters to build your initial foundations.")

    # ------------------------------------------
    # ACTIVITY 2: REAL-LIFE EXAMPLE
    # ------------------------------------------
    elif activity_selection == "Real-Life Example":
        with st.spinner("Generating real-life analogies..."):
            example_md = offline_helper.real_life_example(topic)
            
            st.markdown(f"""
            <div class='edu-card'>
                <h3 class='edu-header'>📖 Real-Life Analogy</h3>
                {example_md}
            </div>
            """, unsafe_allow_html=True)
            
            st.info("💡 Pro-Tip: Visualizing abstract topics via physical models increases comprehension by over 70%!")

    # ------------------------------------------
    # ACTIVITY 3: GENERATE QUIZ
    # ------------------------------------------
    elif activity_selection == "Generate Quiz":
        with st.spinner("Drafting quiz questions..."):
            quiz_questions = offline_helper.generate_quiz(topic)
            
            st.markdown("<h3 style='color:#1e3a8a;'>✏️ Practice Quiz: 5 Multiple Choice Questions</h3>", unsafe_allow_html=True)
            st.write("Test your knowledge and receive instant offline feedback!")
            
            # Using Streamlit form to compile answers nicely
            with st.form(key=f"quiz_form_{topic.lower().replace(' ', '_')}"):
                user_answers = {}
                for idx, q in enumerate(quiz_questions):
                    st.markdown(f"**Q{idx+1}: {q['question']}**")
                    options_list = [f"{k}) {v}" for k, v in q['options'].items()]
                    selected_opt = st.radio(
                        "Choose your answer:",
                        options=options_list,
                        key=f"q_{idx}",
                        index=0
                    )
                    # Extract option letter (A, B, C, or D)
                    user_answers[idx] = selected_opt[0]
                    st.write("")
                
                submit_button = st.form_submit_button(label="Submit Quiz")
                
            if submit_button:
                score = 0
                st.markdown("### 📊 Quiz Results & Review")
                
                for idx, q in enumerate(quiz_questions):
                    u_ans = user_answers[idx]
                    correct_ans = q["correct_answer"]
                    is_correct = u_ans == correct_ans
                    
                    if is_correct:
                        score += 1
                        st.success(f"✅ **Question {idx+1}: Correct!** You selected {u_ans}.")
                    else:
                        st.error(f"❌ **Question {idx+1}: Incorrect.** You selected {u_ans}. The correct answer was **{correct_ans}**.")
                    
                    st.markdown(f"**Explanation:** {q['explanation']}")
                    st.markdown("---")
                
                final_percentage = (score / 5) * 100
                st.metric(label="Your Final Score", value=f"{score}/5 ({final_percentage}%)")
                
                if score == 5:
                    st.balloons()
                    st.success("🏆 Perfect Score! You've completely mastered this topic!")
                elif score >= 3:
                    st.success("👍 Good Job! You have a solid grasp. Review the incorrect questions to score 100% next time.")
                else:
                    st.warning("💪 Nice try! Go back to the 'Explain Topic' tab to review the core concepts, then try again!")

    # ------------------------------------------
    # ACTIVITY 4: EVALUATE MY ANSWER
    # ------------------------------------------
    elif activity_selection == "Evaluate My Answer":
        st.markdown("<h3 style='color:#1e3a8a;'>📈 Conceptual Evaluator</h3>", unsafe_allow_html=True)
        st.write("Write an explanation of the topic in your own words, and your offline tutor will assess your understanding, highlight missing parameters, and give you a score.")
        
        user_answer_text = st.text_area(
            "✍️ Write your description here:",
            height=180,
            placeholder=f"Example: Binary Search is a fast searching algorithm that works on sorted lists. It finds the middle element and halves the search space each time..."
        )
        
        evaluate_btn = st.button("Evaluate Explanation")
        
        if evaluate_btn:
            if not user_answer_text.strip():
                st.warning("⚠️ Please write an answer first before clicking evaluate!")
            else:
                with st.spinner("Reviewing your response structure..."):
                    eval_results = offline_helper.evaluate_answer(topic, user_answer_text)
                    
                    st.markdown("### 📊 Evaluation Report Card")
                    
                    # Score representation
                    score = eval_results["score"]
                    if score >= 80:
                        st.success(f"🌟 **Excellent Understanding! Score: {score}/100**")
                    elif score >= 60:
                        st.info(f"⚡ **Good Progress! Score: {score}/100**")
                    else:
                        st.warning(f"✍️ **Keep Practice! Score: {score}/100**")
                    
                    # Feedback cards
                    st.markdown(f"""
                    <div class='accent-card'>
                        <strong>💡 Primary Feedback:</strong><br>
                        {eval_results["feedback"]}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class='edu-card' style='border-left: 5px solid #ef4444;'>
                        <strong>🚨 Missed Parameters / Mistakes:</strong><br>
                        {eval_results["mistakes"]}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("**🛠️ Actionable Suggestions for Improvement:**")
                    for sug in eval_results["suggestions"]:
                        st.markdown(f"- {sug}")
                        
                    st.markdown(f"""
                    <div class='quote-card'>
                        {eval_results["encouragement"]}
                    </div>
                    """, unsafe_allow_html=True)

    # ------------------------------------------
    # ACTIVITY 5: FULL LEARNING SESSION
    # ------------------------------------------
    elif activity_selection == "Full Learning Session":
        with st.spinner("Assembling custom study session..."):
            session = offline_helper.full_learning_session(topic)
            
            # Step 1: Welcome & Intro
            st.markdown(session["introduction"])
            st.markdown("---")
            
            # Step 2: In-Depth Explanation
            st.markdown("### Step 1: Detailed Theoretical Explanation")
            st.markdown(session["explanation"])
            st.markdown("---")
            
            # Step 3: Real Life Analogy
            st.markdown("### Step 2: Conceptual Metaphor & Analogy")
            st.markdown(session["real_life_example"])
            st.markdown("---")
            
            # Step 4: MCQ Quiz (Inline review style)
            st.markdown("### Step 3: Self-Assessment Challenge")
            st.write("Think about your answers to these five core questions:")
            
            for idx, q in enumerate(session["quiz"]):
                with st.expander(f"Question {idx+1}: {q['question']}"):
                    for opt_letter, opt_text in q["options"].items():
                        st.write(f"**{opt_letter}** : {opt_text}")
                    st.markdown(f"<span style='color:#a855f7; font-weight:bold;'>Correct Answer: {q['correct_answer']}</span>", unsafe_allow_html=True)
                    st.write(f"**Reasoning**: {q['explanation']}")
            st.markdown("---")
            
            # Step 4: Summary & Motivation
            st.markdown("### Step 4: Study Guide Summary")
            st.markdown(session["summary"])
            
            st.markdown(f"""
            <div class='quote-card'>
                {session["motivational_message"]}
            </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
