komunikat = input("Wprowadz komunikat")
nowy = ""

samogloski = "aąeęioóuy"

print()

for litera in komunikat:
    if litera.lower() not in samogloski:
        nowy += litera
        print("Został utworzony nowy łańcuch: ", nowy)

print("\nTwój komunikat bez samogłosek to:", nowy)

komunikat = "onomatopeja"
print(komunikat[2:7])
print(komunikat[2])
print(komunikat[7])
print(komunikat[7 - 1])