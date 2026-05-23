import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set dashboard layout and title
st.set_page_config(
    page_title="Job Skill Trend Analyzer",
    layout="wide"
)

# Check if processed files already exist
# If not, generate them automatically

if not os.path.exists("data/skill_counts.csv"):
    exec(open("analysis/skill_extraction.py").read())

if not os.path.exists("output/forecast.png"):
    exec(open("analysis/predict_trends.py").read())

# Load processed data
skill_df = pd.read_csv("data/skill_counts.csv")
cleaned_df = pd.read_csv("data/cleaned_jobs.csv")

# Dashboard title
st.title("Job Skill Trend Analyzer")

st.write(
    "This dashboard helps analyze trending skills in the current job market and predicts future demand trends."
)

st.markdown("---")

# Sidebar filters
st.sidebar.header("Filters")

top_n = st.sidebar.slider(
    "Select number of top skills",
    5,
    20,
    10
)

search_skill = st.sidebar.text_input(
    "Search for a skill"
)

# Basic project statistics
total_jobs = len(cleaned_df)
total_skills = len(skill_df)
top_skill = skill_df.iloc[0]["Skill"]

col1, col2, col3 = st.columns(3)

col1.metric("Total Jobs", total_jobs)
col2.metric("Total Skills", total_skills)
col3.metric("Most In-Demand Skill", top_skill)

st.markdown("---")

# Top skills visualization
st.subheader("Top Trending Skills")

top_df = skill_df.head(top_n)

fig, ax = plt.subplots(figsize=(12, 5))

ax.bar(top_df["Skill"], top_df["Count"])

plt.xticks(rotation=45)
plt.xlabel("Skills")
plt.ylabel("Demand Count")
plt.title("Top Skills Based on Job Listings")

st.pyplot(fig)

# Forecast section
st.markdown("---")

st.subheader("Skill Demand Forecast")

st.image("output/forecast.png")

# Skill search section
st.markdown("---")

st.subheader("Search Skills")

if search_skill:

    filtered_df = skill_df[
        skill_df["Skill"].str.contains(search_skill, case=False)
    ]

    st.dataframe(filtered_df)

# Display sample records
st.markdown("---")

st.subheader("Job Dataset Preview")

st.dataframe(cleaned_df.head(50))

# Download section
st.markdown("---")

st.subheader("Download Processed Files")

col4, col5 = st.columns(2)

with col4:
    with open("data/cleaned_jobs.csv", "rb") as file:
        st.download_button(
            label="Download Cleaned Dataset",
            data=file,
            file_name="cleaned_jobs.csv",
            mime="text/csv"
        )

with col5:
    with open("data/skill_counts.csv", "rb") as file:
        st.download_button(
            label="Download Skill Analysis",
            data=file,
            file_name="skill_counts.csv",
            mime="text/csv"
        )

# Footer
st.markdown("---")

st.write(
    "Developed using Python, Streamlit, Pandas, Matplotlib, and Scikit-learn."
)
