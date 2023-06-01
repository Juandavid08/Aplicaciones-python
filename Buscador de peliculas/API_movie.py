import tkinter as tk
import requests
from unidecode import unidecode
from urllib.parse import urlencode
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import themed_tk as tkth


#OJO esta API KEY es personal, si deseas tener una debes ingresar al sitio de TMDB y registrarte
API_KEY = "22495c714623687580c87278cf36ebaf"

def buscar_peliculas():
    busqueda = entry_busqueda.get()
    categoria = combo_categorias.get()
    doblaje = combo_doblaje.get()

    if not busqueda or not categoria:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una búsqueda y selecciona una categoría.")
        return

    if categoria == "Título":
        buscar_peliculas_por_nombre(busqueda, doblaje)
    elif categoria == "Categoría":
        id_categoria = obtener_id_categoria(busqueda, doblar(doblaje))
        if id_categoria is not None:
            buscar_peliculas_por_categoria(id_categoria, doblaje)
        else:
            messagebox.showwarning("Advertencia", "Categoría no encontrada.")
    elif categoria == "Actor":
        buscar_peliculas_por_actor(busqueda, doblaje)
    scrollbar.set(0, 0)


def buscar_peliculas_por_nombre(nombre, doblaje):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={nombre}&language={doblar(doblaje)}"
    realizar_busqueda(url, doblaje)

def buscar_peliculas_por_categoria(id_categoria, doblaje):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={id_categoria}&language={doblar(doblaje)}"
    realizar_busqueda(url, doblaje)

def obtener_id_categoria(nombre_categoria, idioma):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language={idioma}"
    response = requests.get(url)

    try:
        response.raise_for_status()
        data = response.json()

        if "genres" in data:
            genres = data["genres"]
            for genre in genres:
                if unidecode(genre.get("name", "").lower()) == unidecode(nombre_categoria.lower()):
                    return genre.get("id")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error en la solicitud: {e}")

    return None

def buscar_peliculas_por_actor(actor, doblaje):
    url = f"https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={actor}&language={doblar(doblaje)}"
    response = requests.get(url)

    try:
        response.raise_for_status()
        data = response.json()

        if "results" in data:
            resultados = data["results"]
            peliculas = []
            for resultado in resultados:
                id_actor = resultado.get("id", "")
                peliculas_actor = obtener_peliculas_por_actor(id_actor, doblaje)
                peliculas.extend(peliculas_actor)
            mostrar_resultados(peliculas, doblaje)
        else:
            messagebox.showinfo("Información", "No se encontraron resultados.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error en la solicitud: {e}")

def realizar_busqueda(url, doblaje, params=None):
    if params is not None:
        query_string = urlencode(params)
        url += '&' + query_string
    response = requests.get(url)

    try:
        response.raise_for_status()
        data = response.json()

        if "results" in data:
            peliculas = data["results"]
            mostrar_resultados(peliculas, doblaje)
        else:
            messagebox.showinfo("Información", "No se encontraron resultados.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error en la solicitud: {e}")

def obtener_peliculas_por_actor(id_actor, doblaje):
    url = f"https://api.themoviedb.org/3/person/{id_actor}/movie_credits?api_key={API_KEY}&language={doblar(doblaje)}"
    response = requests.get(url)
    peliculas = []

    try:
        response.raise_for_status()
        data = response.json()

        if "cast" in data:
            peliculas = data["cast"]

        return peliculas
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error en la solicitud: {e}")
        return peliculas

def mostrar_resultados(peliculas, doblaje):
    resultados_treeview.delete(*resultados_treeview.get_children())

    for pelicula in peliculas:
        titulo = pelicula.get("title", "")
        descripcion = pelicula.get("overview", "")
        fecha_estreno = pelicula.get("release_date", "")
        resultados_treeview.insert("", tk.END, values=(titulo, descripcion, fecha_estreno))
    resultados_treeview.yview_moveto(0.0)

def doblar(doblaje):
    doblajes = {
        "Inglés": "en",
        "Castellano": "es-ES",
        "Italiano": "it",
        "Francés": "fr",
        "Alemán": "de",
        "Japón": "ja",
        "Portugués": "pt",
        "Coreano": "ko",
        "Chino": "zh-TW",
        "Ruso": "ru"
    }
    
    return doblajes.get(doblaje, "en-US")


# Ventana principal
window = tkth.ThemedTk(theme="arc") 
window.title("Búsqueda de películas")
style = ttk.Style()
style.configure("EstiloBoton.TButton", foreground="blue", font=("Arial", 12), background="blue")

# Etiquetas
label_busqueda = tk.Label(window, text="Búsqueda:")
label_busqueda.grid(row=0, column=0)
entry_busqueda = tk.Entry(window)
entry_busqueda.grid(row=0, column=1)

label_categoria = tk.Label(window, text="Filtrar por:")
label_categoria.grid(row=1, column=0)
categorias = ["Título", "Categoría", "Actor"]
combo_categorias = ttk.Combobox(window, values=categorias)
combo_categorias.grid(row=1, column=1)

label_doblaje = tk.Label(window, text="Doblaje:")
label_doblaje.grid(row=2, column=0)
doblajes = ["Castellano", "Inglés", "Italiano", "Francés", "Alemán", "Japonés", "Portugués", "Coreano", "Chino", "Ruso"]
combo_doblaje = ttk.Combobox(window, values=doblajes)
combo_doblaje.grid(row=2, column=1)

resultados_treeview = ttk.Treeview(window, columns=("Título", "Descripción", "Fecha de Estreno"), show="headings")
resultados_treeview.heading("Título", text="Título")
resultados_treeview.heading("Descripción", text="Descripción")
resultados_treeview.heading("Fecha de Estreno", text="Fecha de Estreno")
resultados_treeview.grid(row=3, column=0, columnspan=2, sticky="nsew")

scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=resultados_treeview.yview)
scrollbar.grid(row=3, column=2, sticky="ns")
resultados_treeview.configure(yscrollcommand=scrollbar.set)

btn_buscar = ttk.Button(window, text="Buscar", style="EstiloBoton.TButton", command=buscar_peliculas)
btn_buscar.grid(row=4, column=0, columnspan=2)

window.mainloop()