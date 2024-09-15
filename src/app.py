import streamlit as st
import pandas as pd
from data_processing import mood_dfs, df
from recommendation import mood_artist

# Define mood options
mood_options = [
    'happy', 'sad', 'angry', 'anxious', 'relaxed', 'excited', 
    'bored', 'lonely', 'hopeful', 'confident', 'tired', 
    'irritated', 'surprised', 'grateful', 'fearful'
]

# Load DataFrames for artists and genres
unique_artists_df = pd.read_csv('Data/unique_artists.csv')
unique_genres_df = pd.read_csv('Data/unique_genres.csv')

# Convert the 'artist_name' and 'genre' columns to lists
unique_artists = unique_artists_df['artist_name'].tolist()
unique_genres = unique_genres_df['genre'].tolist()

# Streamlit App Layout
background_image_url = 'static/id_card.jpg'

# Inject custom CSS into the Streamlit app
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({background_image_url});
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Mood-Based Music Recommendation Engine")

# Input selection
mood = st.selectbox("Select a Mood", options=['None']+mood_options)
artists = st.multiselect("Search and select artists", options=unique_artists)
genres = st.multiselect("Search and select genres", options=unique_genres)

# Debug: Output selected inputs
st.write(f"Selected Mood: {mood}")
st.write(f"Selected Artists: {artists}")
st.write(f"Selected Genres: {genres}")

# Generate Recommendations
if st.button('Generate Recommendations'):
    recommendations = mood_artist(mood=mood, artists=artists, genres=genres)
    
    # Debug: Output the shape and columns of the recommendations
    if recommendations.empty:
        st.write("No recommendations found. Try adjusting your inputs.")
    else:
        st.write("Here are your recommendations:")
        st.dataframe(recommendations[['track_name', 'artist_name', 'genre']])

# Reset Button
if st.button('Reset'):
    st.experimental_rerun()
