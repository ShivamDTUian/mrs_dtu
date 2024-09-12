import streamlit as st 
import pickle 
import pandas as pd
import requests

def fetch_poster(movie_id):
    
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f53ead6221d84221e10915757e84d727&language=en-US'.format(movie_id))
    data = response.json()
    
    return "https://image.tmdb.org/t/p/w500" +  data['poster_path']

def fetch_movie_url(movie_id):
    return f"https://www.themoviedb.org/movie/{movie_id}"




def Recommend(movie):
    movie=movie.lower()
    try:
        movie_index = int(movies[movies['title'] == movie].index[0]) 
    except IndexError:
        print(f"Movie '{movie}' not found in the database.")
        return 
    
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = [] 
    recommended_movies_poster = []
    recommended_movie_url = []
    
    
    for i in movie_list :
        movie_id = movies.iloc[i[0]].movie_id   # here we want to fetch posters using movie id from API  
        recommended_movies.append((movies.iloc[i[0]].title).upper())
        #fetching poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
        
        recommended_movie_url.append(fetch_movie_url)
        
    return recommended_movies, recommended_movies_poster, recommended_movie_url   # Also return posters


movie_dict = pickle.load(open('.vscode\movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('.vscode\similarity.pkl','rb'))

st.title('Movie Recommender System ')

selected_movie_name  = st.selectbox(
"How would you like to be contacted?",
movies['title'].values,)

st.write("You Selected:", (selected_movie_name).upper())

if st.button('Recommend'):
    name, poster, url = Recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)  # Create 5 columns
    
    with col1:
         st.markdown(f"[![{name[0]}]({poster[0]})]({url[0]})")

    with col2:
        st.markdown(f"[![{name[1]}]({poster[1]})]({url[1]})")
        
    with col3:
        st.markdown(f"[![{name[2]}]({poster[2]})]({url[2]})")
        
    with col4:
        st.markdown(f"[![{name[3]}]({poster[3]})]({url[3]})")

    with col5:
       st.markdown(f"[![{name[4]}]({poster[4]})]({url[4]})")
        
    col6, col7, col8, col9, col10 = st.columns(5)  #Create 5 columns
    
    with col6:
            st.markdown(f"[![{name[5]}]({poster[5]})]({url[5]})")
        
    with col7:
       st.markdown(f"[![{name[6]}]({poster[6]})]({url[6]})")
    with col8:
        st.markdown(f"[![{name[7]}]({poster[7]})]({url[7]})")
        
    with col9:
        st.markdown(f"[![{name[8]}]({poster[8]})]({url[8]})")
    with col10:
        st.markdown(f"[![{name[9]}]({poster[9]})]({url[9]})")