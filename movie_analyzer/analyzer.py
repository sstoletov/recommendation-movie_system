import pandas as pd

class MovieAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def top_rated(self, n=10):
        return self.df.sort_values("vote_average", ascending=False).head(n)

    def genre_distribution(self):
        genres = self.df["genre_ids"].dropna().apply(eval).explode()
        return genres.value_counts()

