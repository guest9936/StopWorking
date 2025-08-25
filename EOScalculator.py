import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calcola_orario(orario_input=None):
    try:
        if orario_input is None:  # prendo dalla casella di input
            orario_input = entry_orario.get()
            orario = datetime.strptime(orario_input, "%H:%M")
        else:  # uso l'orario passato (es. quello attuale)
            orario = orario_input

        nuovo_orario = orario + timedelta(hours=8, minutes=45)
        entry_risultato.config(state="normal")
        entry_risultato.delete(0, tk.END)
        entry_risultato.insert(0, nuovo_orario.strftime("%H:%M"))
        entry_risultato.config(state="readonly")
    except ValueError:
        messagebox.showerror("Errore", "Formato non valido. Usa HH:MM (es. 14:30)")

def calcola_da_adesso():
    calcola_orario(datetime.now())

# Finestra principale
root = tk.Tk()
root.title("Calcolatore Orario")

# Etichetta e campo input
tk.Label(root, text="Inserisci un orario (HH:MM):").grid(row=0, column=0, padx=10, pady=10)
entry_orario = tk.Entry(root)
entry_orario.grid(row=0, column=1, padx=10, pady=10)

# Pulsanti
btn1 = tk.Button(root, text="Calcola +8h45m", command=lambda: calcola_orario())
btn1.grid(row=1, column=0, padx=10, pady=10)

btn2 = tk.Button(root, text="Da adesso +8h45m", command=calcola_da_adesso)
btn2.grid(row=1, column=1, padx=10, pady=10)

# Risultato
tk.Label(root, text="Orario risultante:").grid(row=2, column=0, padx=10, pady=10)
entry_risultato = tk.Entry(root, state="readonly")
entry_risultato.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
