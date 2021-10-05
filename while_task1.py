# Zadanie nr 1
# Pytaj użytkownika o liczbę tak długo aż poda liczbę parzystą lub przekroczy limit 10 prób.

even_number = int(input("Podaj liczbę parzystą: "))
attempt = 1
is_even = ""
print("")

while even_number % 2 != 0 and attempt < 10:
    print(f"Niestety, {even_number} to nie liczba parzysta, spróbuj ponownie!")
    print(f"Masz jeszcze {10 - attempt} prób \n")
    attempt += 1
    even_number = int(input("Podaj liczbę parzystą: "))
    is_even = False

if even_number % 2 == 0:
    is_even = True
    print(f"Tak! {even_number} to liczba parzysta!")

if attempt >= 10 and is_even == False:
    print(f"Niestety, {even_number} to nie liczba parzysta!")
    print("Wyczerpałeś wszystkie próby!")
