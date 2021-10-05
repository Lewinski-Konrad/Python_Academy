# Zadanie nr 3
# Zapytaj użytkownika o jego oceny końcowe z kilku przedmiotów (matematyka, fizyka, itd.).
# Następnie, przeanalizuj je i wypisz informację czy zdał/zdała do kolejnej klasy.
# Załóż, że zdać można wtedy jeżeli nie ma się żadnej jedynki albo jeżeli ma się
# jedną jedynkę, ale średnia ze wszystkich ocen jest wyższa niż 3.5.

math_grade = int(input("Podaj ocenę końcową z matematyki: "))
polish_grade = int(input("Podaj ocenę końcową z j. polskiego: "))
english_grade = int(input("Podaj ocenę końcową z j. angielskiego: "))
physics_grade = int(input("Podaj ocenę końcową z fizyki: "))
chemistry_grade = int(input("Podaj ocenę końcową z chemii: "))

grade_average = (math_grade + polish_grade + english_grade + physics_grade + chemistry_grade) / 5

failures = 0

if math_grade == 1:
    failures = failures + 1

if polish_grade == 1:
    failures = failures + 1

if english_grade == 1:
    failures = failures + 1

if physics_grade == 1:
    failures = failures + 1

if chemistry_grade == 1:
    failures = failures + 1

if  failures != 0:
    if failures == 1 and grade_average > 3.5:
        print(f"Zdałeś/Zdałaś do kolejnej klasy ze średnią {grade_average:.2f}, pomimo oceny niedostatecznej")
    else:
        print(f"Niestety nie zdałeś/zdałaś do kolejnej klasy ze względu na oceny niedostateczne oraz średnią {grade_average:.2f}")
else:
    print(f"Zdałeś/Zdałaś do kolejnej klasy ze średnią {grade_average:.2f}!")
