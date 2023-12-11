# PSL Streamlit App Page

import json
import os
import pathlib
import requests

import numpy as np
import pandas as pd
import streamlit as st

class MovieRecommendationPageI():

    def __init__(self):
        self.movie_recommender = MovieRecommenderI()
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

#@st.cache_resource()
class MovieRecommenderI():

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
        cached_results_url = 'https://raw.githubusercontent.com/jcm-art/uiuc_psl_public_streamlit/main/src/resources/system_1_rec_dict.json'
        resp = requests.get(cached_results_url)
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
        st.write(self.sys_II_sim_matrix)
        system_II_recommendations = ["TBD, Not Yet implemented" for _ in range(0, 10)]
        return system_II_recommendations

def main():
    current_page = MovieRecommendationPageI()
    current_page.write()

if __name__ == "__main__":
    main()