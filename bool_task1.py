# Zadanie nr 1
# Zapytaj użytkownika o ceny trzech produktów i wypisz wyniki ich porównania.

price1 = float(input("Wpisz cenę pierwszego produktu: "))
price2 = float(input("Wpisz cenę drugiego produktu: "))
price3 = float(input("Wpisz cenę trzeciego produktu: "))
"\n"
print(f"Czy pierwszy = drugi? {price1 == price2}")
print(f"Czy drugi = trzeci? {price2 == price3}")
print(f"Czy pierwszy = trzeci? {price1 == price3}")
