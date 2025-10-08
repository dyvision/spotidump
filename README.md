
## SpotiDump | Backup Your Spotify

### Before you begin go to https://developer.spotify.com/dashboard
- Install [https://ffmpeg.org/](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z)
- Create a dev account
- Create an app
- Fill out the info for the app, make sure redirect urls contains: https://localhost:8888/callback and "Web API" is checked
- Save it
- Click on the app settings and get the client id and after click "view client secret". Place these in the .env file in the root folder without any spacing accordingly

### Running
- After configuring simply click the SpotiDump.bat file
- You will be prompted for a download location. All of your playlists will be dropped here so you may want to create a new music folder (ie: if I entered "c:\" for my location it would create "c:\playlist1" "c:\playlist2" so create a music folder and point to "c:\music")
- After the script will install requirements
- After the script will open a web browser to log you in to spotify
- After logging in copy the redirect url that it sends you to and paste it in the script console
- The script will continue to run until completed
