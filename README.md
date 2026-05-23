# Job Skill Trend Analyzer with Forecasting

A Data Science and analytics project that analyzes current job market trends using skill extraction, visualization, and simple machine learning forecasting.

## Project Overview

This project processes large-scale job market datasets to identify trending technical skills, visualize demand patterns, and predict future demand trends using Linear Regression.

The project includes:
- Data cleaning
- Skill extraction
- Trend analysis
- Forecasting
- Interactive Streamlit dashboard

---

## Features

- Analyze large job market datasets
- Extract technical skills from job descriptions
- Visualize top trending skills
- Forecast future skill demand
- Interactive dashboard with filters and search
- Download processed datasets

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Scikit-learn

---

## Project Structure

```text
job_skill_trend_analyzer/
│
├── analysis/
│   ├── skill_extraction.py
│   ├── trend_analysis.py
│   └── predict_trends.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── Jobs.csv
│   ├── cleaned_jobs.csv
│   ├── skill_counts.csv
│   └── historical_trends.csv
│
├── output/
│   ├── forecast.png
│   └── top_10_skills.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/gsrcode01/job-skill-trend-analyzer.git
```

Move into project folder:

```bash
cd job-skill-trend-analyzer
```

Create virtual environment:

### macOS/Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run skill extraction:

```bash
python analysis/skill_extraction.py
```

Run trend analysis:

```bash
python analysis/trend_analysis.py
```

Run forecasting:

```bash
python analysis/predict_trends.py
```

Launch dashboard:

```bash
python -m streamlit run dashboard/app.py
```

---

## Dashboard Features

- Top trending skills visualization
- Future demand forecasting
- Search functionality
- Dataset preview
- Download processed files

---

## Machine Learning Used

The project uses:
- Linear Regression

Purpose:
- Predict future demand for technical skills based on historical trend data.

---

## Future Improvements

- Real-time job scraping
- Multiple job platforms integration
- Advanced forecasting models
- NLP-based skill extraction
- Deployment on cloud platforms

---

## Author

Girdhar Singh Rajpurohit
