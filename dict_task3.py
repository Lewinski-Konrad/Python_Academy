# Zadanie nr 3
# Zapytaj użytkownika ile miesięcznie wydaje pieniędzy na:
# -jedzenie
# -rozrywkę
# -opłaty
# -inne
# Oblicz udział procentowy każdej kategorii w łącznych wydatkach.
# Następnie poproś użytkownika o wybór kategorii i wypisz jaki
# jest jej udział procentowy.


expenditures = {
    "jedzenie": float(input("Ile miesięcznie wydajesz na jedzenie? ")),
    "rozrywka": float(input("Ile miesięcznie wydajesz na rozrywkę? ")),
    "opłaty": float(input("Ile miesięcznie wydajesz na opłaty? ")),
    "inne": float(input("Ile miesięcznie wydajesz na inne sprawy? ")),
}

exp_values = list(expenditures.values())
total_expenses = exp_values[0] + exp_values[1] + exp_values[2] + exp_values[3]

food_percentage = float(exp_values[0] / total_expenses * 100)
entertainment_percentage = float(exp_values[1] / total_expenses * 100)
expenses_percentage = float(exp_values[2] / total_expenses * 100)
other_percentage = float(exp_values[3] / total_expenses * 100)

expenditures_percentage = {
    "jedzenie": food_percentage,
    "rozrywka": entertainment_percentage,
    "opłaty": expenses_percentage,
    "inne": other_percentage,
}

category = str(input("Wybierz kategorię, aby obliczyć udział procentowy: \n jedzenie, rozrywka, opłaty, "
                     "inne: "))

print(f"Procentowy udział kategorii {category.upper()} wynosi: {expenditures_percentage[category]:.2f}%")