import tekore as tk
from auth import get_user_token
from player import get_first_available_device

# Get the user's token to be able to make requests on their account
token = get_user_token()
spotify = tk.Spotify(token)

#  Find the first available device
available_device = get_first_available_device(spotify)

# Find the user's top artist
top_artist = spotify.current_user_top_artists(limit=1).items[0]

# Play the user's top artist on the first available device
print(
    f'About to play {top_artist.name} on {available_device.name} ({available_device.type})...')
spotify.playback_start_context(
    context_uri=top_artist.uri, device_id=available_device.id)
