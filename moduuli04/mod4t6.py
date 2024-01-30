import random
# alustetaan pisteiden lkm-laskurit, arvo 0
N = n = 0

while N < 1000:
    # arvotaan yksi piste
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    N += 1
    print(f"Arvottu piste: {x}, {y}")
    # onko piste yksikkö ympyrän sisällä? (x^2+y^2<1):
    if x * x + y * y < 1:
        n += 1
print(f"Pisteitä yhteensä {N}, joista ympyrän sisällä {n}.")
# TODO: laske piin likiarvo tehtävässä annetulla kaavalla ja tulosta
