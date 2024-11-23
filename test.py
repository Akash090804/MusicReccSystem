import requests
import json

BASE_URL = "http://127.0.0.1:5000"

# Function to test the /recommend endpoint
def test_recommend(song_name):
    url = f"{BASE_URL}/recommend"
    data = {"song": song_name}
    response = requests.post(url, json=data)
    print(f"Testing /recommend with song: {song_name}")
    print("Response:", response.status_code, response.json())
    print()

# Function to test the /add_favorite endpoint
def test_add_favorite(song_name):
    url = f"{BASE_URL}/add_favorite"
    data = {"song": song_name}
    response = requests.post(url, json=data)
    print(f"Testing /add_favorite with song: {song_name}")
    print("Response:", response.status_code, response.json())
    print()

# Function to test the /next_song endpoint
def test_next_song():
    url = f"{BASE_URL}/next_song"
    response = requests.post(url)
    print("Testing /next_song")
    print("Response:", response.status_code, response.json())
    print()

if __name__ == "__main__":
    # Replace "Coca Cola" with a valid song title from your dataset for testing
    test_recommend("Coca Cola")
    test_add_favorite("Coca Cola")
    test_next_song()
