# Zadanie nr 1
# Zmodyfikuj rozwiązania zadań 1 i 2 z poprzedniej lekcji,
# tak aby wypisywać różne informacje w zależności od wyniku porównań.

# zadanie 1
# Zapytaj użytkownika o ceny trzech produktów
# i wypisz wyniki ich porównania.

# price1 = float(input("Wpisz cenę pierwszego produktu: "))
# price2 = float(input("Wpisz cenę drugiego produktu: "))
# price3 = float(input("Wpisz cenę trzeciego produktu: "))
# "\n"
#
# if price1 > price2:
#     print("Produkt 1 jest droższy od produktu 2")
# if price1 == price2:
#     print("Produkty 1 kosztuje tyle samo co produkt 2")
# if price1 > price3:
#     print("Produkt 1 jest droższy od produktu 3")
# if price1 == price3:
#     print("Produkty 1 kosztuje tyle samo co produkt 3")
# if price2 > price1:
#     print("Produkt 2 jest droższy od produktu 1")
# if price2 > price3:
#     print("Produkt 2 jest droższy od produktu 3")
# if price2 == price3:
#     print("Produkt 2 kosztuje tyle samo co produkt 3")
# if price3 > price1:
#     print("Produkt 3 jest droższy od produktu 1")
# if price3 > price2:
#     print("Produkt 3 jest droższy od produktu 2")

# zadanie 2
# Poproś użytkownika o wprowadzenie listy zakupów, rozdzielając poszczególne elementy przecinkiem.
# Następnie powiedz (wypisz), czy jest to według Ciebie długa lista, czy też nie.

shopping = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shopping_list = shopping.split(",")

if len(shopping_list) > 5:
    print("Wow, Twoja lista jest całkiem długa!")

else:
    print("Na szczęście Twoja lista nie jest aż tak długa!")