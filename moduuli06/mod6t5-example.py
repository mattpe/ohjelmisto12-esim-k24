"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
parametrina saatu lista paitsi että siitä on karsittu pois kaikki
parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot
listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen
että karsitun listan
"""

def get_even_numbers(numbers):
    # luodaan uusi tyhjä lista, millä ei ole mitään tekemistä alkup. kanssa
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            # lisätään arvo uuteen listaan, jos se on parillinen
            even_numbers.append(num)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5]
even_numbers = get_even_numbers(numbers)
print(f"Alkuperäiset luvut: {numbers}, parilliset luvut: {even_numbers}")