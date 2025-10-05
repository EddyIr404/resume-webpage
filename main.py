import streamlit as st

st.title("Eddy's Resume")
st.header("Personal Information")
st.write("Full Name: Muhammad Eddy Irvine Tan Daniel Tan")
st.write("Birth Date: 22 November")
st.write("Place of Birth: Sungai Petani, Kedah, Malaysia")

st.header("Contact Information")

st.markdown("""
| Type      | Details |
|-----------|---------|
| Email     | [eddyirvine02@gmail.com](mailto:eddyirvine02@gmail.com) |
| Phone     | (+60) 11-2059-2737 |
| LinkedIn  | [Eddy Irvine](https://www.linkedin.com/in/eddy-irvine-711960388) |
""")

st.header("Education")

# Create a DataFrame for the skills
skills_data = {
    "Degree": [
        "Bachelor Of Information Technology With Honour (Track In Artificial Intelligence)"
    ],
    "University": [
        "Universiti Malaysia Kelantan (City Campus)"
    ],
    "Batch Year": [
        "2022/2023"
    ]
}

skills_df = pd.DataFrame(skills_data)

# Display the table for Skill
st.table(skills_df)

st.header("Work Experience")
st.write("N/A")

st.header("Skills")

# Create a DataFrame for the skills
skills_data = {
    "Skill": [
        "Programming & Technical Skills",
        "Problem-Solving"
    ],
    "Description": [
        "Familiar with coding concepts and basic programming, with experience applying logic to practical tasks. Proficient in Python and Java.",
        "Skilled at analyzing challenges, identifying solutions, and applying logical strategies to achieve effective results."
    ]
}

skills_df = pd.DataFrame(skills_data)

# Display the table for Skill
st.table(skills_df)

st.header("Projects")

# Create a DataFrame for the projects
projects_data = {
    "Project": [
        "Smilevy",
        "Smart Traffic Light"
    ],
    "Description": [
        "A dental care management app for parents to manage special needs children's dental health. Developed as a group project.",
        "An electronic project using Arduino to simulate motion-based sensors for pedestrian crossing traffic lights. Developed as a group project."
    ],
    "When / Course": [
        "2024/2025 – Capstone / Digital Entrepreneurship",
        "2024 – Internet of Things Course"
    ]
}

projects_df = pd.DataFrame(projects_data)

# Display the table for Projects
st.table(projects_df)
