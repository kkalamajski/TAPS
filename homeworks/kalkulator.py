def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz operację(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if choice == '1':
            print('Suma = ', add(num1, num2))
        elif choice == '2':
            print('Różnica = ', subtract(num1, num2))
        elif choice == '3':
            print('Iloczyn = ', multiply(num1, num2))
        elif choice == '4':
            if num2 == 0:
                print('Nie mozna dzielic przez zero!')
            else:
                print('Iloraz = ', divide(num1, num2))

    else:
        print("Błędna wartość, podaj poprawną")