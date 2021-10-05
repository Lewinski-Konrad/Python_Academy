# Zadanie nr 1
# Połącz kalkulator wartości lokaty i kredytowy.
# Zapytaj użytkownika czy chce obliczyć wartość lokaty czy zdolność kredytową.
# Następnie wyznacz oczekiwaną wartość.
# Obsłuż (na przykład odpowiednim komunikatem) sytuację,
# w której użytkownik wybierze nieistniejącą opcję.

user_choice = input('Wpisz "lokata", aby uruchomić kalkulator wartości lokaty lub "kredyt", \naby uruchomić kalkulator kredytowy: ')
print("")
if user_choice == "lokata":

    print("Obliczę dla Ciebie wartość lokaty.")
    initial_value_input = input("Jaka jest początkowa wartość Twojej lokaty? ")
    percentage_input = input("Jakie jest oprocentowanie? ")
    time_input = input("Ile lat trwa lokata? ")

    initial_value = int(initial_value_input)
    percentage = int(percentage_input)
    time = int(time_input)

    final_value = initial_value * (1 + percentage/100) ** time

    print(f"Wartość Twojej lokaty wyniesie {final_value:.2f} zł! \n")
    print(f"Czy inwestycja wzrośnie o co najmniej 10%? {final_value >= initial_value * 1.1}\n")




elif user_choice == "kredyt":
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

else:
    print(f'Uwaga! Wpisano niewłaściwą opcję -> "{user_choice}"')