import pandas as pd
import re

SKILLS = [
    "python","java","c","c++","javascript","typescript",
    "react","angular","vue","next.js","node","express",
    "html","css","bootstrap","tailwind",
    "sql","mysql","postgres","mongodb",
    "aws","azure","gcp","docker","kubernetes","jenkins",
    "git","linux","terraform",
    "machine learning","deep learning","nlp","data science",
    "pandas","numpy","scikit-learn","tensorflow","pytorch",
    "flask","django","spring","spring boot",
    "langchain","llm","generative ai","power bi"
]

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9+.# ]", " ", text)
    return re.sub(r"\s+", " ", text)

def extract_skills(text):
    text = clean_text(text)

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))

def run_extraction():

    df = pd.read_csv("data/Jobs.csv")

    df["combined"] = (
        df["Title"].astype(str) + " " +
        df["Skills"].astype(str) + " " +
        df["Description"].astype(str)
    )

    df["Extracted_Skills"] = df["combined"].apply(extract_skills)

    all_skills = []

    for skills in df["Extracted_Skills"]:
        all_skills.extend(skills)

    skill_counts = pd.Series(all_skills).value_counts().reset_index()

    skill_counts.columns = ["Skill", "Count"]

    df.to_csv("data/cleaned_jobs.csv", index=False)

    skill_counts.to_csv("data/skill_counts.csv", index=False)

    print("extraction completed!")

run_extraction()