import streamlit as st
import pickle as pkl
import pandas as pd




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies_dict = pkl.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pkl.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender')


#creating a textbox for user

selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend  movies'):
    recommendations = recommend(selected_movie_name)  # Ignore posters, use only names

    # Create dynamic columns based on the number of recommendations
    cols = st.columns(len(recommendations))

    # Iterate through recommendations and display each name in a separate column
    for i, col in enumerate(cols):
        with col:
            st.text(recommendations[i])  # Display the movie name


