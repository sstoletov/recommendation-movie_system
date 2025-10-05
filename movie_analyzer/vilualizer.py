import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    @staticmethod
    def plot_genre_distribution(genre_counts):
        plt.figure(figsize=(10,5))
        sns.barplot(x=genre_counts.index, y=genre_counts.values)
        plt.xticks(rotation=45)
        plt.title("Genre Distribution")
        plt.show()

