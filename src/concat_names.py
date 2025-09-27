import pandas as pd

# Reads an Excel file and concatenates first and last names
# Assumes columns are named 'First Name' and 'Last Name'
def read_and_concatenate_names("C:\Users\DELL\Downloads\Fake.csv"):
    df = pd.read_excel("C:\Users\DELL\Downloads\Fake.csv")
    if 'First Name' in df.columns and 'Last Name' in df.columns:
        df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
        print(df[['First Name', 'Last Name', 'Full Name']].head())
    else:
        print("Required columns 'First Name' and 'Last Name' not found.")

# Example usage:
# read_and_concatenate_names('example.xlsx')
