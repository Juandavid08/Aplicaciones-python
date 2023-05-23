import tkinter as tk
import speech_recognition as sr

def iniciar_escucha():
    global reconocedor, boton_escuchar

    if boton_escuchar["text"] == "Escuchar":
        boton_escuchar.configure(text="Detener", command=detener_escucha)
        reconocedor = sr.Recognizer()
        with sr.Microphone() as source:
            audio = reconocedor.listen(source)
        try:
            texto = reconocedor.recognize_google(audio, language="es-ES")
            texto_entrada.insert(tk.END, texto)
        except sr.UnknownValueError:
            texto_entrada.insert(tk.END, "No se pudo reconocer el habla.")
        except sr.RequestError:
            texto_entrada.insert(tk.END, "Error en la solicitud.")
    else:
        detener_escucha()

def detener_escucha():
    global boton_escuchar
    boton_escuchar.configure(text="Escuchar", command=iniciar_escucha)

window = tk.Tk()
window.title("Reconocimiento de Voz")

boton_escuchar = tk.Button(window, text="Escuchar", command=iniciar_escucha)
boton_escuchar.pack(pady=10)

texto_entrada = tk.Text(window, height=5)
texto_entrada.pack(pady=10)

window.mainloop()


