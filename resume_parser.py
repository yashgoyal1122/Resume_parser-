import json
import re

def parse_resume(resume_text):
    resume_dict = {
        "personal_info": {
            "name": "",
            "contact": {
                "email": "",
                "phone": "",
                "address": ""
            },
            "linkedin": "",
            "website": ""
        },
        "summary": "",
        "experience": [],
        "education": [],
        "skills": [],
        "certifications": [],
        "projects": []
    }

    # Example parsing logic (to be replaced with actual parsing logic)
    lines = resume_text.split('\n')
    for line in lines:
        if "Email:" in line:
            resume_dict["personal_info"]["contact"]["email"] = line.split(':')[1].strip()
        # More parsing logic here...

    return json.dumps(resume_dict, indent=2)

# Example resume text
resume_text = """
Name: John Doe
Email: john.doe@example.com
Phone: +1234567890
Address: 123 Main St, Anytown, USA
LinkedIn: linkedin.com/in/johndoe
Website: johndoe.com

Summary: Experienced software engineer with expertise in AI and ML...

Experience:
Job Title: Senior Software Engineer
Company: Tech Corp
Location: New York, NY
Start Date: Jan 2020
End Date: Present
Responsibilities: Developed AI solutions...

Education:
Degree: B.Sc. in Computer Science
Institution: ABC University
Location: City, State
Graduation Year: 2018

Skills: Python, Java, AI, ML, NLP...

Certifications: AWS Certified Solutions Architect...

Projects:
Project Name: AI Chatbot
Description: Developed a chatbot using NLP techniques...
"""

# Parse the resume
parsed_resume = parse_resume(resume_text)
print(parsed_resume)
