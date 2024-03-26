# Moduuli 12 esimerkit

import requests


def search_shows(search_term):
    response = requests.get(f"https://api.tvmaze.com/search/shows?q={search_term}")
    shows = response.json()
    # print(f"Ensimmäisen sarjan nimi {shows[0]['show']['name']}")
    # Tulostetaan kaikki hakutulokset
    print(f"\nOhjelmahaun tulokset hakusanalla {search_term}:")
    for show in shows:
        # haetaan genret sisäkkäisellä silmukalla
        genres = ""
        for genre in show['show']['genres']:
            genres = genres + genre + " "
        print(f"{show['show']['name']} ({genres}): {show['show']['url']}")

search_input = input("Anna hakusana: ")
search_shows(search_input)