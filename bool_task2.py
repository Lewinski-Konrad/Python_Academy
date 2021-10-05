# Zadanie nr 2
# Poproś użytkownika o wprowadzenie listy zakupów, rozdzielając poszczególne elementy przecinkiem.
# Następnie powiedz (wypisz), czy jest to według Ciebie długa lista, czy też nie.

shopping = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shopping_list = shopping.split(",")

print(f"Czy lista jest długa? {len(shopping_list) > 5}")