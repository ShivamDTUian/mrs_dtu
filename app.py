import streamlit as st 
import pickle 
import pandas as pd
import requests
import os

movie_dict_path = os.path.join('Moviw_recommendation_sys', 'movie_dict.pkl')
similarity_path = os.path.join('Moviw_recommendation_sys', 'similarity.pkl')

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f53ead6221d84221e10915757e84d727&language=en-US'.format(movie_id))
    data = response.json()
    print(data)  # Print the response to debug
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def fetch_movie_url(movie_id):
    return f"https://www.themoviedb.org/movie/{movie_id}"


def Recommend(movie):
    movie=movie.lower()
    try:
        movie_index = int(movies[movies['title'] == movie].index[0]) 
    except IndexError:
        print(f"Movie '{movie}' not found in the database.")
        return [], [], []   
    
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = [] 
    recommended_movies_poster = []
    recommended_movie_url = []
    
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append((movies.iloc[i[0]].title).upper())
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movie_url.append(fetch_movie_url(movie_id))
        
    return recommended_movies, recommended_movies_poster, recommended_movie_url  

movie_dict = pickle.load(open(movie_dict_path, 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))
movies = pd.DataFrame(movie_dict)

st.title('Movie Recommender System')

selected_movie_name  = st.selectbox(
"How would you like to be contacted?",movies['title'].values,)

st.write("You Selected:", (selected_movie_name).upper())

if st.button('Recommend'):
    names, posters, urls = Recommend(selected_movie_name)

    
    col1, col2, col3, col4, col5 = st.columns(5)  # Create 5 columns
    cols = [col1, col2, col3, col4, col5]
    
    for idx, col in enumerate(cols):
        if idx < len(names):
            with col:
                st.markdown(f"**{names[idx]}**")  # Display movie name
                st.markdown(f"[![Poster]({posters[idx]})]({urls[idx]})")  # Display poster with URL
    
    col6, col7, col8, col9, col10 = st.columns(5)
    cols = [col6, col7, col8, col9, col10]
    
    for idx, col in enumerate(cols, start=5):
        if idx < len(names):
            with col:
                st.markdown(f"**{names[idx]}**")  
                st.markdown(f"[![Poster]({posters[idx]})]({urls[idx]})")
