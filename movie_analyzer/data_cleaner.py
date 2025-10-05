import pandas as pd

class DataCleaner:
    @staticmethod
    def clean(df: pd.DataFrame):
        df = df.drop_duplicates(subset='id')
        df = df.fillna({'vote_average': 0, 'vote_count': 0})
        return df

