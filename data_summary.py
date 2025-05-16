import pandas as pd

df = pd.read_csv('netflix_titles_2021.csv')

print("=== Dataset Summary ===")
print(df.info())
print("\n=== Missing Values ===")
print(df.isnull().sum())
print("\n=== Value Counts for 'type' ===")
print(df['type'].value_counts())
