import streamlit as st
import google.generativeai as genai

 # Configure Gemini
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_resume(resume_text, job_description):
     """Analyzes resume and job description using Gemini."""

     prompt = f"""
     You are an expert resume and ATS (Applicant Tracking System) analyst.  Your goal is to help candidates optimize their resumes to match job descriptions and pass through ATS systems.

     Here's the candidate's resume:
     ```
     {resume_text}
     ```

     Here's the job description:
     ```
     {job_description}
     ```

     Your tasks are as follows: 
     The output should include keyword identification, bullet point improvement, skills gap analysis, and a relevant score for the resume.
     **Instructions:** 
     1.**Keyword Identification:** - Analyze the provided resume and the associated job description.- Identify impactful keywords that are missing from the resume 
     but essential for passing ATS screenings.- 
     Create a separate section labeled "Missing Keywords" and categorize the keywords by relevance to the job role.
     2.**Bullet Point Improvement:** - Review each bullet point in the resume.- For each bullet point, 
     provide: - The original text.- An improved version that incorporates keywords from the job description.
     - Ensure that the improved bullet points emphasize achievements, metrics, and relevant skills.
     **For Each Company in Resume** - **Generate the bullet points which are essential to Job Description and needs to be in resume**
     3.**Skills Gap Analysis:** - Compare the skills listed in the resume against those required in the job description.- Present the missing skills in a structured format: - **Heading of Related Area** (e.g., Technical Skills, Soft Skills, etc.) - **Missing Skill** (specific skills that need to be added) 
     4.**Resume Scoring:** - Provide a relevant score for the resume based on its alignment with the job description and inclusion of keywords, bullet points, and required skills.
     **Output Format:** - Clearly label each section as follows: - Missing Keywords - Improved Bullet Points - Skills Gap Analysis - Resume Score 
     **End of Prompt**
     """

     try:
         response = model.generate_content(prompt)
         return response.text
     except Exception as e:
         return f"Error: {e}"

def main():
     st.title("ATS Resume Optimizer")

     resume_text = st.text_area("Paste your Resume Text", height=300)
     job_description = st.text_area("Paste the Job Description", height=300)

     if st.button("Analyze"):
         if resume_text and job_description:
             with st.spinner("Analyzing..."):
                 analysis_results = analyze_resume(resume_text, job_description)
                 st.subheader("Analysis Results:")
                 st.write(analysis_results)
         else:
             st.warning("Please enter both resume and job description.")

if __name__ == "__main__":
     main()
