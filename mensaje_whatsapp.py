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


# Crear la ventana principal
window = tk.Tk()
window.title("Enviar mensaje de WhatsApp")

# Etiqueta y campo de entrada para el número
label_numero = tk.Label(window, text="Número de teléfono:")
label_numero.pack()
entry_numero = tk.Entry(window)
entry_numero.pack()

# Etiqueta y campo de entrada para el mensaje
label_mensaje = tk.Label(window, text="Mensaje:")
label_mensaje.pack()
entry_mensaje = tk.Entry(window)
entry_mensaje.pack()

# Botón para enviar el mensaje
button_enviar = tk.Button(window, text="Enviar", command=enviar_whatsapp)
button_enviar.pack()

# Ejecutar la ventana principal
window.mainloop()
