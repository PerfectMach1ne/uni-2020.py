import random

# sekwencje (krotke) słów do wyboru

PULA = ("Python", "Anagram", "onomatopeja", "autostrada",
        "lampka", "seksofon", "hamburguesa")

# wybieramy losowe słowo z puli

slowo = random.choice(PULA)

# zmienna trzymająca poprawne słowo

correct = slowo

# algorytm mieszania liter

pomieszane = ""

szanse = 4

while slowo:
    pozycja = random.randint(0, len(slowo)-1)
    pomieszane += slowo[pozycja]
    slowo = slowo[:pozycja] + slowo[(pozycja + 1):]     # slowo[0:pozycja] + slowo[(pozycja+1):]

# rozpoczynamy gre

print("Zgadnij, jakie to słowo: ", pomieszane)

odpowiedz = input("\nTwoja odpowiedź: ")
while odpowiedz != correct and odpowiedz != "":
    szanse -= 1
    if szanse == 0:
        print("Koniec szans. tyler1laugh.mp3")
        break
    print("Niestety, to nie to słowo.")
    odpowiedz = input("\nTwoja odpowiedź: ")

if odpowiedz == correct:
    print("Zgadza się!!!")

print("Dziękuję za udział w GrZe")