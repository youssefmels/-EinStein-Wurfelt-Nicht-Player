import requests
import os
from bs4 import BeautifulSoup

def download_txt_file(requests, url):
    os.makedirs("downloads", exist_ok=True)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features = 'html.parser')
        tag = soup.select_one('a[href*="player_game_list_txt"]')
        
        domain = "https://www.littlegolem.net/jsp/info/"

        parameters = tag['href'].replace('>', '&gt')
        uri = domain + parameters
        print("Download URL:", uri)

        request = requests.get(uri)
        if request.status_code == 200:
            filename = "downloads/match_history.txt"
            with open(filename, 'wb') as f:
                f.write(request.content)
                print("Successful")
                
    else:
        print("failed. status code: ", response.status_code)
    pass

def main():
    download_txt_file(requests, "https://www.littlegolem.net/jsp/info/player_game_list.jsp?gtid=einstein&plid=10675")
    pass


if __name__ == "__main__":
    main()