
# Esitellään luokka
class Player:
    def __init__(self, name, start_location):
        print("Luodaan uusi pelaaja")
        self.name = name
        self.score = 0
        self.location = start_location


p1 = Player("John", "Suomi")
p2 = Player("Jane", "Ruotsi")
p3 = Player("Mary", "Norja")

# p4 viittaa samaan Player-olioon kuin p1
p4 = p1
# p1.name = "John"
# print(p1)

print(f"{p1.name} ({p1.location}) pisteet: {p1.score}")
print(f"{p2.name} ({p2.location}) pisteet: {p2.score}")


