# Zadanie nr 1
# Zmodyfikuj zadanie, w którym pytasz użytkownika o listę zakupów i sprawdź,
# czy znajdują się na niej chleb albo bułki.

# shopping_list_input = input("Wpisz listę zakupów, oddzielając produkty przecinkiem: ")
# shopping_list = shopping_list_input.split(",")
#
# if "chleb" in shopping_list or "Chleb" in shopping_list:
#     print("Na Twojej liście znajduje się chleb!")
#
# if "bułki" in shopping_list or "Bułki" in shopping_list:
#     print("Na Twojej liście znajdują się bułki!")
#
# if "chleb" not in shopping_list and "Chleb" not in shopping_list and "bułki" not in shopping_list and "Bułki" not in shopping_list:
#     print("Na Twojej liście nie ma ani bułek, ani chleba!")

# Zadanie nr 2
# Zapytaj użytkownika o numer telefonu i sprawdź czy zawiera przynajmniej jedną cyfrę 0.

# phone_number = input("Podaj numer telefonu: ")
# if "0" in phone_number:
#     print("W Twoim numerze znajduje się 0!")
# else:
#     print("W Twoim numerze nie ma 0!")

# Zadanie nr 3
# Utwórz zmienną value oraz instrukcję warunkową, która sprawdzi czy wartość tej zmiennej jest:
#
# -True
# -False
# -None
# -inną wartością

value = 1

if value is True:
    print("value is True")
elif value is False:
    print("value is False")
elif value is None:
    print("value is None")
else:
    print("value is a different variable")