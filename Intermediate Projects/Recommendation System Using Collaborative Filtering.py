import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('user_item_ratings.csv')
X = data.pivot(index='user_id', columns='item_id', values='rating').fillna(0)
user_similarity = cosine_similarity(X)
X_train, X_test = train_test_split(X, test_size=0.2)
predictions = user_similarity.dot(X_test) / np.array([np.abs(user_similarity).sum(axis=1)]).T
