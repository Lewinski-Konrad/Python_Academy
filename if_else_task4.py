# Zadanie nr 4
# Zapytaj o imię i "rozpoznaj" czy użytkownik to kobieta czy mężczyzna.
# Podpowiedź: Na potrzeby tego zadania możemy założyć,
# że żeńskie imiona kończą się na "a".

user_name = input("Jak masz na imię? ")
if user_name[len(user_name)-1] == "a":   # lub user_name[-1]
    print(f"Cześć, {user_name}, wydaje mi się, że jesteś dziewczyną!")
else:
    print(f"Cześć, {user_name}, wydaje mi się, że jesteś chłopakiem!")

