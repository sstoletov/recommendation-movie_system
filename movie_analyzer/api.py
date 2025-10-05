import streamlit as st
import pandas as pd
from movie_analyzer.analyzer import MovieAnalyzer
from movie_analyzer.recommender import MovieRecommender
from movie_analyzer.visualizer import Visualizer

st.title("Movie Analyzer")

df = pd.read_csv("data/movies.csv")
analyzer = MovieAnalyzer(df)
recommender = MovieRecommender(df)

st.header("Top Rated Movies")
st.write(analyzer.top_rated(10))

st.header("Genre Distribution")
genre_counts = analyzer.genre_distribution()
Visualizer.plot_genre_distribution(genre_counts)

st.header("Movie Recommendations")
movie_input = st.text_input("Enter a movie title:")
if movie_input:
    st.write(recommender.recommend(movie_input))

