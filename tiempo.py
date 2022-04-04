from tkinter import *
import requests

ventana = Tk()
ventana.geometry("350x400")
ventana.title("Gheli Weather Solutions")
ventana.resizable(False, False)
ventana.iconbitmap("icon.ico")
ventana.config(bg="mediumaquamarine")

# Funcionalidad


def mostrarRespuestas(clima):
    try:
        nombreCiudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]

        ciudad["text"] = nombreCiudad
        temperatura["text"] = str(int(temp)) + "°C"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "Intenta nuevamente"


def clima_JSON(ciudad):
    try:
        API_key = "b8b791fc1b3c74cd510b33d2b4e055fd"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID": API_key, "q": ciudad,
                      "units": "metric", "lang": "es"}
        response = requests.get(URL, params=parametros)
        clima = response.json()
        mostrarRespuestas(clima)
    except:
        print("Error")


# Entrada de texto
textoCiudad = Entry(ventana, bg="White", font=(
    "Courier", 20), justify="center")
textoCiudad.pack(padx=30, pady=30)

# Boton
obtenerClima = Button(ventana, bg="lemonchiffon",
                      text="Obtener Clima", font=("Courier", 11), command=lambda: clima_JSON(textoCiudad.get()))
obtenerClima.pack()

# Etiquetas
ciudad = Label(bg="mediumaquamarine", fg="White",
               font=("Courier Bold", 20, "normal"))
ciudad.pack(padx=20, pady=20)

temperatura = Label(bg="mediumaquamarine", fg="White",
                    font=("Courier Bold", 50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion = Label(bg="mediumaquamarine", fg="White",
                    font=("Courier Bold", 20, "normal"))
descripcion.pack(padx=10, pady=10)

ventana.mainloop()
