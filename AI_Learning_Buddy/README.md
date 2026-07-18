# 🤖 AI Learning Buddy

An offline, responsive, and highly interactive educational tutor built using **Python** and **Streamlit**. It helps students master complex academic topics by explaining them in plain English, providing intuitive real-world metaphors, conducting custom 5-question multiple choice tests, and evaluating typed answers with a smart rule-based assessment engine.

---

## ✨ Features Included

1. **Explain Topic**: Get a clear, beginner-friendly breakdown of any topic (with custom-crafted curriculums for popular computer science topics like *Binary Search, Binary Tree, DBMS, Python, Photosynthesis, Machine Learning, Sorting, Stack, Queue, Operating System, and Computer Networks*).
2. **Real-Life Examples**: Grasp abstract systems via rich, real-world physical analogies.
3. **Interactive Quizzes**: Test active recall with interactive 5-question multiple choice quizzes with instant results, scores, and correct answer explanations.
4. **Conceptual Evaluator**: Type descriptions in your own words. The intelligent rule-based evaluator analyzes core terms, structure, and depth, returning a score out of 100, lists of mistakes, and actionable improvement recommendations.
5. **Full Learning Session**: A coordinated step-by-step masterclass covering foundations, metaphors, quizzes, review metrics, and motivational summaries.
6. **Responsible AI Panel**: A dedicated checklist in the sidebar advocating verification, ethical usage, and balanced studying.

---

## 🛠️ Project Structure

```text
AI_Learning_Buddy/
│
├── app.py                  # Main Streamlit UI dashboard and states
├── offline_helper.py       # Predefined databases, quiz banks, and evaluation logic
├── requirements.txt        # Package dependencies (Streamlit)
│
├── .streamlit/
│   └── config.toml         # Custom themes (Primary Blue, White canvas, Soft Grey rails)
```

---

## 🚀 How to Run Locally

### 1. Prerequisites
Make sure you have **Python 3.8+** installed on your machine.

### 2. Clone or Extract the Project
Open your terminal in the `AI_Learning_Buddy` folder.

### 3. Install Dependencies
Install the required packages using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
Launch the web interface locally using:
```bash
python -m streamlit run app.py
```
This will automatically open the application in your default web browser (usually at `http://localhost:8501` or `http://localhost:3000`).

---

## ☁️ Deploying to Streamlit Community Cloud

You can host this application online for free in under 5 minutes!

1. **Upload to GitHub**:
   - Create a new public repository on GitHub.
   - Push the contents of the `AI_Learning_Buddy/` directory directly to the root of your GitHub repository.

2. **Sign in to Streamlit**:
   - Go to [share.streamlit.io](https://share.streamlit.io) and log in with your GitHub account.

3. **Deploy the App**:
   - Click the **"New app"** button.
   - Select your Repository, Branch (`main`), and set the Main file path to `app.py`.
   - Click **"Deploy!"**

Streamlit will automatically detect `requirements.txt`, install Streamlit, configure your theme, and host your personalized 🤖 **AI Learning Buddy** live on the web!
