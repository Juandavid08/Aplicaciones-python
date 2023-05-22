import tkinter as tk
import webbrowser


def enviar_whatsapp():
    numero = entry_numero.get()
    mensaje = entry_mensaje.get()

    if numero and mensaje:
        numero = numero.replace(" ", "")  # Eliminar espacios en blanco
        url = f"https://api.whatsapp.com/send?phone={numero}&text={mensaje}"
        webbrowser.open(url)
    else:
        messagebox.showwarning("Error", "Ingresa el número y el mensaje.")


# Ventana principal
window = tk.Tk()
window.title("Enviar mensaje de WhatsApp")

window.geometry("400x300")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - 400) / 2)  # Centrar horizontalmente
y = int((screen_height - 300) / 2)  # Centrar verticalmente

window.geometry(f"400x300+{x}+{y}")

label_numero = tk.Label(window, text="Número de teléfono:")
label_numero.pack()
entry_numero = tk.Entry(window)
entry_numero.pack()

label_mensaje = tk.Label(window, text="Mensaje:")
label_mensaje.pack()
entry_mensaje = tk.Entry(window)
entry_mensaje.pack()


button_enviar = tk.Button(window, text="Enviar", command=enviar_whatsapp)
button_enviar.pack()

window.mainloop()
