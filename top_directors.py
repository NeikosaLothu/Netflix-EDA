import pandas as pd

df = pd.read_csv('netflix_titles_2021.csv')
top_directors = df['director'].dropna().value_counts().head(10)
print("=== Top 10 Directors ===")
print(top_directors)
