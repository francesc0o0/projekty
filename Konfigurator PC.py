import tkinter 
from tkinter import messagebox
from reportlab.pdfgen import canvas 
import os
import subprocess
import platform
import customtkinter
from datetime import datetime
from PIL import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from bazakomponentow import czesci_pc

class KonfiguratorPC(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.koszyk = {}
        
        self.dane_czesci = czesci_pc
        
        self.title("PC Order")
        self.geometry("500x600")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.ekran_glowny()

        

    def wyczysc_okno(self):
        for widget in self.winfo_children():
            widget.destroy()

    def ekran_glowny(self):
        self.wyczysc_okno()

        self.iconcpu = customtkinter.CTkImage(Image.open("icons/cpu.png"), size=(40, 40))
        self.icongpu = customtkinter.CTkImage(Image.open("icons/gpu.png"), size=(40, 40))
        self.iconmotherboard = customtkinter.CTkImage(Image.open("icons/motherboard.png"), size=(40, 40))
        self.iconram = customtkinter.CTkImage(Image.open("icons/ram.png"), size=(40, 40))
        self.iconharddisk = customtkinter.CTkImage(Image.open("icons/harddisk.png"), size=(40, 40))
        self.iconpowersupply = customtkinter.CTkImage(Image.open("icons/powersupply.png"), size=(40, 40))
        self.iconcpucooler = customtkinter.CTkImage(Image.open("icons/cpucooler.png"), size=(40, 40))
        self.iconcase = customtkinter.CTkImage(Image.open("icons/case.png"), size=(40, 40))

        

        napisz_tytul = customtkinter.CTkLabel(self, text="PC Order", font=("Arial", 22, "bold"))
        napisz_tytul.pack(pady=30, side="top")

        ramka_przyciski = customtkinter.CTkFrame(self)
        ramka_przyciski.pack(side="top", pady=10, fill="both")

        kategorie = list(self.dane_czesci.keys())

        mapa_ikon = {
            "Procesor": self.iconcpu,
            "Karta Graficzna": self.icongpu,
            "Płyta Główna": self.iconmotherboard,
            "Pamięć RAM": self.iconram,
            "Dysk": self.iconharddisk,
            "Zasilacz": self.iconpowersupply,
            "Chłodzenie procesora": self.iconcpucooler,
            "Obudowa": self.iconcase,
        }

        for i, nazwa_kat in enumerate(kategorie):
            wybrano =  any(p['kategoria'] == nazwa_kat for p in self.koszyk.values())
            
            ikona = mapa_ikon.get(nazwa_kat)

            przycisk =customtkinter.CTkButton(
                ramka_przyciski,
                text=f" {nazwa_kat}",
                image=ikona,
                compound="left",
                anchor="w",
                width=160,
                height=50,
                fg_color="transparent",
                text_color="white",
                font=("Arial", 14, "bold"),
                command=lambda k=nazwa_kat: self.ekran_producentow(k)
            )

            przycisk.grid(row=i // 2, column = i % 2, padx=15, pady=15)

        przycisk_koszyka = customtkinter.CTkButton(self, text="Finalizacja zakupy", width=100, height=8, fg_color="blue",
                                          command=self.ekran_podsumowania)    
        
        przycisk_koszyka.pack(side="bottom", pady=20)

        self.btn_ustawienia = customtkinter.CTkButton(
            self, text="Ustawienia", command=self.ekran_ustawien, fg_color="#4A4A4A"
        )
        self.btn_ustawienia.pack(pady=10)

    def ekran_producentow(self, kategoria):
        self.wyczysc_okno()
        
        self.logointel = customtkinter.CTkImage(Image.open("icons/intel.png"), size=(42, 42))
        self.logoamd = customtkinter.CTkImage(Image.open("icons/amd.png"), size=(42, 42))
        self.logomsi = customtkinter.CTkImage(Image.open("icons/msi.png"), size=(42, 42))
        self.logoasus = customtkinter.CTkImage(Image.open("icons/asus.png"), size=(42, 42))
        self.logogigabyte = customtkinter.CTkImage(Image.open("icons/gigabyte.jpg"), size=(42, 42))
        self.logoasrock = customtkinter.CTkImage(Image.open("icons/asrock.png"), size=(42, 42))
        self.logonvidia = customtkinter.CTkImage(Image.open("icons/nvidia.png"), size=(42, 42))
        self.logoamd = customtkinter.CTkImage(Image.open("icons/amd.png"), size=(42, 42))
        self.logosapphire = customtkinter.CTkImage(Image.open("icons/gpu.png"), size=(42,42))
        self.logogainward = customtkinter.CTkImage(Image.open("icons/gpu.png"), size=(42, 42))
        self.logokingston = customtkinter.CTkImage(Image.open("icons/kingston.png"), size=(42, 42))
        self.logocorsair = customtkinter.CTkImage(Image.open("icons/corsair.jpg"), size=(42, 42))
        self.logogskill = customtkinter.CTkImage(Image.open("icons/g.skill.jpg"), size=(42, 42))
        self.logoadata = customtkinter.CTkImage(Image.open("icons/adata.png"), size=(42, 42))
        self.logolexar = customtkinter.CTkImage(Image.open("icons/lexar.png"), size=(42, 42))
        self.logosamsung = customtkinter.CTkImage(Image.open("icons/samsung.png"), size=(42, 42))
        self.logowesterndigital = customtkinter.CTkImage(Image.open("icons/westerndigital.png"), size=(42, 42))
        self.logoendorfy = customtkinter.CTkImage(Image.open("icons/endorfy.jpg"), size=(42, 42))
        self.logobequiet = customtkinter.CTkImage(Image.open("icons/bequiet.jpeg"), size=(42, 42))
        self.logonzhxt = customtkinter.CTkImage(Image.open("icons/nzxt.jpg"), size=(42, 42))
        self.logolianli = customtkinter.CTkImage(Image.open("icons/lianli.jpg"), size=(42, 42))
        self.logofractaldesign = customtkinter.CTkImage(Image.open("icons/fractaldesign.jpg"), size=(42, 42))

        customtkinter.CTkLabel(self, text=f"Wybierz markę: {kategoria}", font=("Arial", 14)).pack(pady=20)

        marki = self.dane_czesci[kategoria].keys()

        mapa_logo = {
            "Intel":self.logointel,
            "AMD": self.logoamd,
            "Msi": self.logomsi,
            "Asus": self.logoasus,
            "Gigabyte": self.logogigabyte,
            "ASRock": self.logoasrock,
            "Nvdia": self.logonvidia,
            "Sapphire": self.logosapphire,
            "Gainward": self.logogainward,
            "Kingston": self.logokingston,
            "Corsair": self.logocorsair,
            "G.Skill": self.logogskill,
            "ADATA": self.logoadata,
            "Lexar": self.logolexar,
            "Samsung": self.logosamsung,
            "Western Digital": self.logowesterndigital,
            "Endorfy": self.logoendorfy,
            "be quiet": self.logobequiet,
            "NZHXT": self.logonzhxt,
            "Lian Li": self.logolianli,
            "Fractal Design": self.logofractaldesign
        }

        for m in marki:
            wybrane_logo = mapa_logo.get(m)

            przycisk = customtkinter.CTkButton(
                self,
                text=m,
                image=wybrane_logo if wybrane_logo else None,
                compound="left",
                height=40, 
                width=250,
                fg_color="transparent",
                command=lambda m=m: self.ekran_modeli(kategoria, m)
            )
            przycisk.pack(pady=10)
            
        customtkinter.CTkButton(self, text="Powrót", command=self.ekran_glowny).pack(pady=20)    

    def ekran_modeli(self, kategoria, grupa):
        self.aktualna_grupa = grupa
        self.wyczysc_okno()


        napis = customtkinter.CTkLabel(self, text=f"Wybierz markę ({kategoria}):", font=("Arial", 14))
        napis.pack(pady=30)
        
        lista_modeli = self.dane_czesci[kategoria][grupa]
        for model in lista_modeli:
            ramka_modelu = customtkinter.CTkFrame(self, border_width=1)
            ramka_modelu.pack(fill="x", padx=20, pady=5)

            ilosc = self.koszyk[model['nazwa']]['ilosc'] if model['nazwa'] in self.koszyk else 0 

            tekst = f"{model['nazwa']} - {model['cena']} zł (W koszyku: {ilosc})"
            customtkinter.CTkLabel(ramka_modelu, text=tekst).pack(side="left", padx=10)

            customtkinter.CTkButton(ramka_modelu, text="+", width=3, command=lambda m=model: self.dodaj_do_koszyka(kategoria, m, grupa)).pack(side="right", padx=2)

            customtkinter.CTkButton(ramka_modelu, text="-", width=3, command=lambda m=model: self.usun_jedna_sztuke(m['nazwa'], kategoria, grupa)).pack(side="right", padx=2)

        przycisk_powrot = customtkinter.CTkButton(self, text="Cofnij", command=lambda k=kategoria : self.ekran_producentow(k))
        przycisk_powrot.pack(pady=20) 

    def dodaj_do_koszyka(self, kategoria, dane_produktu, grupa):
        nazwa = dane_produktu['nazwa']
        if nazwa in self.koszyk:
            self.koszyk[nazwa]['ilosc'] += 1
        else:
            self.koszyk[nazwa] = {
                'nazwa': nazwa,
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

    def ekran_ustawien(self):
        self.wyczysc_okno()

        customtkinter.CTkLabel(self, text="Dodaj podzespół", font=("Arial", 20)).pack(pady=15)

        kategorie = list(self.dane_czesci.keys())
        self.wybrana_kat = customtkinter.StringVar(value=kategorie[0])

        customtkinter.CTkLabel(self, text="Wybierz kategorię:").pack()
        self.menu_kat = customtkinter.CTkOptionMenu(self, values=kategorie, variable= self.wybrana_kat)
        self.menu_kat.pack(pady=10)

        self.entry_marka = customtkinter.CTkEntry(self, placeholder_text="Marka")
        self.entry_marka.pack(pady=10)

        self.entry_nazwa = customtkinter.CTkEntry(self, placeholder_text="Nazwa modelu")
        self.entry_nazwa.pack(pady=10)

        self.entry_cena  = customtkinter.CTkEntry(self, placeholder_text="Cena")
        self.entry_cena.pack(pady=10)

        customtkinter.CTkButton(self, text="Zapisz w bazie danych", command=self.dodaj_czesc).pack(pady=15)
        customtkinter.CTkButton(self, text="Wróć", command=self.ekran_glowny, fg_color="transparent", border_width=1).pack()

    def dodaj_czesc(self):
        kat = self.wybrana_kat.get()
        marka = self.entry_marka.get().strip()
        nazwa = self.entry_nazwa.get().strip()
        cena = self.entry_cena.get().strip()

        if all([marka, nazwa, cena]):
            try:
                cena_int = int(cena)

                if marka not in self.dane_czesci[kat]:
                    self.dane_czesci[kat][marka] = []

                self.dane_czesci[kat][marka].append({"nazwa": nazwa, "cena": cena_int})

                messagebox.showinfo("Sukces", f"Dodano {nazwa} do katgorii {kat}")
                self.ekran_ustawien()

            except ValueError:
                messagebox.showerror("Błąd", "Cena musi być liczbą całkowitą!")
        else:
            messagebox.showwarning("Pole puste", "Proszę wypełnić wszystkie pola.")                               

    def ekran_podsumowania(self):
        self.wyczysc_okno()
        customtkinter.CTkLabel(self, text="Twoja Konfiguracja", font=("Arial", 18, "bold")).pack(pady=20)

        suma_calkowita = 0 
        for nazwa, dane in self.koszyk.items():
            ilosc = dane['ilosc']
            cena_laczna = dane['cena'] * ilosc
            suma_calkowita +=  cena_laczna

            ramka_wpisu = customtkinter.CTkFrame(self)
            ramka_wpisu.pack(fill="x", padx=40, pady=2)
            
            tekst = f"{dane['kategoria']}: {nazwa} x{ilosc} - {cena_laczna} zł"
            customtkinter.CTkLabel(ramka_wpisu, text=tekst, font=("Arial", 10)).pack(side="left")

            customtkinter.CTkButton(ramka_wpisu, text="X", text_color="white", fg_color="red", command=lambda n=nazwa: self.usun_z_koszyka_calkowicie(n)).pack(side="right")
            
            

        customtkinter.CTkLabel(self, text=f"SUMA: {suma_calkowita} zł", font=("Arial", 18, "bold")).pack(pady=20)
        customtkinter.CTkButton(self, text="Wróć do menu", command=self.ekran_glowny).pack(pady=10)
        customtkinter.CTkButton(self, text="Wygeneruj PDF", fg_color="#4CAF50", text_color="white", font=("Arial", 12, "bold"), width=25, height=2, command=self.generuj_pdf).pack(pady=10)

    def generuj_pdf(self):
        pdfmetrics.registerFont(TTFont('Roboto-Regular', 'Roboto-Regular.ttf'))

        
        try:
            nazwa_pliku = "Podsumowanie.pdf"
            c = canvas.Canvas(nazwa_pliku)
            suma_calkowita = 0

            c.setFillColorRGB(0.1, 0.1, 0.3)
            c.rect(0, 750, 600, 100, fill=1)

            try:
                c.drawImage("icons/logo.png", 10, 730, width=120, height=120, mask='auto')
            except Exception as e:
                print(f"Błąd logo: {e}")    

            c.setFillColorRGB(1, 1, 1)
            c.setFont("Roboto-Regular", 24)
            c.drawString(120, 790, "OFERTA KONFIGURACJI PC")

            c.setFont("Roboto-Regular", 10)
            data_teraz = datetime.now().strftime("%d.%m.%Y %H:%M")
            c.drawRightString(550, 765, f"Data wystawienia: {data_teraz}")

            y = 700
            c.setFillColorRGB(0, 0, 0)
            c.setFont("Roboto-Regular", 12)
            c.drawString(50, y, "Kategoria")
            c.drawString(180, y, "Wybrany model")
            c.drawRightString(550, y, "Cena")

            c.setLineWidth(1)
            c.line(50, y-5, 550, y-5)

            y -= 25
            c.setFont("Roboto-Regular", 11)

            for kat, dane in self.koszyk.items():
                ilosc = dane.get('ilosc', 1)
                cena_jednostkowa = dane['cena']
                cena_laczna = cena_jednostkowa * ilosc

                c.drawString(50, y, f"{dane['kategoria']}")
                c.drawString(180, y, f"{kat} (x{ilosc})")
                c.drawRightString(550, y, f"{cena_laczna} zł")

                suma_calkowita += cena_laczna
                y -= 20 

                c.setStrokeColorRGB(0.8, 0.8, 0.8)
                c.line(50, y+15, 550, y+15)
                c.setStrokeColorRGB(0, 0, 0)

            y -= 30
            c.setFillColorRGB(0.95, 0.95, 0.95)
            c.rect(350, y-15, 200, 40, fill=1)
            
            c.setFillColorRGB(0, 0, 0)
            c.setFont("Roboto-Regular", 14)
            c.drawString(360, y, "Suma:")
            c.drawRightString(540, y, f"{suma_calkowita} zł")

            c.setFont("Roboto-Regular", 8)
            c.drawCentredString(300, 50, "Dziękuje za skorzystanie z PC Order")

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

       

if __name__ == "__main__":
    aplikacja = KonfiguratorPC()
    aplikacja.mainloop()

                   



