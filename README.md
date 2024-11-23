# Music Recommendation System API

This project provides a Flask-based API for recommending songs, adding songs to favorites, and fetching the next song based on the most recently played song.

## Base API URL
https://music-recommendation-system-qirr.onrender.com

---

## Endpoints

### 1. Recommend Songs
- **Endpoint**: /recommend
- **Method**: POST
- **Description**: Takes a song title as input and recommends 5 similar songs based on the dataset.

#### Request Body (JSON):
{
  "song": "Song Title Here"
}

#### Response (JSON):
{
  "song": "Song Title Here",
  "recommendations": [
    "Recommended Song 1",
    "Recommended Song 2",
    "Recommended Song 3",
    "Recommended Song 4",
    "Recommended Song 5"
  ]
}

#### Error Response:
{
  "error": "Song not found in the dataset."
}

---

### 2. Add Song to Favorites
- **Endpoint**: /add_favorite
- **Method**: POST
- **Description**: Adds a song to the favorites list and provides recommendations for 5 similar songs.

#### Request Body (JSON):
{
  "song": "Song Title Here"
}

#### Response (JSON):
{
  "message": "'Song Title Here' added to favorites.",
  "recommendations": [
    "Similar Song 1",
    "Similar Song 2",
    "Similar Song 3",
    "Similar Song 4",
    "Similar Song 5"
  ]
}

#### Error Response:
{
  "error": "Song not found in the dataset."
}

---

### 3. Get Next Song
- **Endpoint**: /next_song
- **Method**: POST
- **Description**: Fetches the next song based on the most recently played song.

#### Request Body: None.

#### Response (JSON):
{
  "next_song": "Next Song Title Here"
}

#### Error Response:
{
  "error": "No song played recently."
}

---

## How to Test the API

### 1. Using Postman
- Import the API endpoints into Postman.
- Use the base URL for requests.
- Configure the request body (if applicable) as per the specifications.

### 2. Using cURL (Command Line)

#### Recommend Songs:
curl -X POST -H "Content-Type: application/json" \
-d '{"song": "Song Title Here"}' \
https://music-recommendation-system-qirr.onrender.com/recommend

#### Add Song to Favorites:
curl -X POST -H "Content-Type: application/json" \
-d '{"song": "Song Title Here"}' \
https://music-recommendation-system-qirr.onrender.com/add_favorite

#### Get Next Song:
curl -X POST https://music-recommendation-system-qirr.onrender.com/next_song

---

## Project Setup
1. Clone the repository and navigate to the project directory.
2. Install the required Python libraries:
   pip install flask pandas scikit-learn flask-cors
3. Ensure the following files are present in the project directory:
   - processed_music_data.csv
   - similarities.pkl (optional; if not present, the application will compute and save it.)
4. Run the application:
   python app.py
5. Access the API locally at http://127.0.0.1:5000.

---

## Key Features
- Recommend songs based on similarity tags.
- Maintain a list of favorite songs.
- Fetch the next song recommendation.

---

