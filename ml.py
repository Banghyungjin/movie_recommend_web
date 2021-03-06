from numpy.core.numeric import indices
from numpy.core.records import record
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df2 = pd.read_csv('./model/tmdb.csv', encoding='utf-8')
df2 = df2.reset_index()
# indices = pd.Series(df2.index, index = df2['title'])

class RECOMMEND():
    def __init__(self, vectorizer):     # 선언시 어떤 vectorizer를 사용할 것인지 선택
        self.vectorizer = vectorizer
    
    def get_recommendation(self, title):    # 실행시 title과 연관된 영화를 추천
        count = self.vectorizer(stop_words="english")
        count_matrix = count.fit_transform(df2['soup'])
        cos_sim = cosine_similarity(count_matrix, count_matrix)
        indices = pd.Series(df2.index, index = df2['title'])

        idx= indices[title]
        sim_scores = list(enumerate(cos_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)
        sim_scores = sim_scores[1:11]

        sim_indices = [i[0] for i in sim_scores]
        title = df2['title'].iloc[sim_indices]
        release_date = df2['release_date'].iloc[sim_indices]

        return_df = pd.DataFrame(columns=['Title', 'Date'])
        return_df['Title'] = title
        return_df['Date'] = release_date

        # print(return_df)
        return return_df

recommend = RECOMMEND(TfidfVectorizer)
df = recommend.get_recommendation("Spectre")

print(df)