import requests
from langid import classify
import tkinter as tk
from tkinter import ttk

def texto_traducir(texto, idioma_destino):
    idioma_origen = classify(texto)[0]
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": texto,
        "langpair": f"{idioma_origen}|{idioma_destino}"
    }
    response = requests.get(url, params=params)
    translation = response.json()["responseData"]["translatedText"]
    return translation

def traduccion():
    texto_entrada = entrada_texto.get("1.0", "end-1c")
    idioma_destino = destino_combobox.get().split(" - ")[1]
    idioma_origen = origen_combobox.get().split(" - ")[1]

    if idioma_origen == "":
        idioma_origen = classify(texto_entrada)[0]
        for idx, idioma in enumerate(idiomas):
            if idioma.endswith(idioma_origen):
                origen_combobox.current(idx)
                break

    texto_traducido = texto_traducir(texto_entrada, idioma_destino)
    salida_texto.delete("1.0", "end")
    salida_texto.insert("1.0", texto_traducido)

window = tk.Tk()
window.title("Traductor")
window.geometry("400x300")

window_frame = ttk.Frame(window)
window_frame.pack(pady=20)

entrada_texto = tk.Text(window_frame, height=5)
entrada_texto.pack(pady=10)

idiomas = [
    "Inglés - en",
    "Español - es",
    "Francés - fr",
    "Italiano - it",
    "Alemán - de",
    "Indú - hi",
    "Portugués - pt",
    "Holandés - nl",
    "Griego - el",
    "Polaco - pl",
    "Ruso - ru",
    "Chino Mandarín - zh-CN",
    "Japonés - ja"
]

origen_combobox = ttk.Combobox(window_frame, values=idiomas, state="readonly", textvariable=tk.StringVar(value=""))
origen_combobox.pack()

destino_combobox = ttk.Combobox(window_frame, values=idiomas, state="readonly", textvariable=tk.StringVar(value="Español - es"))
destino_combobox.pack()

traducir_button = ttk.Button(window_frame, text="Traducir", command=traduccion)
traducir_button.pack(pady=10)

salida_texto = tk.Text(window, height=5)
salida_texto.pack(pady=10)

frame_style = ttk.Style()
frame_style.configure("Custom.TFrame", background="#f0f0f0")

window_frame.configure(style="Custom.TFrame")

label_style = ttk.Style()
label_style.configure("Custom.TLabel", background="#f0f0f0", font=("Arial", 12))

window_frame_label = ttk.Label(window_frame, text="Texto a Traducir:", style="Custom.TLabel")
window_frame_label.pack()

button_style = ttk.Style()
button_style.configure("Custom.TButton", background="#4caf50", foreground="white", font=("Arial", 12))

traducir_button.configure(style="Custom.TButton")

window.mainloop()
