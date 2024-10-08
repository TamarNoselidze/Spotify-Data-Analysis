# Spotify Data Analysis Project

This project aims to analyze Spotify music data to uncover trends, such as artist popularity, song features, and year-over-year changes in music trends. 
The analysis is done using a combination of Python scripts and Jupyter notebooks.


## Project Files

 - `data.csv`, `data_2021.csv`, `data_2022.csv`, `data_2023.csv`, `data_2024.csv`: These files contain Spotify track data for respective years.
 - `new_data.csv`: A dataset containing additional or modified Spotify track data for analysis.
 - `fetch_spotify_tracks.py`: A Python script for fetching Spotify track information using Spotify's API.
 - `Spotify_Analysis.ipynb`: A Jupyter notebook containing all the code for data preprocessing, analysis, and visualization
 - `Spotify_Data_Analysis.pptx`: A PowerPoint presentation of the project's findings.



## Installation 

### Requirements:

- Python 3.x
- Jupyter Notebook

The following Python libraries:
- pandas
- numpy
- seaborn
- matplotlib
- spotipy *
- scikit-learn

*spotipy is only necessary if you wish to fetch your own data from Spotify API. 
-  Insert your credentials in the `CID` and `SECRET` variables in the `fetch_spotify_tracks.py` script to do so.


## Key Features of the Analysis

 - Data Wrangling: Merging datasets, cleaning missing values, and feature engineering.
 - Spotify API Data: Fetches additional track metadata using Spotify's API.
 - Visualizations: Graphs that illustrate trends in artist popularity, song features (tempo, loudness, etc.), and trends over time
 - Predictive Modeling: Includes a section that builds a simple model to predict song popularity.


For a detailed information about findings of the analysis, see the notebook `Spotify_Analysis.ipynb` or `Spotify_Data_Analysis.pptx`.



