# PSL Streamlit App Page

import json
import os
import pathlib

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
        movie_list = ["fake movie 1", "fake movie 2", "fake movie 3", "fake movie 4", "fake movie 5"]
        user_ratings = [3 for _ in movie_list]

        for i, movie_name in enumerate(movie_list):
            user_ratings[i] = st.slider(f"{movie_name}", min_value=1, max_value=5, value=3, step=1)


        st.subheader(f"Top 10 Movies Recommended for you")
        for i, movie_title in enumerate(self.movie_recommender.get_system_II_recommendation_list(movie_list, user_ratings)):
            st.write(f"{i+1}) {movie_title}")


#@st.cache_resource()
class MovieRecommender():

    def __init__(self) -> None:
        
        # Load data
        

        # Preprocess data

        # Augment data

        # Prepopulate System I recommendation dictionary
        self.sys_I_recommendation_dict = self._load_precomputed_recommendation_dict()

        # Populate Genre List
        self.genre_list = list(self.sys_I_recommendation_dict.keys())
        
    def _load_precomputed_recommendation_dict(self):
        # Confirm cached data is present
        cached_results_filepath = "src/resources/system_1_rec_dict.json"
        print(f"Verifying system 1 cached results exist: {os.path.isfile(cached_results_filepath)}")

        # Load JSON file
        with open(cached_results_filepath, 'r') as json_file:
            recommendation_dict = json.load(json_file)

        print(recommendation_dict)

        return recommendation_dict
    
    def get_genre_list(self):
        return self.genre_list

    def get_system_I_recommendation_list(self, genre: str):
        return self.sys_I_recommendation_dict[genre]
    
    def get_system_II_recommendation_list(self, movie_list, user_ratings):
        system_II_recommendations = ["TBD, Not Yet implemented" for _ in range(0, 10)]
        return system_II_recommendations



# Function to load all test and train datasets
def _load_data(self, directory_root: str="./app/src/data/"):
    directory_path = pathlib.Path(directory_root)
    movie_filename = directory_path / "movies.dat"
    ratings_filename = directory_path / "ratings.dat"
    users_filename = directory_path / "users.dat"

    # Create a DataFrame from the three datasets
    movies_df = pd.read_csv(
        movie_filename, index_col=False, header=None, sep='::', names=['movie_id', 'title', 'genre'], encoding='latin-1'
    )
    ratings_df = pd.read_csv(
        ratings_filename, index_col=False, header=None, sep='::',names=['user_id', 'movie_id', 'rating', 'timestamp']
    )
    users_df = pd.read_csv(
        users_filename, index_col=False, header=None, sep='::',names=['user_id', 'gender', 'age', 'occupation','zipcode']
    )

    # Return dataframes
    return movies_df, ratings_df, users_df


def main():
    current_page = MovieRecommendationPage()
    current_page.write()

if __name__ == "__main__":
    main()