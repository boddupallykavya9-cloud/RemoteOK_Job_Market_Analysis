import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Handle missing values
    df.fillna("Unknown", inplace=True)

    # Clean skills column
    if 'technical_skills' in df.columns:
        df['technical_skills'] = df['technical_skills'].str.strip()

    # Save cleaned data
    df.to_csv(output_path, index=False)

    print("Data cleaning completed and saved.")


if __name__ == "__main__":
    clean_data(
        input_path="data/raw/remoteok_raw.csv",
        output_path="data/cleaned/remoteok_jobs_cleaned.csv"
    )