import requests
import pandas as pd

TMDB_API_KEY = "YOUR_API_KEY"

class MovieFetcher:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def fetch_movies(self, query: str, max_pages=1):
        movies = []
        for page in range(1, max_pages + 1):
            url = f"{self.base_url}/search/movie?api_key={self.api_key}&query={query}&page={page}"
            response = requests.get(url)
            data = response.json()
            movies.extend(data.get("results", []))
        return pd.DataFrame(movies)

if __name__ == "__main__":
    fetcher = MovieFetcher(TMDB_API_KEY)
    df = fetcher.fetch_movies("Matrix", max_pages=2)
    print(df.head())
    df.to_csv("data/matrix_movies.csv", index=False)

