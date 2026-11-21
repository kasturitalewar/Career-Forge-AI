🚀 CareerForge 
AI Resume Analyzer & Career Guidance Platform:

CareerForge AI is an AI-powered resume analyzer and career guidance platform built using Python, Streamlit, and Google Gemini API. It analyzes a resume according to the user's target role and provides practical guidance for improving career readiness.

🔗 CAREERFORGE AI(https://kasturitalewar-career-forge-ai-app-spf2rq.streamlit.app/)

 ✨ Features
* Resume upload in PDF or DOCX format
* Target-role based resume analysis
* ATS score evaluation
* Resume summary and overview
* Current and missing skills
* Strengths and areas for improvement
* Skill-gap visualization using a pie chart
* Personalized career roadmap
* Recommended projects
* Interview preparation questions
* Downloadable PDF analysis report

 🛠️ Technologies Used
* Python
* Streamlit
* Google Gemini API
* PyPDF2
* python-docx
* Plotly
* ReportLab
* python-dotenv

 ⚙️ How It Works
1. Upload your resume.
2. Enter your target job role.
3. CareerForge extracts the resume text.
4. Google Gemini analyzes the resume according to the target role.
5. The application displays the ATS score, skills, gaps, strengths, roadmap, projects, and interview questions.
6. A complete analysis can be downloaded as a PDF report.

📁 Project Structure
```text
CareerForge AI/
├── app.py
├── ai.py
├── report.py
├── requirements.txt
├── .gitignore
└── README.md
```

🔑 API Key Setup

For local use, create a `.env` file:
```text
GEMINI_API_KEY=your_api_key
```
For the deployed Streamlit application, the Gemini API key is stored securely using Streamlit Secrets.

**Never upload your API key or `.env` file to GitHub.**
 ▶️ Run Locally

Install the required packages:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
streamlit run app.py
```

 🎯 Purpose
CareerForge AI is designed to help students and job seekers understand how their resume matches a target role and identify the skills, projects, and preparation needed to improve their career readiness.

Application look:
<img width="981" height="742" alt="image" src="https://github.com/user-attachments/assets/ff7b098c-aded-471b-bc3a-0a3b434f6349" />
<img width="962" height="745" alt="image" src="https://github.com/user-attachments/assets/29162d84-ea9b-4b1e-bd2e-c11dd838134a" />

 👩‍💻 Author
**Kasturi Talewar**


