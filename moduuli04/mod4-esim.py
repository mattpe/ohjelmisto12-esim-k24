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
