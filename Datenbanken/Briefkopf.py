"""
Moin! 

Die vorliegende Anwendung ist noch nicht restlos ausprogramiert
Auf jeden Fall fehlt noch bei der Übertragung einer CSV Datei in die Datenbank
die Prüfung, ob der Datensatz schon vorhanden ist, um Duplikate zu vermeiden.

Es fehlen auch die Funktionen:
- Anlegen eines Einzeldatensatzes
- Rücksichern der Daten in eine CSV Datei

Aber ihr seid ja schlau und könnt das ggf. selbst ergänzen
"""


import tkinter as tk
import sqlite3
from tkinter import filedialog

# Festlegen des Pfades zur Datenbank
db_name = filedialog.askopenfilename()
# Alternativ:
#db_name = "Adressen.db"

# Verbindung zur Datenbank wird aufgebaut
def connect_to_database():
    """Verbindung zur SQLite-Datenbank herstellen."""
    conn = sqlite3.connect(db_name)
    return conn

# Tabelle wird in DB angelegt
def create_table():
    """Tabelle erstellen, wenn sie nicht existiert."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_personen 
                   (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Vorname TEXT,                    
                    Nachname TEXT,
                    Strasse TEXT,
                    Hausnummer TEXT,
                    PLZ TEXT,
                    Stadt TEXT)""")
    conn.commit()
    conn.close()

# Daten werden aus der DB gelesen
def read_data():
    """Daten aus der Tabelle lesen und zurückgeben."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tbl_personen')
    data = cursor.fetchall()
    conn.close()
    return data

# Listbox wird mit den Datensätzen gefüllt
def lbx_fill():
    data = read_data()
    for entry in data:
        lbx.insert("end", f"{entry[0]}, {entry[1]},{entry[2]},{entry[3]},{entry[4]},{entry[5]},{entry[6]}")

# Beim Klicken auf einen Listbox- Eintrag wird der Text dses Labels angepasst
def on_lbx_select(event):
    # Index des ausgewählten Elements abrufen
    selected_index = lbx.curselection()
    if selected_index:
        # Ausgewähltes Element abrufen
        selected_item = list(str(lbx.get(selected_index)).split(","))
        lblText = f"{selected_item[1]} {selected_item[2]}\n{selected_item[5]} {selected_item[6]}\n{selected_item[3]} {selected_item[4]}"
        lbl_adr.configure(text=lblText, font='Helvetia')

# Speichert den Labeltext in der Zwischenablage
def btnClip():
    lbl_adr.clipboard_clear()
    lbl_adr.clipboard_append(lbl_adr.cget('text'))

# Lädt die Daten eines CSV in die Datenbank
def btnCSV():
    from tkinter import filedialog
    import csv
    csv_path=filedialog.askopenfilename(filetypes=(("CSV", "*.csv"), ("Text", "*.txt")))
    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=["Vorname", "Nachname", "Strasse", "Hausnummer", "PLZ", "Stadt"])
        data = [row for row in reader]
        data.pop(0)
    conn = connect_to_database()
    cursor = conn.cursor()
    for row in data:
        cursor.execute('''
            INSERT INTO tbl_personen (Vorname, Nachname, Strasse, Hausnummer, PLZ, Stadt)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (row["Vorname"], row["Nachname"], row["Strasse"], row["Hausnummer"], row["PLZ"], row["Stadt"]))

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
    lbx_fill()

# Soll einen neuen einzelnen DB Eintrag anlegen
# , ist aber noch nicht ausprogrammiert und öffnet bislang nur
# ein neues Fenster
def btn_new_entry():
    # Neues Fenster erstellen
    new_window = tk.Toplevel(app)
    new_window.title("Neuer Eintrag")

    # Label im neuen Fenster hinzufügen
    label = tk.Label(new_window, text="Neuer Eintrag hier")
    label.pack(padx=10, pady=10)


# Grafische Anwendung startet
app = tk.Tk()
app.geometry("800x400")
app.configure(bg='#e9d9bd')

# create widgets

# Listbox
lbx = tk.Listbox(master=app)
lbx_fill()
lbx.bind("<<ListboxSelect>>", on_lbx_select)

# Die anderen Elemente
btn_new = tk.Button(master=app, text="Neuer Eintrag", command=btn_new_entry)
btn_csv = tk.Button(master=app, text="Neu aus CSV", command=btnCSV)
lbl_adr = tk.Label(master=app)
btn_clip = tk.Button(master=app, text="In Zwischenablage kopieren", command=btnClip)

# place widgets

lbx.place(relx=0.05, rely=0.05, relheight=0.75, relwidth=0.50)
btn_new.place(relx=0.60, rely=0.05, relheight=0.05, relwidth=0.35)
btn_csv.place(relx=0.60, rely=0.15, relheight=0.05, relwidth=0.35)
lbl_adr.place(relx=0.60, rely=0.25, relheight=0.40, relwidth=0.35)
btn_clip.place(relx=0.60, rely=0.70, relheight=0.05, relwidth=0.35)

# Labeltext on init
lblText="Herr\nMax Mustermann\n12345 Musterstadt\nMusterstraße 1"
lbl_adr.configure(text=lblText, font='Helvetia')

app.mainloop()