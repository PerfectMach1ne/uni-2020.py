# krotki i plecak

plecak = ("latarka",
          "scyzoryk",
          "lina")

starePudlo = ("leki", "pistolet")

print("Podczas swojej wędrówki, znajdujesz stare pudło, otwierasz je i widzisz: ")

for item in starePudlo:
    print(item)

print("Czy wziąć zawartość pudła?")
print("1. Tak")
print("2. Nie")

wybor = int(input(": "))

print("Zawartość twojego plecaka to: ")

if wybor == 1:
    plecak = plecak + starePudlo

for item in plecak:
    print(item)