from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging
from flask_cors import CORS
app = Flask(__name__)

CORS(app, resources={r"/": {"origins": ""}}, supports_credentials=True)
# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Global variables
recent_song = None
favorites = []

# Load the processed dataset
try:
    df = pd.read_csv("processed_music_data.csv")
    logging.info("Dataset loaded successfully.")
except FileNotFoundError:
    logging.error("Dataset file 'processed_music_data.csv' not found.")
    exit()

# Verify that the required columns exist
if 'title' not in df.columns or 'Tags' not in df.columns:
    logging.error("Dataset must contain 'title' and 'Tags' columns.")
    exit()

# Load or compute the similarity matrix
try:
    similarity = pickle.load(open("similarities.pkl", "rb"))
    logging.info("Similarity matrix loaded successfully.")
except FileNotFoundError:
    logging.warning("Similarity matrix not found. Computing a new one...")
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df['Tags'])
    similarity = cosine_similarity(count_matrix)
    pickle.dump(similarity, open("similarities.pkl", "wb"))
    logging.info("New similarity matrix computed and saved.")

# Function to recommend songs
def recommend_songs(song):
    if song not in df['title'].values:
        return []
    idx = df[df['title'] == song].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended_songs = [df.iloc[i[0]]['title'] for i in sorted_scores]
    return recommended_songs

# API to recommend songs
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    song = data.get('song')
    if not song or song not in df['title'].values:
        return jsonify({"error": "Song not found in the dataset."}), 400

    # Update the recent_song to the song being recommended
    global recent_song
    recent_song = song

    # Get recommendations
    recommended_songs = recommend_songs(song)

    return jsonify({
        "song": song,
        "recommendations": recommended_songs
    })

# API to add a song to favorites
@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    data = request.get_json()
    song = data.get('song')
    if not song or song not in df['title'].values:
        return jsonify({"error": "Song not found in the dataset."}), 400

    # Add the song to the favorites list
    favorites.append(song)

    # Update the recent_song to the newly added favorite
    global recent_song
    recent_song = song

    # Recommend 5-6 similar songs for the newly added favorite
    recommended_songs = recommend_songs(song)

    return jsonify({
        "message": f"'{song}' added to favorites.",
        "recommendations": recommended_songs
    })

# API to get the next song based on recent_song
@app.route('/next_song', methods=['POST'])
def next_song():
    global recent_song
    if not recent_song:
        return jsonify({"error": "No song played recently."}), 400

    # Get a recommendation based on the recent song
    recommendations = recommend_songs(recent_song)

    if recommendations:
        # Pick the first recommendation as the "next song"
        next_song = recommendations[0]

        # Update recent_song
        recent_song = next_song

        return jsonify({"next_song": next_song})
    else:
        return jsonify({"error": "No similar songs found."}), 400

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
