import pandas as pd
from collections import Counter

df = pd.read_csv('netflix_titles_2021.csv')
genres = df['listed_in'].dropna().str.split(', ')
all_genres = Counter([genre for sublist in genres for genre in sublist])
top_genres = all_genres.most_common(10)

print("=== Top 10 Genres ===")
for genre, count in top_genres:
    print(f"{genre}: {count}")
