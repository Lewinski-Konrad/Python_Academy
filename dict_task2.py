# Zadanie nr 2
# Stwórz zmienną my_family zawierającą drzewo genealogiczne Twojej rodziny.
# Zacznij od siebie, opisując imię, nazwisko oraz datę urodzenia każdej
# osoby oraz jej rodziców.

my_family = [
    {
        "first_name": "Konrad",
        "last_name": "Lewiński",
        "birth_date": "01.06.1999",
        "mother": {
                    "first_name": "Iwona",
                    "last_name": "Lewińska",
                    "birth_date": "11.08.1971",
                    "mother": {
                                "first_name": "Teresa",
                                "last_name": "Seler",
                                "birth_date": "11.08.1971",
                    },
                    "father": {
                                "first_name": "Andrzej",
                                "last_name": "Seler",
                                "birth_date": "18.04.1949",
                    },

        },
        "father": {
                    "first_name": "Ryszard",
                    "last_name": "Lewiński",
                    "birth_date": "11.09.1961",
                    "mother": {
                                "first_name": "Celina",
                                "last_name": "Lewińska",
                                "birth_date": "22.10.1942",
                    },
                    "father": {
                                "first_name": "Jan",
                                "last_name": "Lewiński",
                                "birth_date": "03.07.1938",
                    },

        },
     }
]

print(my_family, sep="\n")
