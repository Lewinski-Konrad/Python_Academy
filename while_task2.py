# Zadanie nr 2
# Wczytaj numer telefonu użytkownika i rozdziel go myślnikami (format XXX-XXX-XXX).

phone_number = input("Podaj swój numer telefonu: ")
phone_number = phone_number.replace("-", "").replace(" ", "")
phone_number_formated = ""
phone_index = 0

while phone_index < len(phone_number):
    if phone_index % 3 == 0 and phone_index != 0:
        phone_number_formated += "-"
    phone_number_formated += phone_number[phone_index]
    phone_index += 1

print(phone_number_formated)

