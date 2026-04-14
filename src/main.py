"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.9}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.95, "likes_acoustic": False}),
    ]

    for label, user_prefs in profiles:
        print(f"\n=== {label} ===")
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("Top recommendations:\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"Title: {song['title']}")
            print(f"Artist: {song['artist']}")
            print(f"Score: {score:.2f}")
            print(f"Reasons: {explanation}")
            print()


if __name__ == "__main__":
    main()
