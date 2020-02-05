
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecoder

#Get the username

username = sys.argv[1]

# USER ID : 21mzu4nngumfd6423om3g3osa?si=FNiG1MIURgmhS6wbDB1gfw

# Erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)



except:
    os.remove(f".cache={username}")
    token = util.prompt_for_user_token(username)

# create out spotify object

spotifyObject = spotipy.Spotify(auth=token)


user = spotifyObject.current_user()

displayName = user["display_name"]
followers = user['followers']['total']

while True:
    print()
    print(">>> Welcome to Spotipy " + displayName, " !")
    print(">>> You have ", followers, " followers.")
    print()
    print("0 - Search for an aritst")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    # Search for the artist
    if choice == "0":
        print()

        searchQuery = input("Ok, What's their name? : ")
        print()

        # get search results

        searchResults = spotifyObject.search(searchQuery, 1,0,"artist")

        artist = searchResults['artists']['items'][0]

        # artist details
        print(artist['name'])
        print(str(artist['followers']['total'])+ " followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # album details
        trackURI = []
        trackART = []
        z = 0

        # extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM ", item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # extract track data
            trackReults = spotifyObject.album_tracks(albumID)
            trackReults = trackReults['items']

            for item in trackReults:
                print(str(z) + ": "+item['name'])
                trackURI.append(item['uri'])
                trackART.append(albumArt)
                z=z+1
            print()

        #see the album art

        while True:
            songSelection = input("Enter a song number to the see thae album art associated with it or X to exit: ")

            if songSelection == "x" or "X":
                break
            webbrowser.open(trackART[int(songSelection)])



    elif choice == "1":
        break




# print(json.dumps(VARIABLE, sort_keys=True, indent=4)) #useful


