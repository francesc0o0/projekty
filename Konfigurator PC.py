import tkinter 

class KonfiguratorPC:
    def __init__(self, okno, dane):
        self.okno = okno
        self.dane_czesci = dane
        self.koszyk = {}

        self.okno.title("Konfigurator PC")
        self.okno.geometry("500x600")
        self.okno.configure(bg="#D3D3D3")

        self.ekran_glowny()

    def wyczysc_okno(self):
        for widget in self.okno.winfo_children():
            widget.destroy()

    def ekran_glowny(self):
        self.wyczysc_okno()

        napisz_tytul = tkinter.Label(self.okno, text="Konfigurator PC", font=("Arial", 22, "bold"), bg="#1C1C1C", fg="white")
        napisz_tytul.pack(pady=30)

        ramka_przyciski = tkinter.Frame(self.okno)
        ramka_przyciski.pack(pady=10)

        kategorie = list(self.dane_czesci.keys())

        for i, nazwa_kat in enumerate(kategorie):
            wybrano =  any(p['kategoria'] == nazwa_kat for p in self.koszyk.values())
            kolor_btn = "#FF9500" if nazwa_kat in self.koszyk else "#505050"

            przycisk = tkinter.Button(ramka_przyciski, text=nazwa_kat, width=22, height=2,
                                      bg=kolor_btn, fg="white", font=("Arial", 10, "bold"), command=lambda k=nazwa_kat: self.ekran_producentow(k))

            przycisk.grid(row=i // 2, column=i % 2, padx=15, pady=15)

        przycisk_koszyka = tkinter.Button(self.okno, text="Finalizacja zakupy", width=30, height=2, bg="lightblue",
                                          command=self.ekran_podsumowania)    
        
        przycisk_koszyka.pack(side="bottom", pady=20)

    def ekran_producentow(self, kategoria):
        self.wyczysc_okno()
        tkinter.Label(self.okno, text=f"Wybierz markę: {kategoria}", font=("Arial", 14)).pack(pady=20)

        marki = self.dane_czesci[kategoria].keys()

        for m in marki:
            tkinter.Button(self.okno, text=m, width=25, height=2, bg="#505050", fg="white", command=lambda marka=m: self.ekran_modeli(kategoria, marka)).pack(pady=5)

        tkinter.Button(self.okno, text="Powrót", command=self.ekran_glowny).pack(pady=20)    

    def ekran_modeli(self, kategoria, grupa):
        self.aktualna_grupa = grupa
        self.wyczysc_okno()


        napis = tkinter.Label(self.okno, text=f"Wybierz markę ({kategoria}):", font=("Arial", 14))
        napis.pack(pady=30)
        
        lista_modeli = self.dane_czesci[kategoria][grupa]
        for model in lista_modeli:
            ramka_modelu = tkinter.Frame(self.okno, relief="groove", borderwidth=1)
            ramka_modelu.pack(fill="x", padx=20, pady=5)

            ilosc = self.koszyk[model['nazwa']]['ilosc'] if model['nazwa'] in self.koszyk else 0 

            tekst = f"{model['nazwa']} - {model['cena']} zł (W koszyku: {ilosc})"
            tkinter.Label(ramka_modelu, text=tekst).pack(side="left", padx=10)

            tkinter.Button(ramka_modelu, text="+", width=3, command=lambda m=model: self.dodaj_do_koszyka(kategoria, m, grupa)).pack(side="right", padx=2)

            tkinter.Button(ramka_modelu, text="-", width=3, command=lambda m=model: self.usun_jedna_sztuke(m['nazwa'], kategoria, grupa)).pack(side="right", padx=2)

        przycisk_powrot = tkinter.Button(self.okno, text="Cofnij", command=lambda k=kategoria : self.ekran_producentow(k))
        przycisk_powrot.pack(pady=20) 

    def dodaj_do_koszyka(self, kategoria, dane_produktu, grupa):
        nazwa = dane_produktu['nazwa']
        if nazwa in self.koszyk:
            self.koszyk[nazwa]['ilosc'] += 1
        else:
            self.koszyk[nazwa] = {
                'kategoria': kategoria,
                'cena': dane_produktu['cena'],
                'ilosc': 1
            }    

        self.ekran_modeli(kategoria, grupa) 

    def usun_jedna_sztuke(self, nazwa_produktu, kategoria, grupa):
        if nazwa_produktu in self.koszyk:
            self.koszyk[nazwa_produktu]['ilosc'] -= 1
            if self.koszyk[nazwa_produktu]['ilosc'] <= 0:
                del self.koszyk[nazwa_produktu]
        self.ekran_modeli(kategoria, grupa)               

    def usun_z_koszyka_calkowicie(self, nazwa_produktu):
        if nazwa_produktu in self.koszyk:
            del self.koszyk[nazwa_produktu]
        self.ekran_podsumowania()        

    def ekran_podsumowania(self):
        self.wyczysc_okno()
        tkinter.Label(self.okno, text="Twoja Konfiguracja", font=("Arial", 18, "bold")).pack(pady=20)

        suma_calkowita = 0 
        for nazwa, dane in self.koszyk.items():
            ilosc = dane['ilosc']
            cena_laczna = dane['cena'] * ilosc
            suma_calkowita +=  cena_laczna

            ramka_wpisu = tkinter.Frame(self.okno)
            ramka_wpisu.pack(fill="x", padx=40, pady=2)
            
            tekst = f"{dane['kategoria']}: {nazwa} x{ilosc} - {cena_laczna} zł"
            tkinter.Label(ramka_wpisu, text=tekst, font=("Arial", 10)).pack(side="left")

            tkinter.Button(ramka_wpisu, text="X", fg="white", bg="red", command=lambda n=nazwa: self.usun_z_koszyka_calkowicie(n)).pack(side="right")
            
            

        tkinter.Label(self.okno, text=f"SUMA: {suma_calkowita} zł", font=("Arial", 18, "bold")).pack(pady=20)
        tkinter.Button(self.okno, text="Wróć do menu", command=self.ekran_glowny).pack(pady=10)

#----------LISTA CZĘŚCI------------

czesci_pc = {
    "Procesor": {
        "Intel": [{"nazwa": "Core i5-13400F", "cena":900}, {"nazwa": "Core i9-14900K", "cena":1700}],
        "AMD": [{"nazwa": "Ryzen 5 7600", "cena":850}, {"nazwa": "Ryzen 7 7800x3d", "cena":2000}]
    },
    "Płyta Główna": {
        "Msi": [{"nazwa": "B660 Tomahawk", "cena":800}],
        "Asus": [{"nazwa": "B760-plus", "cena":600}],
    },
    "Karta Graficzna": {
        "Nvdia": [{"nazwa": "Rtx 4060", "cena":1300}, {"nazwa": "Rtx 5090", "cena":13000}],
        "AMD": [{"nazwa": "RX 7700 XT", "cena":1500}, {"nazwa": "RX 9070 XT", "cena":3000}],
    },
    "Pamięć RAM": {
        "Kingston": [{"nazwa": "DDR5 16GB 6000Mhz", "cena":800}],
        "Corsair": [{"nazwa": "DDR5 32GB 6400Mhz", "cena":1600}],
    },
    "Dysk": {
        "Lexar": [{"nazwa": "980 Pro 1TB", "cena":400}],
        "Samsung": [{"nazwa": "NM790 2TB", "cena":600}],
    },
    "Zasilacz": {
        "Endorfy": [{"nazwa": "Vervo L5 600W", "cena":250}],
        "be quiet": [{"nazwa": "Pure Power 12 850W", "cena":500}, {"nazwa": "Pure Power 12 1000W", "cena":700}],
    },
    "Obudowa": {
        "NZHXT": [{"nazwa": "H9 flow", "cena":550}],
        "be quiet": [{"nazwa": "Light base 500", "cena":500}, {"nazwa": "Shadow base 802", "cena":400}]
    },
    "Chłodzenie procesora": {
        "Powietrzne": [{"nazwa": "Fera 5 Dual", "cena":150}],
        "Wodne (AIO)": [{"nazwa": "NZHXT Kraken", "cena":450}]
    }
    

}    


root = tkinter.Tk()
aplikacja = KonfiguratorPC(root, czesci_pc)
root.mainloop()

                   



