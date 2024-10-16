import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {'User1': [5, 0, 3, 0, 0],
        'User2': [4, 0, 0, 2, 1],
        'User3': [0, 4, 0, 3, 3],
        'User4': [0, 0, 5, 0, 2],
        'User5': [1, 0, 0, 0, 0]}


df = pd.DataFrame(data, index=['Item1', 'Item2', 'Item3', 'Item4', 'Item5'])

print("User-Item Matrix:")
print(df)


similarity_matrix = cosine_similarity(df.T)
print("\n\n")
print(similarity_matrix)

user_similarity_df = pd.DataFrame(similarity_matrix, index=df.columns, columns=df.columns)

print("\nUser Similarity Matrix:")
print(user_similarity_df)



def recommend_items(user, df, similarity_matrix, top_n=2):
   
    user_idx = df.columns.get_loc(user)
    similar_users = similarity_matrix[user_idx]
    
    
    weighted_scores = np.dot(similar_users, df.T)
    
    
    scores = pd.Series(weighted_scores, index=df.index)
    
    
    already_rated = df[user] > 0
    scores = scores[~already_rated]
    
    
    return scores.sort_values(ascending=False).head(top_n)


recommended_items = recommend_items('User1', df, similarity_matrix)

print("\nRecommended Items for User1:")
print(recommended_items)
