import requests
import json
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")
Handle= "ManaStarsdotcom"
ApiKey= os.getenv("ApiKey")
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



