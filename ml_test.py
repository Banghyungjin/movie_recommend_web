import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df2 = pd.read_csv('./model/tmdb.csv', encoding='utf-8')
count = TfidfVectorizer(stop_words="english")
count_matrix = count.fit_transform(df2['soup'])
cos_sim = cosine_similarity(count_matrix, count_matrix)
print(cos_sim)