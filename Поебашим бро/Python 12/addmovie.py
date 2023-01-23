import pandas as pd

movies_df = pd.read_csv(r'Z:\Data sciense\DS\Поебашим бро\Python 12\data\movies.csv')

rat1_df = pd.read_csv(r'Z:\Data sciense\DS\Поебашим бро\Python 12\data\ratings1.csv')
rat2_df = pd.read_csv(r'Z:\Data sciense\DS\Поебашим бро\Python 12\data\ratings2.csv')

ratings = pd.concat(
    [rat1_df, rat2_df],
    ignore_index=True
)
ratings = ratings.drop_duplicates(ignore_index=True)

def full_movie_list(mov_id):
    for index,movie_id in enumerate(movies_df['movieId']):
        if mov_id == movie_id:
            return movies_df.iloc[index, 1:]
    
movies_df_full = ratings['movieId'].apply(full_movie_list)
print(movies_df_full)
movies_df_full.info()
