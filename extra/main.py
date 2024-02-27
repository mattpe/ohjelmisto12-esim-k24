# pääohjelma
# kaikki import-lauseet on tapana laittaa tiedoston alkuun.
# (Tässä esimerkin vuoksi "väärin")

# koko moduulin import
#import functions_hello
#functions_hello.hello("Masa")

# yhden funktion import
from functions_hello import hello
hello("masa")

# import python-paketista (projektin alikansio)
#from paketti import module
#module.hello()

# toinen tapa
from paketti.module import hello
hello()