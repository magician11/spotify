import tekore as tk

CONFIG_FILE = 'credentials.config'

client_id, client_secret, redirect_uri = tk.config_from_file(CONFIG_FILE)

print(client_id)
print(client_secret)
print(redirect_uri)

# app_token = tk.request_client_token(client_id, client_secret)
# spotify = tk.Spotify(app_token)

# tracks, = spotify.search('ween')

# print(tracks)
# for result in tracks.items:
#     print(result.artists[0])

# album = spotify.album('3RBULTZJ97bvVzZLpxcB0j')
# print(album)
# print(album.artists[0])
# for track in album.tracks.items:
#     print(track.track_number, track.name)


user_token = tk.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=tk.scope.every
)

tk.config_to_file(CONFIG_FILE, client_id, client_secret,
                  redirect_uri + (user_token.refresh_token,))

spotify = tk.Spotify(user_token)
# spotify.token = user_token
devices = spotify.playback_devices()
for device in devices:
    print(device)

print(devices)
tracks = spotify.current_user_top_tracks(limit=10)
spotify.playback_start_tracks([t.id for t in tracks.items])
for track in tracks.items:
    print(track.name)
