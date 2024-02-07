# tworzenie krotki
kierownik = ("Jan", "Kowalski", 34, 5500, "Sardynkowa 5")

# wyswietlanie krotki
print(kierownik)

# wyswietlanie sekwencyjne
i = 1
for element in kierownik:
    print(str(i) + ". " + str(element))
    i += 1