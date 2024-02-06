import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game2',
    user='username',
    password='password',
    autocommit=True
)

# luodaan osoitin ja sijoitetaan muuttujaan
cursor = connection.cursor()
# ajetaan sql-komento osoittimen execute-metodilla (=funktio)
cursor.execute("SELECT iso_country, name FROM country")
# fetchone hakee yhden rivin kerrallaan tulosjoukosta ja osoitin siirtyy seuraavalle riville
# result_row = cursor.fetchone()
# fetchall() hakee kaikki rivit
result_rows = cursor.fetchall()
#print(f"Ensimmäinen rivi: {result_rows[0]}, jossa maakoodi: {result_rows[0][0]}")
print(f"Maakoodeja löytyi {cursor.rowcount} kappaletta.")
if cursor.rowcount > 0:
    for row in result_rows:
        print(f"Maakoodi: {row[0]}, nimi: {row[1]}")
else:
    print("Ei tuloksia.")

# Parempi tapa: kääritään yksittäiset toiminnallisuudet uudelleenkäytettäviin funktioihin

def find_country_by_code(iso_code):
    sql = f"SELECT name, continent FROM country WHERE iso_country='{iso_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result
    return

def update_country_name_by_code(iso_code, name):
    sql = f"UPDATE country SET name='{name}' WHERE iso_country='{iso_code}'"
    # tarkasta, että sql on oikein muodostettu
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print(f"Tietue päivitetty ({iso_code}: {name}).")
        return True
    print("Pieleen meni.")

code_input = input("Anna maakoodi: ")
country_input = input("Uusi nimi: ")
update_country_name_by_code(code_input, country_input)

country = find_country_by_code(code_input)
# jos country != None
if country:
    print(f"Löydetty maa: {country[0]}, {country[1]}")
else:
    print("Ei tuloksia.")