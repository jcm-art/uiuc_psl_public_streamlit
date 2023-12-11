# PSL Streamlit App Page

import json
import os
import pathlib
import requests

import numpy as np
import pandas as pd
import streamlit as st

class MovieRecommendationPageII():

    def __init__(self):
        self.movie_recommender = MovieRecommenderII()

    def write(self):
        st.title("Movie Recommender (PSL Project 4)")
        st.write("Authors: Justin Martin and Dillon Harding")
        st.header("System II: Movie Recommendations based on User Preferences")
        
        # Get User ratings
        st.subheader("Rate the following movies to get a recommendation; movies rated 0 will be ignored.")

        # Get Top Movies for Rating
        top_movies_df = self._get_top_movie_df()

        self.movie_list = top_movies_df.head(20)["title"].tolist()
        self.movie_ids = top_movies_df.head(20)["movie_id"].tolist()

        self.user_ratings = []
        self.not_seen = []

        # Make grid of movies for ratings
        self.make_movie_grid(self.movie_list)

        print(self.user_ratings)
        print(self.not_seen)
        st.subheader(f"Top 10 Movies Recommended for you")
        for i, movie_title in enumerate(self.movie_recommender.get_system_II_recommendation_list(self.movie_ids, self.user_ratings)):
            st.write(f"{i+1}) {movie_title}")

    def _get_top_movie_df(self):
        # URL of the CSV file
        csv_url = "https://raw.githubusercontent.com/jcm-art/uiuc_psl_public_streamlit/main/src/resources/top_100_most_reviewed_movies.csv"

        # Load the CSV file into a DataFrame
        top_100_movies_df = pd.read_csv(csv_url)
        return top_100_movies_df

    def make_movie_grid(self, movie_list):

        # Define the number of columns in the grid
        num_columns = 5

        # Calculate the number of rows based on the number of movies and columns
        num_rows = len(movie_list) // num_columns + (len(movie_list) % num_columns > 0)

        # Create a grid layout using Streamlit's columns
        for i in range(num_rows):
            column_list = st.columns(num_columns)

            for j in range(num_columns):
                movie_index = i * num_columns + j
                
                if movie_index < len(movie_list):

                    # Write inside each column
                    with column_list[j]:
                        self.write_single_movie(movie_list, movie_index)

    def write_single_movie(self, movie_list, movie_index):
        # Write movie title
        movie_title = movie_list[movie_index]
        st.write(f"{movie_title}")

        # Image URL for demonstration purposes, replace it with actual image URLs
        # image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/e/e7/Video-x-generic.svg/240px-Video-x-generic.svg.png"
        #st.image(image_url, caption=f"Poster {movie_index}", use_column_width=True)

        # Rating slider
        self.user_ratings.append(st.slider(f"Movie {movie_index}", min_value=1, max_value=5, value=0, step=1))

        # Checkbox to mark as not seen
        #self.not_seen.append(st.checkbox(f"Do not rate {movie_index}"))

        # Output spacer for movie grid
        st.write("------")


#@st.cache_resource()
class MovieRecommenderII():

    def __init__(self) -> None:
        
        # Load data
        

        # Preprocess data

        # Augment data

        # Prepopulate System II sim matrix
        try:
            self.sys_II_sim_matrix = self._local_load_precomputed_sim_matrix()
        except:
            self.sys_II_sim_matrix = self._load_precomputed_sim_matrix() 
        
    def _load_precomputed_sim_matrix(self):
        # Load Matrix file from github URL
        cached_results_url = 'https://github.com/jcm-art/uiuc_psl_public_streamlit/blob/main/app/src/resources/similarity_matrix.npy'
        resp = requests.get(cached_results_url)
        st.write(resp)
        sim_matrix = np.load(resp.text)

        #print(recommendation_dict)

        return sim_matrix

    def _local_load_precomputed_sim_matrix(self):
        # Confirm cached data is present
        cached_results_filepath = "src/resources/similarity_matrix.npy"
        print(f"Verifying system 2 cached sim matrix results exist: {os.path.isfile(cached_results_filepath)}")

        # Load np matrix
        sim_matrix = np.load(cached_results_filepath)

        return sim_matrix
    
    def get_genre_list(self):
        return self.genre_list
    
    def get_system_II_recommendation_list(self, movie_ids, user_ratings):
        #st.write(self.sys_II_sim_matrix)
        user_movie_vector = np.zeros((1, self.sys_II_sim_matrix.shape[0]))
        for i, movie_id in enumerate(movie_ids):
            if user_ratings[i]!=0:
                user_movie_vector[0, movie_id] = user_ratings[i]
        st.write(user_movie_vector)
        total_rated = np.count_nonzero(user_movie_vector)
        avg_rating = np.sum(user_movie_vector)/np.count_nonzero(user_movie_vector) if total_rated >0 else 0
        st.write(f"{avg_rating} is your average rating for {total_rated} movies")

        system_II_recommendations = ["TBD, Not Yet implemented" for _ in range(0, 10)]

        return system_II_recommendations

def main():
    current_page = MovieRecommendationPageII()
    current_page.write()

if __name__ == "__main__":
    main()