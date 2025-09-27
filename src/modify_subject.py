import pandas as pd

# Reads an Excel file, modifies the 'Subject' column, and replaces 'news' with 'Dinesh'
def modify_subject_column(file_path):
    df = pd.read_csv("C:\Users\DELL\Downloads\Fake.csv")
    if 'Subject' in df.columns:
        df['Subject'] = df['Subject'].replace('news', 'Dinesh')
        print(df[['Subject']].head())
        # Optionally, save the modified file
        # df.to_excel('modified_'+file_path, index=False)
    else:
        print("Column 'Subject' not found.")

# Example usage:
# modify_subject_column('example.xlsx')
