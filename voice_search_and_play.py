import speech_recognition as sr
import tekore as tk
from auth import get_user_token
from player import get_first_available_device

# Get the user's token to be able to make requests on their account
token = get_user_token()
spotify = tk.Spotify(token)

#  Find the first available device
available_device = get_first_available_device(spotify)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

heard = r.recognize_google(audio)
print(f'I heard you say "{heard}"')

# get the first track found from this search
tracks, = spotify.search(query=heard, limit=1)

# play the song!
print(
    f'About to play "{tracks.items[0].name}" by "{tracks.items[0].artists[0].name}" on {available_device.name} ({available_device.type})...')
spotify.playback_start_tracks([tracks.items[0].id])
