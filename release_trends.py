import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles_2021.csv')
release_trend = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
release_trend.plot(kind='bar')
plt.title("Content Release Trend Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.tight_layout()
plt.savefig("release_trend.png")
plt.show()
