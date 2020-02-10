import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecoder

#Get the username


#  21mzu4nngumfd6423om3g3osa?si=FNiG1MIURgmhS6wbDB1gfw

username = sys.argv[1]

try:
    token = util.prompt_for_user_token(username)

except:
    os.remove(f".cache={username}")
    token = util.prompt_for_user_token(username)

spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
displayName = user["display_name"]
followers = user['followers']['total']

sp = spotipy.Spotify(auth=token)


print(">>> Welcome to Spotipy " + displayName, " !")
print(">>> You have ", followers, " followers.")
print("The admin have the following playlists...")


scope = ''
token = util.prompt_for_user_token(username, scope)

sp = spotipy.Spotify(auth=token)
sp.trace = False
results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))
