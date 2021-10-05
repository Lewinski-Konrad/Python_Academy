# Zadanie nr 3
# Zmodyfikuj program obliczający wartość lokaty, tak aby dodatkowo wypisywał informacje,
# czy w planowanym okresie łączna wartość inwestycji wzrośnie o co najmniej 10%.

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
