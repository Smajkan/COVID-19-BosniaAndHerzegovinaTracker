import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import requests
import datetime

# GET METODA OVDJE:


def CovidDostaviInformacije():
    api = 'https://disease.sh/v3/covid-19/countries/bosnia'

    json_data = requests.get(api).json()
    ukupno_slucajeva = str(json_data['cases'])
    ukupno_mrtvih = str(json_data['deaths'])
    umrlo_danas = str(json_data['todayDeaths'])
    aktivnih = str(json_data['active'])
    ukupno_oporavljenih = str(json_data['recovered'])
    osvjezavanje_izvresno_u = json_data['updated']
    # konvertuje u ispravno vrijeme i datum
    datum = datetime.datetime.fromtimestamp(osvjezavanje_izvresno_u/1e3)

    label.config(text="Ukupno slučajeva: " + ukupno_slucajeva
                 + "\n"+"Ukupno preminulih: " + ukupno_mrtvih
                 + "\n"+"Ukupno aktivni slučajeva: " + aktivnih
                 + "\n"+"Ukupno oporavljenih: " + ukupno_oporavljenih
                 + "\n"+"Preminulih danas: " + umrlo_danas)

    label2.config(text=datum)


    # GUI ZA APLIKACIJU
canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("COVID-19 STATISTIKA - BIH")

# ZASTAVA BOSNE
canvas.iconbitmap(
    r'C:\Users\dell\Desktop\Projects\CoronaTrackerPython\bosniaflag.ico')
# 'C:\Users\imeusera\Desktop\ImeFolderaGdjeSteSpremiliBosniaflag.ico\bosniaflag.ico'

# font koji ćemo koristiti
f = ("popins", 15, "bold")

# buttoni i labeli
button = tk.Button(canvas, font=f, text="PRIKAŽI",
                   command=CovidDostaviInformacije)
button.pack(pady=20)

# label da se pokažu podaci
label = tk.Label(canvas, font=f)
label.pack(pady=20)

# Ovdje se prikazuje vrijeme od kada su informacije
label2 = tk.Label(canvas, font=8)
label2.pack()
CovidDostaviInformacije()

canvas.mainloop()
