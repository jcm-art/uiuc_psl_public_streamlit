# PSL Streamlit App Page

import json
import os
import pathlib
import requests

import numpy as np
import pandas as pd
import streamlit as st

# To run, use: streamlit run app/src/main.py

class MovieRecommendationPage():

    def __init__(self):
        self.movie_recommender = MovieRecommender()
        self.genre_list = self.movie_recommender.get_genre_list()

    def write(self):
        st.title("Movie Recommender (PSL Project 4)")
        st.write("Authors: Justin Martin and Dillon Harding")
        st.header("System I: Popular movie recommendations")

        # Get genre selection from user
        st.subheader(f"Select a genre to receive movie recommendations")
        genre_selection = st.selectbox("Select a Genre", self.genre_list, index=0)

        # Give user recommendations for genre selection
        st.subheader(f"Top 10 Movies in {genre_selection} Genre")
        for i, movie_title in enumerate(self.movie_recommender.get_system_I_recommendation_list(genre_selection)):
            st.write(f"{i+1}) {movie_title}")
        st.write(f"")

        st.header("System II: Movie Recommendations based on User Preferences")
        # Get User ratings
        st.subheader("Rate the following movies to get a recommendation")

        # TODO - replace movie list with real movies
        movie_list = [
            "fake movie 1", "fake movie 2", "fake movie 3", "fake movie 4", "fake movie 5", 
            "fake movie 6", "fake movie 7", "fake movie 8", "fake movie 9", "fake movie 10", 
            "fake movie 11"]
        self.user_ratings = []
        self.not_seen = []

        # Make grid of movies for ratings
        self.make_movie_grid(movie_list)

        print(self.user_ratings)
        print(self.not_seen)
        st.subheader(f"Top 10 Movies Recommended for you")
        for i, movie_title in enumerate(self.movie_recommender.get_system_II_recommendation_list(movie_list, self.user_ratings)):
            st.write(f"{i+1}) {movie_title}")


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
        image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/e/e7/Video-x-generic.svg/240px-Video-x-generic.svg.png"
        st.image(image_url, caption=f"Poster {movie_index}", use_column_width=True)

        # Rating slider
        self.user_ratings.append(st.slider(f"Slider {movie_index}", min_value=1, max_value=5, value=3, step=1))

        # Checkbox to mark as not seen
        self.not_seen.append(st.checkbox(f"Do not rate {movie_index}"))

        # Output spacer for movie grid
        st.write("------")


#@st.cache_resource()
class MovieRecommender():

    def __init__(self) -> None:
        
        # Load data
        

        # Preprocess data

        # Augment data

        # Prepopulate System I recommendation dictionary
        try:
            self.sys_I_recommendation_dict = self._local_load_precomputed_recommendation_dict()
        except:
            self.sys_I_recommendation_dict = self._load_precomputed_recommendation_dict()

        # Populate Genre List
        self.genre_list = list(self.sys_I_recommendation_dict.keys())
        
    def _load_precomputed_recommendation_dict(self):
        # Load JSON file from github URL
        cached_results_url = 'https://github.com/jcm-art/uiuc_psl_public_streamlit/blob/main/app/src/resources/system_1_rec_dict.json'
        resp = requests.get(url)
        recommendation_dict = json.loads(resp.text)

        #print(recommendation_dict)

        return recommendation_dict

    def _local_load_precomputed_recommendation_dict(self):
        # Confirm cached data is present
        cached_results_filepath = "src/resources/system_1_rec_dict.json"
        print(f"Verifying system 1 cached results exist: {os.path.isfile(cached_results_filepath)}")

        # Load JSON file
        with open(cached_results_filepath, 'r') as json_file:
           recommendation_dict = json.load(json_file)

        #print(recommendation_dict)

        return recommendation_dict
    
    def get_genre_list(self):
        return self.genre_list

    def get_system_I_recommendation_list(self, genre: str):
        return self.sys_I_recommendation_dict[genre]
    
    def get_system_II_recommendation_list(self, movie_list, user_ratings):
        system_II_recommendations = ["TBD, Not Yet implemented" for _ in range(0, 10)]
        return system_II_recommendations

def main():
    current_page = MovieRecommendationPage()
    current_page.write()

if __name__ == "__main__":
    main()