# while-silmukat (loopit)

# jakolaskukone, jakaja ei voi olla nolla
""" monen rivin merkkijono, käytetään myös monen rivin kommenttina
num1 = float(input("Anna jaettava nro: "))
num2 = float(input("Anna jakaja: "))
while num2 == 0:
    print("Ei voi olla nolla.")
    num2 = float(input("Anna jakaja: "))

result = num1 / num2
print(f"Jakolaskun tulos on {result}")
"""

# iteroiva silmukka (käytetään "laskuria" silmukan toistokertojen määrittelyyn)
# i = 1  # iteraattori i
i = int(input("Mistä numerosta aloitetaan? "))
amount = int(input("Kuinka monta numeroa tulostetaan? "))
offset = int(input("Anna numeroiden väli: "))
max_number = amount * offset + i
while i < max_number:
    print(f"Numero on {i}")
    i = i + offset
print(f"i:n lopullinen arvo silmukan jälkeen: {i}")

# voit testata ehtolauseiden toimintaa tulostamalla niiden arvoja
print(i < i+1)  # -> True


# sisäkkäiset kontrollirakenteet ja satunnaisuus
import random

random_number = random.randint(1, 3)
print(f"Arvottu numero: {random_number}")

# pelin "asetukset"
player_count = 4
dice_amount = 3

# alustetaan parhaan tuloksen näyttämiseen tarvittavat muuttujat
best_player = None
best_result = 0

# jokainen pelaaja suorittaa vuorollaan, aloitetaan pelaajasta 1
current_player = 1
while current_player <= player_count:
    result = 0  # nopan silmälukujen summan ennen heittoja
    throw_count = 0  # iteraattori nopan heitoille
    # noppia heitetään dice_amount -muuttujassa asetettu määrä
    while throw_count < dice_amount:
        die = random.randint(1, 6)
        print(f"Pelaaja {current_player}, {throw_count+1}. heitto: {die}")
        result = result + die
        throw_count += 1  # sama kuin throw_count = throw_count + 1
    print(f"Pelaajan {current_player} tulos: {result}")
    # testataan saatiinko uusi paras tulos, ja tallennetaan tarvittaessa edellisen
    # parhaan tuloksen tilalle, päivitetään samalla paras pelaaja
    if result > best_result:
        best_result = result
        best_player = f"Pelaaja {current_player}"
    # jos tulos ei ole parempi, mutta on sama kuin edellinen paras tulos,
    # yhdistetään pelaajan nimi edellisen parhaan pelajaan nimen lisäksi samaan stringiin
    elif result == best_result:
        best_player = best_player + f", Pelaaja {current_player}"
    current_player = current_player + 1
print(f"paras tulos {best_result}, {best_player}")


# Break-komento, "heittää" ulos aktiivisesta silmukasta, suoritus jatkuu koodilohkon jälkeen
counter = 0
while True:  # ikuinen silmukka
    print(f"laskuri eka {counter}")
    counter += 1
    if counter == 5:
        break  # poistuu silmukan koodilohkosta samantien, allaoleva ei tulostu
    print(f"laskuri toka {counter}")

