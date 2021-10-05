# Zadanie nr 3
# Zapytaj użytkownika o numer telefonu i wypisz go w postaci zanonimizowanej.
#
# Wypisz pierwszych 5 cyfr, a kolejne zastąp myślnikiem.


phone_number = input("Jaki jest Twój numer telefonu? ")
phone_number = phone_number.replace("-", "")
phone_number = phone_number.replace(" ", "")
public_digits = phone_number[:5]
number_of_private_digits = len(phone_number) - 5
private_digits = "-" * number_of_private_digits
anonymous_number = f"{public_digits}{private_digits}"

print("Zanonimizowany numer:", anonymous_number)