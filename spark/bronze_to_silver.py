import pandas as pd
from langdetect import detect
import re

# read bronze layer
df = pd.read_json(
    "../data/bronze/all_articles.json"
)
print(df.columns)

print(df.head())

# remove duplicates
df.drop_duplicates(inplace=True)

# remove empty titles
df = df[df["title"].notna()]

# remove short content
df = df[df["content"].str.len() > 50]

# clean text
def clean_text(text):

    text = re.sub(r'\\n', ' ', str(text))

    text = re.sub(r'\\s+', ' ', text)

    return text.strip()

df["content"] = df["content"].apply(clean_text)

# detect language
def detect_language(text):

    try:
        return detect(str(text))

    except:
        return "unknown"

df["language"] = df["content"].apply(
    detect_language
)

# save silver layer
df.to_json(
    "../data/silver/articles_clean.json",
    orient="records",
    force_ascii=False,
    indent=4
)

print("\nSilver Layer Created Successfully")
print(df.head())