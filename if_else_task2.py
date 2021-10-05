# Zadanie nr 2
# Zmodyfikuj rozwiązanie zadania z kalkulatorem wydatków z lekcji dotyczącej słownika (moduł 3).
# Pobierz te same informacje na temat miesięcznych wydatków w różnych kategoriach.
# Wypisz jednak informacje na temat procentowego udziału najbardziej znaczącej kategorii.

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
bills_percentage = float(exp_values[2] / total_expenses * 100)
other_percentage = float(exp_values[3] / total_expenses * 100)

expenditures_percentages = [
    food_percentage,
    entertainment_percentage,
    bills_percentage,
    other_percentage,
]

if max(expenditures_percentages) == food_percentage:
    print(f"Największy udział w wydatkach ma jedzenie: {food_percentage:.2f}% wszystkich wydatków")

if max(expenditures_percentages) == entertainment_percentage:
    print(f"Największy udział w wydatkach ma rozrywka: {entertainment_percentage:.2f}% wszystkich wydatków")

if max(expenditures_percentages) == bills_percentage:
    print(f"Największy udział w wydatkach mają opłaty: {bills_percentage:.2f}% wszystkich wydatków")

if max(expenditures_percentages) == other_percentage:
    print(f"Największy udział w wydatkach mają inne sprawy: {other_percentage:.2f}% wszystkich wydatków")
