import math 

while True:
    print("KALKULATOR")

    print("1.Dodawanie")

    print("2.Odejmowanie")

    print("3.Mnożenie")

    print("4.Dzielenie")

    print("5.Potęgowanie")

    print("6.Pierwiastkowanie")

    print("7.Wyjście")

    dzialanie = input("Wybierz jakie działanie: ") 

    if dzialanie == "7":
        print("Koniec pracy Kalkulatora")
        break

    if dzialanie == "6":
        a = float(input("Podaj liczbę do pierwiastkowania: "))
        if a >= 0:
            print("Wynik √a =", math.sqrt(a))
        else:
            print("Nie można pierwiastkować liczb ujemnych ")
        continue

    a = float(input("Podaj pierwszą liczbe: "))

    b = float(input("Podaj drugą liczbę: "))

    if dzialanie == "1":
        print("a + b =", a+b)

    elif dzialanie == "2":
        print("a - b =", a-b)

    elif dzialanie == "3":
        print("a * b =", a*b)   

    elif dzialanie == "4":
        if b != 0:
            print("a / b =", a/b)
        else:
            print("Błąd: Nie można dzielić przez zero")

    elif dzialanie == "5":
        print("a ** b =", a**b)

    else:
        print("Nie ma takiego działania")

    input("Nacisnij Enter by kontunuować:")                         


    




