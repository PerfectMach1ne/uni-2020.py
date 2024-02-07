slowo = input("Podaj slowo: ")
dlugoscSlowa = len(slowo)
literka = int(input("Podaj numer litery do wyswietlenia: "))

if literka < dlugoscSlowa:
    print("Na miejscu", literka, "wystepuje litera:", slowo[literka])
else:
    print("Slowo nie ma tylu liter!")

slowo = "Onomatopeja"

print(slowo)
print(slowo[3])
print(slowo[0] + slowo[2])
# print(slowo[11]) ===> ERROR - index 11 is out of bound
# the lenght of the string is 11, so its' last index is 10 = 11 - 1

slowo = input("Podaj słowo: ")

print(slowo)
print(slowo[0])

dlugoscSlowa = len(slowo)
print(slowo[dlugoscSlowa - 1])

for i in range(75):
    print('=', end = "")
print("\n" + slowo[-1])