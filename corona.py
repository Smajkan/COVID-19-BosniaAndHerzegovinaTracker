import datetime
import tkinter as tk
from tkinter import messagebox, ttk
import requests


class CovidTrackerApp:
    """Modern COVID-19 tracker for Bosnia and Herzegovina."""

    API_COUNTRY = "https://disease.sh/v3/covid-19/countries/bosnia"
    API_VACCINE = (
        "https://disease.sh/v3/covid-19/vaccine/coverage/countries/"
        "bosnia?lastdays=1&fullData=true"
    )

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("COVID-19 STATISTIKA - BIH (2025)")
        self.root.geometry("540x580")
        self.root.iconbitmap("./bosniaflag.ico")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))

        header = ttk.Label(
            self.root, text="Bosnia and Herzegovina COVID-19", style="Header.TLabel"
        )
        header.pack(pady=10)

        self.data_labels: dict[str, ttk.Label] = {}
        fields = [
            "Ukupno slučajeva",
            "Ukupno preminulih",
            "Aktivnih slučajeva",
            "Oporavljenih",
            "Testiranih",
            "Vakcinisanih",
            "Preminulih danas",
            "Novi slučajevi",
            "Populacija",
        ]
        for field in fields:
            row = ttk.Frame(self.root)
            row.pack(fill="x", padx=20, pady=3)
            ttk.Label(row, text=f"{field}:").pack(side="left")
            value = ttk.Label(row, text="--", width=20)
            value.pack(side="right")
            self.data_labels[field] = value

        self.updated_label = ttk.Label(self.root, text="")
        self.updated_label.pack(pady=10)

        ttk.Button(self.root, text="Osvježi", command=self.update_data).pack(pady=10)

        self.update_data()
        messagebox.showinfo(
            "COVID-19 Tracker 2025",
            "Dobrodošli u poboljšani pregled podataka!",
        )

    def update_data(self) -> None:
        """Fetch COVID-19 data and update the labels."""
        try:
            json_data = requests.get(self.API_COUNTRY).json()
            vaccine_json = requests.get(self.API_VACCINE).json()
        except requests.RequestException as exc:  # network issues
            messagebox.showerror("Greška", f"Neuspjelo preuzimanje podataka:\n{exc}")
            return

        values = {
            "Ukupno slučajeva": json_data.get("cases"),
            "Ukupno preminulih": json_data.get("deaths"),
            "Aktivnih slučajeva": json_data.get("active"),
            "Oporavljenih": json_data.get("recovered"),
            "Testiranih": json_data.get("tests"),
            "Vakcinisanih": vaccine_json.get("timeline", [{}])[0].get("total"),
            "Preminulih danas": json_data.get("todayDeaths"),
            "Novi slučajevi": json_data.get("todayCases"),
            "Populacija": json_data.get("population"),
        }
        for field, val in values.items():
            self.data_labels[field].config(text=str(val))

        timestamp = json_data.get("updated")
        if timestamp:
            datum = datetime.datetime.fromtimestamp(timestamp / 1e3)
            self.updated_label.config(
                text=f"Ažurirano: {datum.strftime('%d.%m.%Y %H:%M')}"
            )


if __name__ == "__main__":
    ROOT = tk.Tk()
    CovidTrackerApp(ROOT)
    ROOT.mainloop()
