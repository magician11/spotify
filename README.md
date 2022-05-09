# Spotify

All things fun and games with Spotify.

## Setup

### Python

This code is written in the Python programming language.

While versions of Python may come with your OS, I used [pyenv](https://github.com/pyenv/pyenv) to install the latest version.

This README assumes the latest version of your Python install is run using `python`

### Install the Tekore library

`pip install tk`

### Setup your credentials file

Create a file called `credentials.config`
Goto the [Spotify for Developers Dashboard](https://developer.spotify.com/dashboard/applications) and create an app.

Then add the following lines to `credentials.config`

```
[DEFAULT]
SPOTIFY_CLIENT_ID = xxx
SPOTIFY_CLIENT_SECRET = yyy
SPOTIFY_REDIRECT_URI = https://example.com/callback
```

### Add a refresh token to your config file

Then add a refresh token to the config file by running

`python get_refresh_token.py`

You'll then see in your `credentials.config` the added line

`SPOTIFY_USER_REFRESH = aaa`

## Using the Spotify API

I've included some example scripts.

- `list_top_11.py` will list your top artists and tracks
- `play_fav_artist.py` will play your favourite artist on your first available device

To run any of them, simply type `python [_script_.py]`

To find out what else you can do with the Tekore library in interacting with Spotify, [view their docs](https://tekore.readthedocs.io/en/stable/index.html).
