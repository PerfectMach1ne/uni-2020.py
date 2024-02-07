message = input("Wprowadz komunikat: ")

print("\nDlugość twojego komunikatu wynosi: ", len(message))

print("\nNajczęściej występująca litera w języku pulskoim, 'a', ")
if 'a' in message:
    print("wystąpiła w twoim komunikacie")
else:
    print("nie wystąpiła w twoim komunikacie")