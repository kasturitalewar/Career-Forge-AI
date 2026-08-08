import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from ai import analyze_resume
from report import create_report
import plotly.express as px
import tempfile

st.set_page_config(page_title="CareerForge AI",page_icon="🚀",layout="wide")

st.title("🚀 CareerForge AI")
st.write("AI Resume Analyzer and Career Guidance Platform")
st.divider()

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader=PdfReader(file)
        text=""
        for page in reader.pages:
            text+=page.extract_text() or ""
        return text
    else:
        doc=Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

file=st.file_uploader("Upload Resume",type=["pdf","docx"])
role=st.text_input("Target Role",placeholder="Example: Python Developer")

if file and role:
    resume_text=extract_text(file)

    if st.button("Analyze Resume",use_container_width=True):

        with st.spinner("Gemini is analyzing your resume..."):
            result=analyze_resume(resume_text,role)

        if "error" in result:
            st.error(result["error"])
            st.stop()

        st.success("Analysis completed!")

        col1,col2,col3=st.columns(3)

        col1.metric("ATS Score",f"{result['ats_score']}%")
        col2.metric("Skills Found",len(result["current"]))
        col3.metric("Skill Gap",len(result["missing"]))

        st.progress(result["ats_score"]/100)
        st.divider()

        st.subheader("Resume Overview")
        st.write(result["summary"])

        tab1,tab2,tab3,tab4=st.tabs(
            ["Skills","Roadmap","Interview","Report"]
        )

        with tab1:

            st.subheader("Skill Analysis")

            data={
                "Type":["Current Skills","Missing Skills"],
                "Count":[
                    len(result["current"]),
                    len(result["missing"])
                ]
            }

            chart=px.pie(
                data,
                names="Type",
                values="Count",
                hole=0.4
            )

            st.plotly_chart(
                chart,
                use_container_width=True
            )

            st.subheader("Current Skills")

            st.write(
                ", ".join(result["current"])
            )

            st.subheader("Strengths")

            for item in result["strengths"]:
                st.success(item)

            st.subheader("Areas to Improve")

            for item in result["weaknesses"]:
                st.warning(item)

            st.subheader("Missing Skills")

            for item in result["missing_info"]:
                st.info(item)

            st.subheader("Recommended Projects")

            for project in result["projects"]:

                if isinstance(project,dict):

                    st.write(
                        "###",
                        project.get("name","Project")
                    )

                    st.write(
                        "Requirements:",
                        project.get("requirements","")
                    )

                    st.info(
                        project.get(
                            "description",
                            ""
                        )
                    )

                else:
                    st.write(project)

        with tab2:

            st.subheader("Career Roadmap")

            for step in result["roadmap"]:
                st.info(step)

            st.subheader("Recommendation")

            st.success(
                result["recommendation"]
            )

        with tab3:

            st.subheader("Interview Preparation")

            for question in result["interview"]:
                st.write("•",question)

        with tab4:

            st.subheader("CareerForge AI Report")

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as pdf:

                create_report(
                    result,
                    pdf.name
                )

                pdf_data=open(
                    pdf.name,
                    "rb"
                ).read()

            st.download_button(
                "Download PDF Report",
                pdf_data,
                "CareerForge_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

else:

    st.info(
        "Upload your resume and enter your target role to begin."
    )
    