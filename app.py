import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b4096d76f8a167a3c9f5071e97fc4c46&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_ind = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_ind]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies =[]
    recommend_movies_poster =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster


similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

def main():
    st.title('Movie Recommendation System')
    select_movie_name = st.selectbox(
        'Search for similar movies',
        movies['title'].values)

    if st.button('Recommend'):
        name,poster = recommend(select_movie_name)
        col1, col2, col3, col4, col5 = st.columns(
            5)

        with col1:
            st.text(name[0])
            st.image(poster[0])

        with col2:
            st.text(name[1])
            st.image(poster[1])

        with col3:
            st.text(name[2])
            st.image(poster[2])

        with col4:
            st.text(name[3])
            st.image(poster[3])

        with col5:
            st.text(name[4])
            st.image(poster[4])

if __name__ == '__main__':
    main()





