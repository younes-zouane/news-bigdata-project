import pandas as pd

df = pd.read_json("../data/silver/articles_clean.json")

# articles per source
source_stats = df.groupby("source").size().reset_index(name="total_articles")

# articles per language
language_stats = df.groupby("language").size().reset_index(name="count")

# save
source_stats.to_csv("../data/gold/articles_per_source.csv", index=False)

language_stats.to_csv("../data/gold/articles_per_language.csv", index=False)

print("Gold analytics created")