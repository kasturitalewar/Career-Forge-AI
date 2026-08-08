from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_report(result,filename):
    doc=SimpleDocTemplate(filename)
    styles=getSampleStyleSheet()
    content=[]
    content.append(Paragraph("CareerForge AI Report",styles["Title"]))
    content.append(Spacer(1,10))
    content.append(Paragraph(f"Target Role: {result['role']}",styles["Heading2"]))
    content.append(Paragraph(f"ATS Score: {result['ats_score']}%",styles["Heading2"]))
    content.append(Paragraph("Resume Summary",styles["Heading2"]))
    content.append(Paragraph(result["summary"],styles["BodyText"]))
    content.append(Paragraph("Current Skills",styles["Heading2"]))
    content.append(Paragraph(", ".join(result["current"]),styles["BodyText"]))
    content.append(Paragraph("Missing Skills",styles["Heading2"]))
    content.append(Paragraph(", ".join(result["missing"]),styles["BodyText"]))
    content.append(Paragraph("Strengths",styles["Heading2"]))
    for item in result["strengths"]:
        content.append(Paragraph("• "+item,styles["BodyText"]))
    content.append(Paragraph("Areas to Improve",styles["Heading2"]))
    for item in result["weaknesses"]:
        content.append(Paragraph("• "+item,styles["BodyText"]))
    content.append(Paragraph("Career Roadmap",styles["Heading2"]))
    for step in result["roadmap"]:
        content.append(Paragraph("• "+step,styles["BodyText"]))
    content.append(Paragraph("Recommended Projects",styles["Heading2"]))
    for project in result["projects"]:
        if isinstance(project,dict):
            content.append(Paragraph(project.get("name","Project"),styles["Heading3"]))
            content.append(Paragraph(project.get("description",""),styles["BodyText"]))
        else:
            content.append(Paragraph(str(project),styles["BodyText"]))
    content.append(Paragraph("Interview Preparation",styles["Heading2"]))
    for question in result["interview"]:
        content.append(Paragraph("• "+question,styles["BodyText"]))
    content.append(Paragraph("Final Recommendation",styles["Heading2"]))
    content.append(Paragraph(result["recommendation"],styles["BodyText"]))
    doc.build(content)