import sys
import tekore as tk
from auth import get_user_token
from player import get_first_available_device

# Get the user's token to be able to make requests on their account
token = get_user_token()
spotify = tk.Spotify(token)

#  Find the first available device
available_device = get_first_available_device(spotify)

if len(sys.argv) == 1:
    print(f'Usage: python {sys.argv[0]} <string_to_search>')
    exit()

# get the search string from the command line
search_string = ' '.join(sys.argv[1:])

# get the tracks found from this search
tracks, = spotify.search(query=search_string)

# play the songs!
print(f'About to play {len(tracks.items)} tracks for "{search_string}" on {available_device.name} ({available_device.type})...')
spotify.playback_start_tracks([t.id for t in tracks.items])
