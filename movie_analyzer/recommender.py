from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class MovieRecommender:
    def __init__(self, df):
        self.df = df.fillna('')

    def recommend(self, movie_title, top_n=5):
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['overview'])
        idx = self.df[self.df['title'].str.contains(movie_title, case=False)].index[0]
        sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
        indices = sim.argsort()[-top_n-1:-1][::-1]
        return self.df.iloc[indices][['title', 'vote_average']]

