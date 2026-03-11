import tkinter 
from tkinter import messagebox
from reportlab.pdfgen import canvas 
import os
import subprocess
import platform
import customtkinter

class KonfiguratorPC:
    def __init__(self, okno, dane):
        self.okno = okno
        self.dane_czesci = dane
        self.koszyk = {}

        self.okno.title("PC Order")
        self.okno.geometry("500x600")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.ekran_glowny()

    def wyczysc_okno(self):
        for widget in self.okno.winfo_children():
            widget.destroy()

    def ekran_glowny(self):
        self.wyczysc_okno()

        napisz_tytul = customtkinter.CTkLabel(self.okno, text="PC Order", font=("Arial", 22, "bold"))
        napisz_tytul.pack(pady=30)

        ramka_przyciski = customtkinter.CTkFrame(self.okno)
        ramka_przyciski.pack(pady=10)

        kategorie = list(self.dane_czesci.keys())

        for i, nazwa_kat in enumerate(kategorie):
            wybrano =  any(p['kategoria'] == nazwa_kat for p in self.koszyk.values())
            kolor_btn = "#FF9500" if nazwa_kat in self.koszyk else "#505050"

            przycisk = customtkinter.CTkButton(ramka_przyciski, text=nazwa_kat, width=22, height=2,
                                      fg_color=kolor_btn, text_color="white", font=("Arial", 10, "bold"), command=lambda k=nazwa_kat: self.ekran_producentow(k))

            przycisk.grid(row=i // 2, column=i % 2, padx=15, pady=15)

        przycisk_koszyka = customtkinter.CTkButton(self.okno, text="Finalizacja zakupy", width=30, height=2, fg_color="blue",
                                          command=self.ekran_podsumowania)    
        
        przycisk_koszyka.pack(side="bottom", pady=20)

    def ekran_producentow(self, kategoria):
        self.wyczysc_okno()
        customtkinter.CTkLabel(self.okno, text=f"Wybierz markę: {kategoria}", font=("Arial", 14)).pack(pady=20)

        marki = self.dane_czesci[kategoria].keys()

        for m in marki:
            customtkinter.CTkButton(self.okno, text=m, width=25, height=2, fg_color="#505050", text_color="white", command=lambda marka=m: self.ekran_modeli(kategoria, marka)).pack(pady=5)

        customtkinter.CTkButton(self.okno, text="Powrót", command=self.ekran_glowny).pack(pady=20)    

    def ekran_modeli(self, kategoria, grupa):
        self.aktualna_grupa = grupa
        self.wyczysc_okno()


        napis = customtkinter.CTkLabel(self.okno, text=f"Wybierz markę ({kategoria}):", font=("Arial", 14))
        napis.pack(pady=30)
        
        lista_modeli = self.dane_czesci[kategoria][grupa]
        for model in lista_modeli:
            ramka_modelu = customtkinter.CTkFrame(self.okno, border_width=1)
            ramka_modelu.pack(fill="x", padx=20, pady=5)

            ilosc = self.koszyk[model['nazwa']]['ilosc'] if model['nazwa'] in self.koszyk else 0 

            tekst = f"{model['nazwa']} - {model['cena']} zł (W koszyku: {ilosc})"
            customtkinter.CTkLabel(ramka_modelu, text=tekst).pack(side="left", padx=10)

            customtkinter.CTkButton(ramka_modelu, text="+", width=3, command=lambda m=model: self.dodaj_do_koszyka(kategoria, m, grupa)).pack(side="right", padx=2)

            customtkinter.CTkButton(ramka_modelu, text="-", width=3, command=lambda m=model: self.usun_jedna_sztuke(m['nazwa'], kategoria, grupa)).pack(side="right", padx=2)

        przycisk_powrot = customtkinter.CTkButton(self.okno, text="Cofnij", command=lambda k=kategoria : self.ekran_producentow(k))
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
        customtkinter.CTkLabel(self.okno, text="Twoja Konfiguracja", font=("Arial", 18, "bold")).pack(pady=20)

        suma_calkowita = 0 
        for nazwa, dane in self.koszyk.items():
            ilosc = dane['ilosc']
            cena_laczna = dane['cena'] * ilosc
            suma_calkowita +=  cena_laczna

            ramka_wpisu = customtkinter.CTkFrame(self.okno)
            ramka_wpisu.pack(fill="x", padx=40, pady=2)
            
            tekst = f"{dane['kategoria']}: {nazwa} x{ilosc} - {cena_laczna} zł"
            customtkinter.CTkLabel(ramka_wpisu, text=tekst, font=("Arial", 10)).pack(side="left")

            customtkinter.CTkButton(ramka_wpisu, text="X", text_color="white", fg_color="red", command=lambda n=nazwa: self.usun_z_koszyka_calkowicie(n)).pack(side="right")
            
            

        customtkinter.CTkLabel(self.okno, text=f"SUMA: {suma_calkowita} zł", font=("Arial", 18, "bold")).pack(pady=20)
        customtkinter.CTkButton(self.okno, text="Wróć do menu", command=self.ekran_glowny).pack(pady=10)
        customtkinter.CTkButton(self.okno, text="Wygeneruj PDF", fg_color="#4CAF50", text_color="white", font=("Arial", 12, "bold"), width=25, height=2, command=self.generuj_pdf).pack(pady=10)

    def generuj_pdf(self):
        try:
            nazwa_pliku = "Podsumowanie.pdf"
            c = canvas.Canvas(nazwa_pliku)

            c.setFont("Helvetica-Bold", 16)
            c.drawString(100, 800, "Konfiguracja PC")
            c.line(100, 795, 500, 795)

            c.setFont("Helvetica", 12)
            y = 760
            suma_calkowita = 0

            for nazwa, dane in self.koszyk.items():
                ilosc = dane['ilosc']
                cena_laczna = dane['cena'] * ilosc
                suma_calkowita += cena_laczna

                linia = f"- {dane['kategoria']}: {nazwa} x{ilosc} ({cena_laczna} zł)"
                c.drawString(100, y, linia)
                y -= 20

            c.line(100, y, 500, y)
            y -= 25
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, y, f"SUMA CALOKOWITA: {suma_calkowita} zł")

            c.save()

            system_op = platform.system()
            if system_op == "Windows":
                os.startfile(nazwa_pliku)
            else:
                try:
                    subprocess.run(['xdg-open', nazwa_pliku])
                except: 
                    os.system(f'xdg-open {nazwa_pliku}')        

            messagebox.showinfo("Sukces", f"Plik {nazwa_pliku} został wygenerowany")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się stworzyć PDF: {e}")        


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


root = customtkinter.CTk()
aplikacja = KonfiguratorPC(root, czesci_pc)
root.mainloop()

                   



