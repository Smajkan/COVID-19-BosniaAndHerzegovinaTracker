import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import requests
import datetime

# Additional modules for the refreshed look
from tkinter import messagebox

# GET METODA OVDJE:


def CovidDostaviInformacije():
    """Fetch COVID-19 data and update the labels."""
    api = 'https://disease.sh/v3/covid-19/countries/bosnia'
    vaccine_api = (
        'https://disease.sh/v3/covid-19/vaccine/coverage/countries/'
        'bosnia?lastdays=1&fullData=true'
    )

    json_data = requests.get(api).json()
    vaccine_json = requests.get(vaccine_api).json()

    ukupno_slucajeva = str(json_data['cases'])
    ukupno_mrtvih = str(json_data['deaths'])
    umrlo_danas = str(json_data['todayDeaths'])
    aktivnih = str(json_data['active'])
    novi_slucajevi = str(json_data['todayCases'])
    ukupno_oporavljenih = str(json_data['recovered'])
    testirano = str(json_data['tests'])
    populacija = str(json_data['population'])
    ukupno_vakcinisanih = str(vaccine_json['timeline'][0]['total'])
    osvjezavanje_izvresno_u = json_data['updated']
    # konvertuje u ispravno vrijeme i datum
    datum = datetime.datetime.fromtimestamp(osvjezavanje_izvresno_u/1e3)

    label.config(
        text=(
            "Ukupno slučajeva: " + ukupno_slucajeva
            + "\n" + "Ukupno preminulih: " + ukupno_mrtvih
            + "\n" + "Ukupno aktivni slučajeva: " + aktivnih
            + "\n" + "Ukupno oporavljenih: " + ukupno_oporavljenih
            + "\n" + "Testiranih: " + testirano
            + "\n" + "Ukupno vakcinisanih: " + ukupno_vakcinisanih
            + "\n" + "Preminulih danas: " + umrlo_danas
            + "\n" + "Novi slučajeva: " + novi_slucajevi
            + "\n" + "Populacija: " + populacija
        )
    )

    label3.config(text="Ažurirano: ")
    label2.config(text=datum)


# GUI ZA APLIKACIJU
canvas = tk.Tk()
canvas.geometry("500x550")
canvas.title("COVID-19 STATISTIKA - BIH (2025)")

# Apply a modern style
style = Style()
style.theme_use('clam')

# ZASTAVA BOSNE
canvas.iconbitmap(
    r'./bosniaflag.ico')
# 'C:\Users\imeusera\Desktop\ImeFolderaGdjeSteSpremiliBosniaflag.ico\bosniaflag.ico'

# font koji ćemo koristiti
f = ("Helvetica", 15, "bold")


# buttoni i labeli
button = tk.Button(canvas, font=f, text="Prikaži podatke",
                   command=CovidDostaviInformacije)
button.pack(pady=20)

# label da se pokažu podaci
label = tk.Label(canvas, font=f, justify="left")
label.pack(pady=20)


# Prije ispisa vremena
label3 = tk.Label(canvas, font=("Helvetica", 10, "bold"))
label3.pack()

# Ovdje se prikazuje vrijeme od kada su informacije
label2 = tk.Label(canvas, font=("Helvetica", 9))
label2.pack()

# Load data immediately on start
CovidDostaviInformacije()

# Show about message for 2025 update
messagebox.showinfo(
    "COVID-19 Tracker 2025",
    "Ažurirani prikaz podataka za 2025. godinu"
)

canvas.mainloop()
