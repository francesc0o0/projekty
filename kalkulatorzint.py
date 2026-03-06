import math
import tkinter


przyciski_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

prawo_symbols = ["÷", "×", "-", "+", "="]
gora_symbols = ["AC", "+/-", "%", "√"]

liczba_wierszy = len(przyciski_values)
liczba_column = len(przyciski_values[0])

kolor_jasnoszary = "#D4D4D2"
kolor_czarny = "#1C1C1C"
kolor_ciemnoszary = "#505050"
kolor_pomarenczowy = "#FF9500"
kolor_biały = "white"

okno = tkinter.Tk()
okno.title("Kalkulator")
okno.resizable(False, False)

ramka = tkinter.Frame(okno)
label = tkinter.Label (ramka, text="0", font=("Arial, 45"), background = kolor_czarny,
                       foreground = kolor_biały, anchor="e", width= liczba_column)


label.grid(row=0, column=0, columnspan=liczba_column, sticky="we")

for row in range(liczba_wierszy):
    for column in range(liczba_column):
        wartosc = przyciski_values[row][column]
        przycisk = tkinter.Button(ramka, text=wartosc, font=("Arial", 30),
                                  width=liczba_column-1, height=1,
                                  command=lambda wartosc=wartosc: wartosc_kliku(wartosc))
        
        if wartosc in gora_symbols:
            przycisk.config(foreground=kolor_czarny, background=kolor_jasnoszary)
        elif wartosc in prawo_symbols:
            przycisk.config(foreground=kolor_biały, background=kolor_pomarenczowy)
        else:
            przycisk.config(foreground=kolor_biały, background= kolor_ciemnoszary)    

        przycisk.grid(row=row+1, column=column )

ramka.pack()

A = "0" 
operator = None
B = None 

def reset():
    global A, B, operator
    A = "0"
    operator = None 
    B = None

def procent(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)       

def wartosc_kliku(wartosc):
    global prawo_symbols, gora_symbols, label, A, B, operator

    if wartosc in prawo_symbols:
        if wartosc == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = procent(numA + numB)
                
                elif operator == "-":
                    label["text"] = procent(numA - numB)    

                elif operator == "×":
                    label["text"] = procent(numA * numB)

                elif operator == "÷":
                    label["text"] = procent(numA / numB)

                reset()         

        elif wartosc in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

                operator = wartosc
    
    elif wartosc in gora_symbols:
        if wartosc == "AC":
            reset()
            label["text"] = "0"   

        elif wartosc == "+/-":
            wynik = float(label["text"]) * -1
            label["text"] = str(wynik)

        elif wartosc == "%":
            wynik = float(label["text"]) / 100
            label["text"] = str(wynik)

        elif wartosc == "√":
            liczba = float(label["text"])
            if liczba >= 0:
                label["text"] = str(math.sqrt(liczba))
            else: 
                label["text"] = "√ >= 0"       

    else:
        if wartosc == ".":
            if wartosc not in label["text"]:
                label["text"] += wartosc 

        elif wartosc in "0123456789":
            if label["text"] == "0":
                label["text"] = wartosc
            else:
                label["text"] += wartosc    

#Srodkowanie okna
okno.update()
okno_width = okno.winfo_width()
okno_height = okno.winfo_height()
ekran_width = okno.winfo_screenheight()
ekran_height = okno.winfo_screenheight()

okno_x = int((ekran_width/2) - (okno_width/2))
okno_y = int((ekran_height/2) - (okno_width/2))

okno.geometry(f"{okno_width}x{okno_height}+{okno_x}+{okno_y}")

#Przechwytywanie klawiatury
def klawiatura (event):
    char = event.char
    if char == "*":
        char = "×"
    if char == "/":
        char = "÷"    
    
    if char in "0123456789.+-/*×÷":
        wartosc_kliku(char)

    elif event.keysym == "Return":
        wartosc_kliku("=")

    elif event.keysym == "BackSpace":
        label["text"] = "0"

    elif event.keysym == "Escape":
        okno.destroy 

okno.bind("<Key>", klawiatura)

okno.mainloop()
