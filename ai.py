
import os
import json
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def analyze_resume(resume_text, role):

    prompt = f"""
Analyze this resume for the target role: {role}.

Return ONLY JSON with these keys:
ats_score, summary, current, missing, missing_info,
strengths, weaknesses, roadmap, projects, interview,
recommendation

ats_score: realistic score from 0 to 100.
current: relevant skills actually found.
missing: relevant skills needed for the target role.
missing_info: explain each missing skill with importance,
learning and project.
strengths: positive points from the actual resume.
weaknesses: actual improvement areas.
roadmap: 4 practical steps.
projects: 3 suitable projects.
interview: 5 relevant questions.
recommendation: short final advice.

Do not recommend unrelated technologies.
Do not invent information.
Keep the analysis concise and practical.

Target Role:
{role}

Resume:
{resume_text}
"""

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            response_text = response.text

            response_text = response_text.replace(
                "```json", ""
            ).replace("```", "").strip()

            result = json.loads(response_text)

            result["role"] = role

            return result

        except Exception as e:

            if "503" in str(e) and attempt < 2:
                time.sleep(10)
                continue

            return {"error": str(e)}
