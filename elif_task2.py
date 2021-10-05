# Zadanie nr 2
# Zaimplementuj program interpretujący wynik uzyskany w teście Coopera.
# Zapytaj o:
# -wiek
# -płeć
# -uzyskany wynik
# Na tej podstawie zinterpretuj rezultat.
# Możesz zaimplementować tylko wybrane przedziały wiekowe. (Przedział 20-39 lat)

print(f"Witaj w teście Coopera!\nAby przystąpić do testu, musisz być w przedziale wiekowym 20-39 lat.")
age = int(input("Ile masz lat? "))
gender = input("Jakiej jesteś płci (K/M)? ")
score = float(input("Jaki uzyskałeś/uzyskałaś wynik (w metrach)? "))
result = ""
print("")

if 20 <= age <= 29 and gender == "K":
    if score > 2700:
        result = "Bardzo dobrze!"
    elif 2200 <= score <= 2700:
        result = "Dobrze!"
    elif 1800 <= score <= 2199:
        result = "Średnio!"
    elif 1500 <= score <= 1799:
        result = "Źle!"
    else:
        result = "Bardzo źle!"
    print(f"Twój wynik to: {result}")

elif 30 <= age <= 39 and gender == "K":
    if score > 2500:
        result = "Bardzo dobrze!"
    elif 2000 <= score <= 2500:
        result = "Dobrze!"
    elif 1700 <= score <= 1999:
        result = "Średnio!"
    elif 1400 <= score <= 1699:
        result = "Źle!"
    else:
        result = "Bardzo źle!"
    print(f"Twój wynik to: {result}")

elif 20 <= age <= 29 and gender == "M":
    if score > 2800:
        result = "Bardzo dobrze!"
    elif 2400 <= score <= 2800:
        result = "Dobrze!"
    elif 2200 <= score <= 2399:
        result = "Średnio!"
    elif 1600 <= score <= 2199:
        result = "Źle!"
    else:
        result = "Bardzo źle!"
    print(f"Twój wynik to: {result}")

elif 30 <= age <= 39 and gender == "M":
    if score > 2700:
        result = "Bardzo dobrze!"
    elif 2300 <= score <= 2700:
        result = "Dobrze!"
    elif 1900 <= score <= 2299:
        result = "Średnio!"
    elif 1500 <= score <= 1899:
        result = "Źle!"
    else:
        result = "Bardzo źle!"
    print(f"Twój wynik to: {result}")

else:
    print("Błędnie wprowadzone dane!")