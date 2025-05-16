import pandas as pd

df = pd.read_csv('netflix_titles_2021.csv')
country_counts = df['country'].dropna().value_counts().head(10)
print("=== Top 10 Countries by Content Count ===")
print(country_counts)
