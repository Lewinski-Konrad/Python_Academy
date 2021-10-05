# Zadanie
# Napisz uproszczony kalkulator kredytowy.
# Celem kalkulatora jest sprawdzenie czy użytkownika
# stać na kredyt hipoteczny o podanych parametrach.
# Zapytaj użytkownika o:
#
# - kwotę kredytu
# - oprocentowanie kredytu
# - wartość wkładu własnego
# - czas kredytowania w latach
# - przychód miesięczny
# - sumę miesięcznych wydatków

print("Oto kalkulator kredytowy")

credit_amount = float(input("Wpisz pożądaną kwotę kredytu: "))
interest_rate = float(input("Wybierz oprocentowanie: "))
contribution = float(input("Wpisz iloość wkładu własnego: "))
credit_time = float(input("Wpisz czas kredytowania (w latach): "))
monthly_income = float(input("Jaki jest Twój przychód miesięczny?: "))
monthly_expenses = float(input("Wpisz swoje miesięczne wydatki: "))
print("")
credit_installment = float((credit_amount * interest_rate / 100) / 12 + credit_amount / (credit_time * 12))
funds_available = float(monthly_income - monthly_expenses)
property_value = float(contribution + credit_amount)

print(f"Rata kredytu wynosi {credit_installment:.2f}zł miesięcznie")
print(f"Dostępne środki wynoszą {funds_available:.2f}zł")
print(f"Wartość nieruchomości to {property_value:.2f}zł \n")

if contribution > property_value * 0.2:
    if funds_available > credit_installment + 1000:
        print("Gratulacje, możesz uzyskać podany kredyt!")
    else:
        print("Niestety nie możesz uzyskać podanego kredytu")
if property_value * 0.1 <= contribution <= property_value * 0.2:
    if funds_available > credit_installment + 2000:
        print("Gratulacje, możesz uzyskać podany kredyt!")
    else:
        print("Niestety nie możesz uzyskać podanego kredytu")
else:
    print("Niestety nie możesz uzyskać podanego kredytu")