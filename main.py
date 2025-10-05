from movie_analyzer.data_fetcher import MovieFetcher
from movie_analyzer.data_cleaner import DataCleaner

fetcher = MovieFetcher("YOUR_API_KEY")
df = fetcher.fetch_movies("Matrix", max_pages=3)

cleaned_df = DataCleaner.clean(df)
cleaned_df.to_csv("data/movies.csv", index=False)

print("Data fetched and cleaned. Run `streamlit run movie_analyzer/app.py` to start the app.")

