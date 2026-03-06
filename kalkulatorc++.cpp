#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main() {
    string dzialanie;
    float a, b;

    while (true) {
        cout << "---Kalkulator---" << endl;
        cout << "1.Dodawanie" << endl;
        cout << "2.Odejmowanie" << endl;
        cout << "3.Mnożenie" << endl;
        cout << "4.Dzielenie" << endl;
        cout << "5.Potęgowanie" << endl;
        cout << "6.Pierwiastkowanie" << endl;
        cout << "7.Wyjście" << endl;

        cout << "Wybierz działanie: ";
        cin >> dzialanie;

        if (dzialanie == "7") {
            cout << "Koniec pracy kalkulatora";
            break;
        }

        if (dzialanie == "6") {
            cout << "Podaj liczbę do pierwiastkowania: ";
            cin >> a;
            if (a >= 0){
                cout << "Wynik: " << sqrt(a) << endl;
            } else {
                cout << "Nie można pierwiastkować liczb ujemnych!" << endl;
            }
            continue;
        }


        cout << "Podaj pierwszą liczbę: " << endl;
        cin >> a;
        cout << "Podaj drugą liczbę: " << endl;
        cin >> b;

        if (dzialanie == "1") {
            cout << "a + b = " << a + b << endl;
        }
        else if (dzialanie == "2") {
            cout << "a -b = " << a - b << endl;
        }
        else if (dzialanie == "3") {
            cout << "a * b = " << a * b << endl;
        }
        else if (dzialanie == "4") {
            cout << "a / b = " << a / b << endl;
        }
        else if (dzialanie == "5") {
            cout << "a ** b = " << pow(a, b) << endl;
        }
        else {
            cout << "Nie ma takiego działania" << endl;
        }

        cout << "\nNacisnij Enter, aby kontynuować...";
        cin.ignore();
        cin.get();
    }
    return 0;
}