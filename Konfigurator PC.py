import tkinter 
from tkinter import messagebox
from reportlab.pdfgen import canvas 
import os
import subprocess
import platform
import customtkinter
from datetime import datetime
from PIL import Image

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

        self.iconcpu = customtkinter.CTkImage(Image.open("icons/cpu.png"), size=(40, 40))
        self.icongpu = customtkinter.CTkImage(Image.open("icons/gpu.png"), size=(40, 40))
        self.iconmotherboard = customtkinter.CTkImage(Image.open("icons/motherboard.png"), size=(40, 40))
        self.iconram = customtkinter.CTkImage(Image.open("icons/ram.png"), size=(40, 40))
        self.iconharddisk = customtkinter.CTkImage(Image.open("icons/harddisk.png"), size=(40, 40))
        self.iconpowersupply = customtkinter.CTkImage(Image.open("icons/powersupply.png"), size=(40, 40))
        self.iconcpucooler = customtkinter.CTkImage(Image.open("icons/cpucooler.png"), size=(40, 40))
        self.iconcase = customtkinter.CTkImage(Image.open("icons/case.png"), size=(40, 40))

        

        napisz_tytul = customtkinter.CTkLabel(self.okno, text="PC Order", font=("Arial", 22, "bold"))
        napisz_tytul.pack(pady=30, side="top")

        ramka_przyciski = customtkinter.CTkFrame(self.okno)
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

        przycisk_koszyka = customtkinter.CTkButton(self.okno, text="Finalizacja zakupy", width=30, height=2, fg_color="blue",
                                          command=self.ekran_podsumowania)    
        
        przycisk_koszyka.pack(side="bottom", pady=20)

    def ekran_producentow(self, kategoria):
        self.wyczysc_okno()
        
        self.logointel = customtkinter.CTkImage(Image.open("icons/intel.png"), size=(20, 20))
        self.logoamd = customtkinter.CTkImage(Image.open("icons/amd.png"), size=(20,20))
        self.logomsi = customtkinter.CTkImage(Image.open("icons/msi.png"), size=(20, 20))
        self.logoasus = customtkinter.CTkImage(Image.open("icons/asus.png"), size=(20, 20))
        self.logogigabyte = customtkinter.CTkImage(Image.open("icons/gigabyte.jpg"), size=(20, 20))
        self.logoasrock = customtkinter.CTkImage(Image.open("icons/asrock.png"), size=(20, 20))
        self.logonvidia = customtkinter.CTkImage(Image.open("icons/nvidia.png"), size=(20, 20))
        self.logoamd = customtkinter.CTkImage(Image.open("icons/amd.png"), size=(20, 20))
        self.logosapphire = customtkinter.CTkImage(Image.open("icons/gpu.png"), size=(20,20))
        self.logogainward = customtkinter.CTkImage(Image.open("icons/gpu.png"), size=(20, 20))
        self.logokingston = customtkinter.CTkImage(Image.open("icons/kingston.png"), size=(20, 20))
        self.logocorsair = customtkinter.CTkImage(Image.open("icons/corsair.jpg"), size=(20, 20))
        self.logogskill = customtkinter.CTkImage(Image.open("icons/g.skill.jpg"), size=(20, 20))
        self.logoadata = customtkinter.CTkImage(Image.open("icons/adata.png"), size=(20, 20))
        self.logolexar = customtkinter.CTkImage(Image.open("icons/lexar.png"), size=(20, 20))
        self.logosamsung = customtkinter.CTkImage(Image.open("icons/samsung.png"), size=(20, 20))
        self.logowesterndigital = customtkinter.CTkImage(Image.open("icons/westerndigital.png"), size=(20, 20))
        self.logoendorfy = customtkinter.CTkImage(Image.open("icons/endorfy.jpg"), size=(20, 20))
        self.logobequiet = customtkinter.CTkImage(Image.open("icons/bequiet.jpeg"), size=(20,20))
        self.logonzhxt = customtkinter.CTkImage(Image.open("icons/nzxt.jpg"), size=(20, 20))
        self.logolianli = customtkinter.CTkImage(Image.open("icons/lianli.jpg"), size=(20, 20))
        self.logofractaldesign = customtkinter.CTkImage(Image.open("icons/fractaldesign.jpg"), size=(20, 20))

        customtkinter.CTkLabel(self.okno, text=f"Wybierz markę: {kategoria}", font=("Arial", 14)).pack(pady=20)

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
                self.okno,
                text=m,
                image=wybrane_logo if wybrane_logo else None,
                compound="left",
                height=40, 
                width=250,
                fg_color="transparent",
                command=lambda m=m: self.ekran_modeli(kategoria, m)
            )
            przycisk.pack(pady=10)
            
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
            suma_calkowita = 0

            c.setFillColorRGB(0.1, 0.1, 0.3)
            c.rect(0, 750, 600, 100, fill=1)

            c.setFillColorRGB(1, 1, 1)
            c.setFont("Helvetica", 24)
            c.drawString(50, 790, "OFERTA KONFIGURACJI PC")

            c.setFont("Helvetica", 10)
            data_teraz = datetime.now().strftime("%d.%m.%Y %H:%M")
            c.drawRightString(550, 765, f"Data wystawienia: {data_teraz}")

            y = 700
            c.setFillColorRGB(0, 0, 0)
            c.setFont("Helvetica", 12)
            c.drawString(50, y, "Kategoria")
            c.drawString(180, y, "Wybrany model")
            c.drawRightString(550, y, "Cena")

            c.setLineWidth(1)
            c.line(50, y-5, 550, y-5)

            y -= 25
            c.setFont("Helvetica", 11)

            for kat, dane in self.koszyk.items():
                ilosc = dane.get('ilosc', 1)
                cena_jednostkowa = dane['cena']
                cena_laczna = cena_jednostkowa * ilosc

                c.drawString(50, y, f"{dane['kategoria']}")
                c.drawString(180, y, f"{kat} (x{ilosc})")
                c.drawRightString(550, y, f"{cena_laczna} zl")

                suma_calkowita += cena_laczna
                y -= 20 

                c.setStrokeColorRGB(0.8, 0.8, 0.8)
                c.line(50, y+15, 550, y+15)
                c.setStrokeColorRGB(0, 0, 0)

            y -= 30
            c.setFillColorRGB(0.95, 0.95, 0.95)
            c.rect(350, y-15, 200, 40, fill=1)
            
            c.setFillColorRGB(0, 0, 0)
            c.setFont("Helvetica", 14)
            c.drawString(360, y, "Suma:")
            c.drawRightString(540, y, f"{suma_calkowita} zl")

            c.setFont("Helvetica", 8)
            c.drawCentredString(300, 50, "Dziekuje za skorzystanie z PC Order")

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
        "Intel": [
            {"nazwa": "Core i3-14100F", "cena": 550},
            {"nazwa": "Core i5-13400F", "cena": 900}, 
            {"nazwa": "Core i5-14600K", "cena": 1350},
            {"nazwa": "Core i7-14700K", "cena": 1850},
            {"nazwa": "Core i9-14900K", "cena": 2600}
        ],
        "AMD": [
            {"nazwa": "Ryzen 5 5600", "cena": 500},
            {"nazwa": "Ryzen 5 7600", "cena": 850}, 
            {"nazwa": "Ryzen 7 7700X", "cena": 1300},
            {"nazwa": "Ryzen 7 7800x3d", "cena": 2000},
            {"nazwa": "Ryzen 9 7950X3D", "cena": 2700}
        ]
    },
    "Płyta Główna": {
        "Msi": [
            {"nazwa": "A520M-A PRO", "cena": 300},
            {"nazwa": "B660 Tomahawk", "cena": 800},
            {"nazwa": "MAG B650 TOMAHAWK WIFI", "cena": 950},
            {"nazwa": "MPG Z790 EDGE WIFI", "cena": 1500},
            {"nazwa": "MEG Z790 GODLIKE", "cena": 5000}
        ],
        "Asus": [
            {"nazwa": "PRIME H610M-K", "cena": 350},
            {"nazwa": "B760-plus", "cena": 600},
            {"nazwa": "TUF GAMING B650-PLUS", "cena": 900},
            {"nazwa": "ROG STRIX Z790-F GAMING", "cena": 1800},
            {"nazwa": "ROG MAXIMUS Z790 HERO", "cena": 2900}
        ],
        "Gigabyte": [
            {"nazwa": "B550M DS3H", "cena": 400},
            {"nazwa": "B650 GAMING X AX", "cena": 850},
            {"nazwa": "B760 AORUS ELITE AX", "cena": 1000},
            {"nazwa": "Z790 AORUS MASTER", "cena": 2200},
            {"nazwa": "X670E AORUS XTREME", "cena": 3200}
        ],
        "ASRock": [
            {"nazwa": "B660M Pro RS", "cena": 500},
            {"nazwa": "B650 Pro RS", "cena": 800},
            {"nazwa": "Z790 Steel Legend", "cena": 1200},
            {"nazwa": "X670E Taichi", "cena": 2300}
        ]
    },
    "Karta Graficzna": {
        "Nvdia": [
            {"nazwa": "Rtx 4060", "cena": 1300}, 
            {"nazwa": "Rtx 4070 Super", "cena": 2700},
            {"nazwa": "Rtx 4080 Super", "cena": 4600},
            {"nazwa": "Rtx 4090", "cena": 8500},
            {"nazwa": "Rtx 5090", "cena": 13000}
        ],
        "AMD": [
            {"nazwa": "RX 7600", "cena": 1200},
            {"nazwa": "RX 7700 XT", "cena": 1500}, 
            {"nazwa": "RX 7800 XT", "cena": 2200},
            {"nazwa": "RX 7900 XTX", "cena": 4300},
            {"nazwa": "RX 9070 XT", "cena": 3000}
        ],
        "Sapphire": [
            {"nazwa": "RX 7600 Pulse", "cena": 1250},
            {"nazwa": "RX 7800 XT Pure", "cena": 2350},
            {"nazwa": "RX 7900 GRE Nitro+", "cena": 2800},
            {"nazwa": "RX 7900 XTX Vapor-X", "cena": 4800}
        ],
        "Gainward": [
            {"nazwa": "RTX 4060 Ghost", "cena": 1250},
            {"nazwa": "RTX 4070 Super Ghost", "cena": 2650},
            {"nazwa": "RTX 4070 Ti Super Panther", "cena": 3700},
            {"nazwa": "RTX 4080 Super Phoenix", "cena": 4500}
        ]
    },
    "Pamięć RAM": {
        "Kingston": [
            {"nazwa": "DDR4 16GB 3600Mhz", "cena": 200},
            {"nazwa": "DDR5 16GB 6000Mhz", "cena": 800},
            {"nazwa": "FURY Beast 32GB 6000Mhz", "cena": 500},
            {"nazwa": "FURY Renegade 64GB 6000Mhz", "cena": 1100}
        ],
        "Corsair": [
            {"nazwa": "Vengeance LPX 16GB 3600Mhz", "cena": 220},
            {"nazwa": "Vengeance RGB 32GB 6000Mhz", "cena": 550},
            {"nazwa": "DDR5 32GB 6400Mhz", "cena": 1600},
            {"nazwa": "Dominator Titanium 64GB 7200Mhz", "cena": 1800}
        ],
        "G.Skill": [
            {"nazwa": "Ripjaws V 16GB 3600Mhz", "cena": 210},
            {"nazwa": "Flare X5 32GB 6000Mhz", "cena": 520},
            {"nazwa": "Trident Z5 RGB 32GB 6400Mhz", "cena": 650},
            {"nazwa": "Trident Z5 Neo 64GB 6000Mhz", "cena": 1050}
        ],
        "ADATA": [
            {"nazwa": "XPG Spectrix 16GB 3600Mhz", "cena": 230},
            {"nazwa": "XPG Lancer 32GB 6000Mhz", "cena": 540},
            {"nazwa": "XPG Lancer RGB 32GB 7200Mhz", "cena": 750}
        ]
    },
    "Dysk": {
        "Lexar": [
            {"nazwa": "NM620 1TB", "cena": 250},
            {"nazwa": "NM710 1TB", "cena": 300},
            {"nazwa": "980 Pro 1TB", "cena": 400},
            {"nazwa": "NM790 2TB", "cena": 600},
            {"nazwa": "NM790 4TB", "cena": 1100}
        ],
        "Samsung": [
            {"nazwa": "980 500GB", "cena": 200},
            {"nazwa": "NM790 2TB", "cena": 600},
            {"nazwa": "990 PRO 1TB", "cena": 450},
            {"nazwa": "990 PRO 2TB", "cena": 800},
            {"nazwa": "990 PRO 4TB", "cena": 1500}
        ],
        "Western Digital": [
            {"nazwa": "WD Blue SN580 1TB", "cena": 280},
            {"nazwa": "WD Black SN770 1TB", "cena": 350},
            {"nazwa": "WD Black SN850X 2TB", "cena": 750},
            {"nazwa": "WD Black SN850X 4TB", "cena": 1400}
        ]
    },
    "Zasilacz": {
        "Endorfy": [
            {"nazwa": "Vervo L5 600W", "cena": 250},
            {"nazwa": "Vero M5 700W", "cena": 320},
            {"nazwa": "Supremo FM5 750W", "cena": 420},
            {"nazwa": "Supremo FM5 850W", "cena": 480},
            {"nazwa": "Supremo FM5 1000W", "cena": 650}
        ],
        "be quiet": [
            {"nazwa": "System Power 10 600W", "cena": 280},
            {"nazwa": "Pure Power 12 750W", "cena": 450},
            {"nazwa": "Pure Power 12 850W", "cena": 500}, 
            {"nazwa": "Pure Power 12 1000W", "cena": 700},
            {"nazwa": "Dark Power 13 1200W", "cena": 1300}
        ],
        "Corsair": [
            {"nazwa": "CV650 650W", "cena": 300},
            {"nazwa": "RM750e 750W", "cena": 500},
            {"nazwa": "RM850x Shift", "cena": 700},
            {"nazwa": "HX1200 1200W", "cena": 1100},
            {"nazwa": "AX1600i 1600W", "cena": 2500}
        ]
    },
    "Obudowa": {
        "NZHXT": [
            {"nazwa": "H5 Flow", "cena": 400},
            {"nazwa": "H7 Flow", "cena": 550},
            {"nazwa": "H9 flow", "cena": 750},
            {"nazwa": "H9 Elite", "cena": 1100}
        ],
        "be quiet": [
            {"nazwa": "Pure Base 500", "cena": 320},
            {"nazwa": "Pure Base 500DX", "cena": 450},
            {"nazwa": "Shadow base 802", "cena": 400},
            {"nazwa": "Light base 500", "cena": 500},
            {"nazwa": "Dark Base Pro 901", "cena": 1400}
        ],
        "Lian Li": [
            {"nazwa": "Lancool 216", "cena": 450},
            {"nazwa": "O11 Dynamic Mini", "cena": 600},
            {"nazwa": "O11 Dynamic EVO", "cena": 850},
            {"nazwa": "O11 Vision", "cena": 900}
        ],
        "Fractal Design": [
            {"nazwa": "Pop Air", "cena": 380},
            {"nazwa": "Meshify 2 Compact", "cena": 550},
            {"nazwa": "North", "cena": 700},
            {"nazwa": "Torrent", "cena": 900}
        ]
    },
    "Chłodzenie procesora": {
        "Powietrzne": [
            {"nazwa": "Spartan 5", "cena": 80},
            {"nazwa": "Fera 5 Dual", "cena": 150},
            {"nazwa": "Fortis 5 Dual", "cena": 220},
            {"nazwa": "Deepcool AK620", "cena": 320},
            {"nazwa": "Noctua NH-D15", "cena": 520}
        ],
        "Wodne (AIO)": [
            {"nazwa": "Endorfy Navis F240", "cena": 350},
            {"nazwa": "Arctic Liquid Freezer III 240", "cena": 380},
            {"nazwa": "Arctic Liquid Freezer III 360", "cena": 450},
            {"nazwa": "NZHXT Kraken", "cena": 650},
            {"nazwa": "NZXT Kraken Elite 360", "cena": 1200}
        ]
    }
    

}    


root = customtkinter.CTk()
aplikacja = KonfiguratorPC(root, czesci_pc)
root.mainloop()

                   



