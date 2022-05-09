def get_first_available_device(spotify):
    available_devices = spotify.playback_devices()

    # If we have no available devices, exit the program
    if len(available_devices) == 0:
        print('No devices are available for this user.\nExiting...')
        exit()

    return available_devices[0]
