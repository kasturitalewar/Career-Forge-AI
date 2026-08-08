import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(resume_text,role):
    prompt=f"""
Analyze this resume for the target role: {role}.

Return ONLY JSON with these keys:
ats_score,summary,current,missing,missing_info,strengths,weaknesses,roadmap,projects,interview,recommendation

ats_score: realistic score from 0 to 100.
current: relevant skills actually found.
missing: relevant skills needed for the target role.
missing_info: explain each missing skill with importance, learning and project.
strengths: positive points from the actual resume.
weaknesses: actual improvement areas.
roadmap: 4 practical steps.
projects: 3 suitable projects.
interview: 5 relevant questions.
recommendation: short final advice.

Important:
Analyze the resume specifically for the target role.
Do not recommend unrelated technologies.
Do not invent information.
Keep the analysis concise and practical.

Target Role:
{role}

Resume:
{resume_text}
"""

    try:
        response=client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        text=response.text.replace("```json","").replace("```","").strip()
        result=json.loads(text)
        result["role"]=role
        return result
    except Exception as e:
        return {"error":str(e)}