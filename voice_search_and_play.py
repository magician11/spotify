import tekore as tk
from auth import get_user_token
from speech import speech_to_text, text_to_speech
from player import get_first_available_device

# Get the user's token to be able to make requests on their account
token = get_user_token()
spotify = tk.Spotify(token)

#  Find the first available device
available_device = get_first_available_device(spotify)

text_to_speech('What music would you like to hear?')
heard = speech_to_text()
print(f'I heard you say "{heard}"')

# get the first track found from this search
tracks, = spotify.search(query=heard, limit=1)

if(len(tracks.items) == 0):
    print("I couldn't find any songs for this search. Exiting...")
    text_to_speech(
        "I'm sorry, I couldn't find any music matching this search. Bye!")
    exit()

# play the song!
message = f'Ok, playing "{tracks.items[0].name}" by "{tracks.items[0].artists[0].name}"...'
print(message)
text_to_speech(message)
spotify.playback_start_tracks([tracks.items[0].id])
