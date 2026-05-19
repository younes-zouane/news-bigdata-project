import streamlit as st
import pandas as pd

st.title("News Big Data Dashboard")

source_df = pd.read_csv("../data/gold/articles_per_source.csv")

language_df = pd.read_csv("../data/gold/articles_per_language.csv")

st.subheader("Articles Per Source")

st.bar_chart(
    source_df.set_index("source")
)

st.subheader("Articles Per Language")

st.bar_chart(
    language_df.set_index("language")
)