import tkinter as tk
from datetime import datetime, timedelta
from tkinter import ttk

#Array que contiene las diferentes ciudades utilizadas y su diferencia de horario
ciudades = {
    "Bogotá": -5,
    "Madrid": 2,
    "Londres": 1,
    "Berlín": 2,
    "Washington": -4,
    "Tokio": 9,
    "Cairo": 3
}

def actualizar_hora():
    ciudad = combo_ciudades.get()
    if ciudad and ciudad in ciudades:
        diferencia_horaria = timedelta(hours=ciudades[ciudad])
        hora_actual = (datetime.utcnow() + diferencia_horaria).strftime("%H:%M:%S")
        label.config(text=hora_actual)
    else:
        label.config(text="00:00:00")
    ventana.after(1000, actualizar_hora)

ventana = tk.Tk()
ventana.title("Reloj Mundial")

label = tk.Label(ventana, font=("Arial", 80), bg="black", fg="white", text="00:00:00")
label.pack(padx=50, pady=50)

combo_ciudades = ttk.Combobox(ventana, values=["Selecciona una ciudad"] + list(ciudades.keys()))
combo_ciudades.current(0)
combo_ciudades.pack()

actualizar_hora()

ventana.mainloop()