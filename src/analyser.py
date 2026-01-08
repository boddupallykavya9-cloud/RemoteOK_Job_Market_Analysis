import pandas as pd

def analyze_data(cleaned_data_path):
    df = pd.read_csv(cleaned_data_path)

    # Top job titles
    top_jobs = df['job_title'].value_counts().head(10)

    # Skill frequency comparison
    df['technical_skills'] = df['technical_skills'].str.split(',')
    skills_exploded = df.explode('technical_skills')
    skills_exploded['technical_skills'] = skills_exploded['technical_skills'].str.strip()

    top_skills = skills_exploded['technical_skills'].value_counts().head(10)

    print("\nTop Job Titles:\n", top_jobs)
    print("\nTop Skills:\n", top_skills)


if __name__ == "__main__":
    analyze_data("data/cleaned/remoteok_jobs_cleaned.csv")