slowo = input("Wprowadz slowo: ")
licznik = 0

for literka in slowo:
    print(literka)
    licznik += 1

print("Ilosc literek w slowie " + slowo + " to: ", licznik)