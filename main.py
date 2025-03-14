### SpotiDump | Backup Your Spotify ###

#Before you begin go to https://developer.spotify.com/dashboard
#Create a dev account
#Create an app
#Fill out the info for the app, make sure redirect urls contains: https://localhost:8888/callback and "Web API" is checked
#Save it
#Click on the app settings and get the client id and after click "view client secret". Place these in the .env file in the root folder without any spacing accordingly

import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
  
try:     
    os.remove('.cache')
except:
    pass

clear()
location = input('Paste the location of where you would like to save the files (remove any quotes):')

if location == "":
    location = '.'

print("Installing required libraries...")
os.system('pip install -r ./requirements.txt')

from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

clear()

load_dotenv()

input("You will now be redirected to Spotify. Login and copy the URL you're directed to on login. You will paste that in the next window. \r\n\r\n Press ENTER to continue")


try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ['client_id'],
                                                           client_secret=os.environ['client_secret'],redirect_uri="https://localhost:8888/callback",scope="user-library-read"))
    clear()
    
except:
    clear()
    print("You don't have your .env file filled out with the correct info. View the readme file for advice on how to configure")
    exit()

playlists = []
albums = []
liked = []

#query playlists
p_request = sp.current_user_playlists(limit=100)
playlists.extend(p_request['items'])
while p_request['next'] != None:
    playlists.extend(p_request['items'])
    p_request = sp.next(p_request)
    
#query albums
a_request = sp.current_user_saved_albums(50)
albums.extend(a_request['items'])
while a_request['next'] != None:
    albums.extend(a_request['items'])       
    a_request = sp.next(a_request)

#query liked songs
l_request = sp.current_user_saved_tracks(50)
liked.extend(l_request['items'])
while l_request['next'] != None:
    liked.extend(l_request['items'])       
    l_request = sp.next(l_request)    

#playlists:
for item in playlists:
    clear()
    print("Downloading {}...".format(item['name']))
    folder = '{}/{}'.format(location,item['name'].replace(' ','-').replace('*','').replace('/','-').replace('\\','-'))
    try:
        os.mkdir(folder)
        print("Created {}".format(folder))
    except:
        print('{} already created'.format(folder))
    os.system('python -m spotdl {} --overwrite skip --output "{}"'.format(item['external_urls']['spotify'],folder))

#albums:
for item in albums:
    clear()
    print("Downloading {}...".format(item['album']['name']))
    folder = '{}/{}'.format(location,item['album']['name'].replace(' ','-').replace('*','').replace('/','-').replace('\\','-'))
    try:
        os.mkdir(folder)
        print("Created {}".format(folder))
    except:
        print('{} already created'.format(folder))
    os.system('python -m spotdl {} --overwrite skip --output "{}"'.format(item['album']['external_urls']['spotify'],folder))

            
#liked:
folder = '{}/Liked-Songs'.format(location)
try:
    os.mkdir(folder)
    print("Created {}".format(folder))
except:
    print('{} already created'.format(folder))
for item in liked:
    clear()
    print("Downloading Liked Songs Playlist...")
    os.system('python -m spotdl {} --overwrite skip --output "{}"'.format(item['track']['external_urls']['spotify'],folder))
    
clear()
print("SpotiDump completed. Please navigate to \"{}\" to see your results".format(location))
                        