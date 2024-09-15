from data_processing import mood_dfs, df

import pandas as pd

def mood_artist(mood=None, artists=None, genres=None):
    # Convert single values to lists if necessary (not needed here with Streamlit)
    # artists and genres are already lists from Streamlit's multiselect

    # Select DataFrame based on mood, or use the main df if no mood is specified
    if mood and mood in mood_dfs:
        df_filtered = mood_dfs[mood].copy()
    else:
        # If no mood is specified, use the main DataFrame (df_main)
        df_filtered = df.copy()
    
    # Filter by multiple artists if provided
    if artists:
        df_filtered = df_filtered[df_filtered['artist_name'].isin(artists)]
    
    # Filter by multiple genres if provided
    if genres:
        df_filtered = df_filtered[df_filtered['genre'].isin(genres)]
    
    # Sort the results by popularity
    df_filtered_sorted = df_filtered.sort_values(by='popularity', ascending=False)
    
    # Determine number of genres and artists to sample from
    num_genres = len(genres) if genres else 1
    num_artists = len(artists) if artists else 1
    
    total_samples = 50
    samples_per_genre = total_samples // num_genres
    samples_per_artist = total_samples // num_artists
    
    result_dfs = []
    
    # For each genre, sample the appropriate number of tracks (only if genres are provided)
    if genres:
        for genre in genres:
            genre_df = df_filtered_sorted[df_filtered_sorted['genre'] == genre]
            # Sample evenly for each genre
            n_sample_genre = min(samples_per_genre, len(genre_df))  # Ensure we don't sample more than available
            sampled_df_genre = genre_df.sample(n=n_sample_genre, random_state=42)  # random_state for reproducibility
            result_dfs.append(sampled_df_genre)
    
    # For each artist, sample the appropriate number of tracks (only if artists are provided)
    if artists:
        for artist in artists:
            artist_df = df_filtered_sorted[df_filtered_sorted['artist_name'] == artist]
            # Sample evenly for each artist
            n_sample_artist = min(samples_per_artist, len(artist_df))  # Ensure we don't sample more than available
            sampled_df_artist = artist_df.sample(n=n_sample_artist, random_state=42)  # random_state for reproducibility
            result_dfs.append(sampled_df_artist)
    
    # If genres and artists are not provided, just use the filtered DataFrame
    if not result_dfs:
        final_result = df_filtered_sorted.head(total_samples)
    else:
        # Combine all the sampled results
        final_result = pd.concat(result_dfs)
    
    # Shuffle the final result
    final_result_shuffled = final_result.sample(frac=1).reset_index(drop=True)
    
    return final_result_shuffled


