import requests
import json

ApiKey= "AIzaSyCRGY0C1ciI2AMVSGsK6HY5NtXlYVTSmbU"
Handle= "ManaStarsdotcom"

def get_playlist():

    try:

        url= f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={Handle}&key={ApiKey}"

        response= requests.get(url)
        data = response.json()
        response.raise_for_status()

        #print(json.dumps(data,indent=4))

        channel_items=data["items"][0]
        channel_playlist=channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        return channel_playlist
    except requests.exceptions.RequestException as e:
        print(e)

if __name__ == "__main__":
    playlist_id= get_playlist()
    print(playlist_id)
else:
    print("You are trying to run from an external location")


