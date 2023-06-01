import cv2
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np

#OJO debes cambiar la variable llamada URL por la ruta en la que está el archivo haarcascade_frontalface_default, el archivo lo puedes encontrar en el siguientelink
#https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml


URL = r"C:\Users\im00719\OneDrive - Alliance\Documentos\GitHub\Aplicaciones-python\Detector de caras"


face_cascade = cv2.CascadeClassifier(URL + '\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

window = tk.Tk()
window.title("Face Detection")
window.geometry("800x600")

label_image = tk.Label(window)
label_image.pack()

def detectar_rostros():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        face_image = frame[y:y+h, x:x+w]

        mostrar_imagen(face_image)

    mostrar_imagen(frame)

    window.after(10, detectar_rostros)

def mostrar_imagen(image):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    label_image.configure(image=image)
    label_image.image = image


detectar_rostros()
window.mainloop()

cap.release()
cv2.destroyAllWindows()
