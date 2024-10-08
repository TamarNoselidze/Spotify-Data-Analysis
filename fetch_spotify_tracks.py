import os

os.environ['CID'] = ''
os.environ['SECRET'] = ''



import logging
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import datetime

logger = logging.getLogger()


def get_tracks_data_by_month(spotify_client, year, chunk_size, max_results_per_month):
    tracks_data_list = []
    for month in range(1, 13):
        month_range = (datetime.date(year, month, 1), datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1))
        query = f'year:{year} month:{month}'
        for i in range(0, max_results_per_month, chunk_size):
            try:
                track_results = spotify_client.search(q=query, type='track', limit=chunk_size, offset=i)
                for track in track_results['tracks']['items']:
                    single_track_dict = {
                        'name': track['name'],
                        'artist_count': len(track['artists']),  # Concatenate all artist names
                        'track_id': track['id'],
                        'popularity': track.get('popularity', 0),  # Default popularity to 0 if not present
                        'year': year,  # Year from the outer loop
                        # 'explicit': track.get('explicit', False)  # Explicit status
                        'explicit': 1 if track.get('explicit', False) else 0  # Explicit status as integer

                    }
                    tracks_data_list.append(single_track_dict)
            except Exception as e:
                print(e)
                logger.info(e)
                continue
    return tracks_data_list


def get_audio_features_data(spotify_client, track_ids, chunk_size):
    audio_features_list = []
    for i in range(0, len(track_ids), chunk_size):
        try:
            track_id_list = track_ids[i:i+chunk_size]
            results = spotify_client.audio_features(track_id_list)
            results = [dict({'id': 'None'}) if v is None else v for v in results]
            audio_features_list.extend(results)
        except Exception as e:
            print(e)
            logger.info(e)
            continue
    return audio_features_list

def save_data_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def get_spotify_audio_features_data_to_csv(event, context):
    client_id = os.environ['CID']
    client_secret = os.environ['SECRET']
    spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    tracks_data_list = get_tracks_data_by_month(spotify_client, 2024, 50, 1000)
    track_ids = [d['track_id'] for d in tracks_data_list]
    audio_features_list = get_audio_features_data(spotify_client, track_ids, 100)
    
    # Combine track data with audio features
    merged_list = [{**u, **v} for u, v in zip(tracks_data_list, audio_features_list)]

    # Save the combined data to a CSV file
    save_data_to_csv(merged_list, 'data_2024.csv')

# Example direct call (remove event, context if not using in a cloud function)
get_spotify_audio_features_data_to_csv(None, None)
