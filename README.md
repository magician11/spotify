# Spotify

All things fun and games with Spotify.

## Setup

Install the Tekore library.

`pip install tk`

Create a file called `credentials.config` and add the following lines

```
[DEFAULT]
SPOTIFY_CLIENT_ID = xxx
SPOTIFY_CLIENT_SECRET = yyy
SPOTIFY_REDIRECT_URI = zzz
```

Then add the refresh token to the config file by running

`python3 get_refresh_token.py`

