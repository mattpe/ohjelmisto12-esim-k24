# Moduuli 12 esimerkit

import requests


def search_shows(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    try:
        response = requests.get(url)
        print(f"HTTP response status code: {response.status_code}")
        shows = response.json()
        # print(f"Ensimmäisen sarjan nimi {shows[0]['show']['name']}")
        # Tulostetaan kaikki hakutulokset, jos http-pyyntö onnistui
        if response.status_code == 200:
            print(f"\nOhjelmahaun tulokset hakusanalla {search_term}:")
            for show in shows:
                # haetaan genret sisäkkäisellä silmukalla
                genres = ""
                for genre in show['show']['genres']:
                    genres = genres + genre + " "
                print(f"{show['show']['name']} ({genres}): {show['show']['url']}")
    except requests.exceptions.RequestException as error:
        print("HTTP-pyyntö meni pieleen. Ei verkkoyhteyttä palvelimeen.")
        print(error)


search_input = input("Anna hakusana: ")
search_shows(search_input)
