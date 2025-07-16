import customtkinter
from pyswip import Prolog

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("green")

prolog = Prolog()
prolog.consult("steamdeidad.pl")


# --------------------------
# Pantalla de bienvenida
# --------------------------
def pantalla_bienvenida():
    root = customtkinter.CTk() 
    root.title("SteamDeidad - Bienvenida")
    root.geometry("500x250")

    # Etiqueta principal
    titulo = customtkinter.CTkLabel(
        root,
        text="👾 Hola, bienvenido a SteamDeidad",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=20)


    from random import choice
    mensajes = [
        "SteamDeidad:- ¡Hola! ¿Listo para hablar sobre juegos?",
        "SteamDeidad:- Soy SteamDeidad, tu guía gamer.",
        "SteamDeidad:- Sistema cargado. ¿Jugamos?",
        "SteamDeidad:- ¡Buenos días, jugador estético!",
        "SteamDeidad:- Te ves bien hoy... para ser gamer."
    ]
    mensaje_bot = customtkinter.CTkLabel(
        root,
        text=choice(mensajes),
        font=("Arial", 13),
        wraplength=450,
        text_color="lightgray"
    )
    mensaje_bot.pack(pady=10)

    # Botón para iniciar
    boton_iniciar = customtkinter.CTkButton(
        root,
        text="🎮 Iniciar",
        font=("Arial", 14, "bold"),
        command=lambda: menu_principal(root)
    )
    boton_iniciar.pack(pady=20)

    root.mainloop()

# --------------------------
# Menú principal (después de iniciar)
# --------------------------
def menu_principal(ventana_actual):
    ventana_actual.destroy()

    menu = customtkinter.CTk()
    menu.title("SteamDeidad - Menú Principal")
    menu.geometry("400x500")

    titulo = customtkinter.CTkLabel(menu, text="🕹️ SteamDeidad - Menú Principal", font=("Arial", 16, "bold"))
    titulo.pack(pady=15)

    opciones = [
        ("1. Listar videojuegos por género", ventana_genero),
        ("2. Listar videojuegos por rating mínimo", ventana_rating),
        ("3. Listar videojuegos por modo de juego", ventana_modo_juego),
        ("4. Listar videojuegos por año", ventana_anio),
        ("5. Mostrar todos los videojuegos", ventana_todos),
        ("6. Mostrar géneros disponibles", ventana_generos_disponibles),
        ("7. Información completa de un videojuego", ventana_info_completa),
        ("8. Recomendaciones personalizadas", ventana_recomendaciones),
        ("9. Salir", lambda: menu.destroy())
    ]

    for texto, accion in opciones:
        boton = customtkinter.CTkButton(menu, text=texto, width=250, command=accion)
        boton.pack(pady=6)

    menu.mainloop()


# --------------------------
# Ventana por opción 1: Buscar por género
# --------------------------
def ventana_genero():
    sub = customtkinter.CTkToplevel()
    sub.title("Buscar por Género")
    sub.geometry("460x400")

    customtkinter.CTkLabel(sub, text="🎮 Género del juego (ej: rpg, accion):").pack(pady=10)

    entrada = customtkinter.CTkEntry(sub, width=250)
    entrada.pack()

    resultado_text = customtkinter.CTkTextbox(sub, height=200, width=420)
    resultado_text.pack(pady=15)

    def buscar():
        genero = entrada.get().lower()
        resultado_text.delete("1.0", "end")
        try:
            resultados = list(prolog.query(f"videojuegos_por_genero({genero}, Lista).", maxresult=1))
            if resultados:
                juegos = resultados[0]["Lista"]
                resultado_text.insert("end", f"🎮 Juegos del género '{genero}':\n")
                for juego in juegos:
                    nombre = juego.decode() if isinstance(juego, bytes) else str(juego)
                    resultado_text.insert("end", f" - {nombre}\n")
            else:
                resultado_text.insert("end", "⚠️ No se encontraron juegos.")
        except Exception as e:
            resultado_text.insert("end", f"❌ Error: {e}")

    customtkinter.CTkButton(sub, text="Buscar", command=buscar).pack(pady=10)

# --------------------------
# Ventana por opción 2: Buscar por rating mínimo
# --------------------------
def ventana_rating():
    sub = customtkinter.CTkToplevel()
    sub.title("Buscar juegos por Rating")
    sub.geometry("420x350")

    customtkinter.CTkLabel(sub, text="📊 Inserte Rating (1 a 5):").pack(pady=10)

    entrada = customtkinter.CTkEntry(sub, width=80)
    entrada.pack()

    resultado_text = customtkinter.CTkTextbox(sub, height=200, width=380)
    resultado_text.pack(pady=15)

    def buscar():
        rating_str = entrada.get().strip()
        resultado_text.delete("1.0", "end")

        try:
            rating = int(rating_str)
            if rating < 1 or rating > 5:
                resultado_text.insert("end", "⚠️ El rating debe estar entre 1 y 5.")
                return

            resultados = list(prolog.query(f"videojuegos_por_rating_exacto({rating}, Lista)."))
            if resultados:
                juegos = resultados[0]["Lista"]
                resultado_text.insert("end", f"🎮 Juegos con rating igual a {rating}:\n")
                for juego in juegos:
                    nombre = juego.decode() if isinstance(juego, bytes) else str(juego)
                    resultado_text.insert("end", f" - {nombre}\n")
            else:
                resultado_text.insert("end", "⚠️ No se encontraron juegos.")
        except ValueError:
            resultado_text.insert("end", "❌ Ingresa un número entero válido.")
        except Exception as e:
            resultado_text.insert("end", f"❌ Error: {e}")

    customtkinter.CTkButton(sub, text="Buscar", command=buscar).pack(pady=10)


# --------------------------
# Ventana opcion 3
# --------------------------

def ventana_modo_juego():
    sub = customtkinter.CTkToplevel()
    sub.title("Buscar por Modo de Juego")
    sub.geometry("440x500")

    customtkinter.CTkLabel(
        sub,
        text="SteamDeidad:- Entre solo, multi y ambos, soy más fan de juegos solo, te mete más al juego",
        wraplength=400,
        justify="center"
    ).pack(pady=10)

    customtkinter.CTkLabel(sub, text="🎮 Selecciona el modo de juego:", font=("Arial", 12)).pack(pady=5)

    resultado_text = customtkinter.CTkTextbox(sub, height=240, width=400)
    resultado_text.pack(pady=15)

    def buscar_por_modo(modo):
        resultado_text.delete("1.0", "end")
        try:
            resultados = list(prolog.query(f"videojuegos_por_modo({modo}, Lista).", maxresult=1))
            if resultados:
                juegos = resultados[0]["Lista"]
                resultado_text.insert("end", f"🎮 Juegos con modo '{modo}':\n\n")
                for i, juego in enumerate(juegos, 1):
                    nombre = juego.decode() if isinstance(juego, bytes) else str(juego)
                    resultado_text.insert("end", f"{i} - {nombre}\n")
            else:
                resultado_text.insert("end", "⚠️ No se encontraron juegos.")
        except Exception as e:
            resultado_text.insert("end", f"❌ Error: {e}")

    frame_botones = customtkinter.CTkFrame(sub, fg_color="transparent")
    frame_botones.pack(pady=10)

    customtkinter.CTkButton(frame_botones, text="🎮 Solo", width=100, command=lambda: buscar_por_modo("solo")).pack(side="left", padx=5)
    customtkinter.CTkButton(frame_botones, text="🧑‍🤝‍🧑 Multi", width=100, command=lambda: buscar_por_modo("multi")).pack(side="left", padx=5)
    customtkinter.CTkButton(frame_botones, text="⚔ Ambos", width=100, command=lambda: buscar_por_modo("ambos")).pack(side="left", padx=5)

# --------------------------
# Ventana opcion 4
# --------------------------

def ventana_anio():
    sub = customtkinter.CTkToplevel()
    sub.title("Buscar por Año de Lanzamiento")
    sub.geometry("430x350")

    customtkinter.CTkLabel(sub, text="📅 Año de lanzamiento (ej. 2020):").pack(pady=10)

    entrada = customtkinter.CTkEntry(sub, width=120)
    entrada.pack()

    resultado_text = customtkinter.CTkTextbox(sub, height=200, width=390)
    resultado_text.pack(pady=15)

    def buscar():
        anio_str = entrada.get().strip()
        resultado_text.delete("1.0", "end")

        try:
            anio = int(anio_str)
            resultados = list(prolog.query(f"videojuegos_por_anio({anio}, Lista).", maxresult=1))
            if resultados:
                juegos = resultados[0]["Lista"]
                if juegos:
                    resultado_text.insert("end", f"📅 Juegos lanzados en {anio}:\n")
                    for juego in juegos:
                        nombre = juego.decode() if isinstance(juego, bytes) else str(juego)
                        resultado_text.insert("end", f" - {nombre}\n")
                else:
                    resultado_text.insert("end", f"⚠️ No se encontraron juegos lanzados en {anio}.")
            else:
                resultado_text.insert("end", f"⚠️ No se encontraron juegos lanzados en {anio}.")
        except ValueError:
            resultado_text.insert("end", "❌ Ingresa un año válido (número entero).")
        except Exception as e:
            resultado_text.insert("end", f"❌ Error: {e}")

    customtkinter.CTkButton(sub, text="Buscar", command=buscar).pack(pady=10)


# --------------------------
# Ventana opcion 5
# --------------------------

def ventana_todos():
    sub = customtkinter.CTkToplevel()
    sub.title("Todos los Videojuegos")
    sub.geometry("500x550")

    resultado_text = customtkinter.CTkTextbox(sub, height=430, width=460)
    resultado_text.pack(pady=15)

    try:
        resultados = list(prolog.query("todos_los_videojuegos(Lista).", maxresult=1))
        if resultados:
            juegos = resultados[0]["Lista"]
            if juegos:
                resultado_text.insert("end", "SteamDeidad:- No te asustes, pero serán muchos, créeme MUCHOS\n\n")
                resultado_text.insert("end", f"🎮 Total de videojuegos registrados: {len(juegos)}\n\n")
                for idx, juego in enumerate(juegos, 1):
                    nombre = juego.decode() if isinstance(juego, bytes) else str(juego)
                    resultado_text.insert("end", f"{idx} - {nombre}\n")
            else:
                resultado_text.insert("end", "⚠️ No se encontraron videojuegos registrados.")
        else:
            resultado_text.insert("end", "⚠️ No se pudo obtener la lista de videojuegos.")
    except Exception as e:
        resultado_text.insert("end", f"❌ Error: {e}")

# --------------------------
# Ventana opcion 6
# --------------------------

def ventana_generos_disponibles():
    sub = customtkinter.CTkToplevel()
    sub.title("Géneros Disponibles")
    sub.geometry("460x400")

    resultado_text = customtkinter.CTkTextbox(sub, height=300, width=420)
    resultado_text.pack(pady=15)

    try:
        resultados = list(prolog.query("generos_disponibles(Lista).", maxresult=1))
        if resultados:
            generos = resultados[0]["Lista"]
            if generos:
                resultado_text.insert("end", "SteamDeidad:- Interesado en saber qué géneros de juegos existen? PERFECTO, acá está la lista:\n\n")
                for idx, genero in enumerate(generos, 1):
                    genero_str = genero.decode() if isinstance(genero, bytes) else str(genero)
                    resultado_text.insert("end", f"{idx} - {genero_str}\n")
            else:
                resultado_text.insert("end", "⚠️ No se encontraron géneros.")
        else:
            resultado_text.insert("end", "⚠️ Error al obtener los géneros.")
    except Exception as e:
        resultado_text.insert("end", f"❌ Error: {e}")


# --------------------------
# Ventana por opción 7: Información completa del videojuego
# --------------------------
def ventana_info_completa():
    sub = customtkinter.CTkToplevel()
    sub.title("Información Completa de Videojuego")
    sub.geometry("500x580")

    customtkinter.CTkLabel(sub, text="SteamDeidad:- Vale, dime el nombre o parte del nombre del juego y te ayudo.").pack(pady=5)
    customtkinter.CTkLabel(sub, text="Ingresa una palabra clave del nombre:").pack()
    entrada = customtkinter.CTkEntry(sub, width=200)
    entrada.pack()

    resultado_text = customtkinter.CTkTextbox(sub, height=250, width=440)
    resultado_text.pack(pady=15)

    def buscar():
        palabra = entrada.get().strip()
        if palabra == "":
            resultado_text.delete("1.0", "end")
            resultado_text.insert("end", "⚠️ Debes ingresar una palabra clave.\n")
            return

        resultado_text.delete("1.0", "end")
        try:
            query = f"buscar_juegos_parciales('{palabra}', Lista)."
            resultados = list(prolog.query(query, maxresult=1))
            if not resultados or not resultados[0]["Lista"]:
                resultado_text.insert("end", "SteamDeidad:- No encontré juegos que coincidan con esa palabra.\n")
                return

            juegos = resultados[0]["Lista"]
            juegos = [j.decode() if isinstance(j, bytes) else str(j) for j in juegos]

            resultado_text.insert("end", "SteamDeidad:- Aquí tienes los juegos que encontré:\n\n")
            for i, juego in enumerate(juegos, 1):
                resultado_text.insert("end", f"{i} - {juego}\n")

            customtkinter.CTkLabel(sub, text="\nSelecciona el número del juego:").pack()
            seleccion = customtkinter.CTkEntry(sub, width=100)
            seleccion.pack()

            def mostrar_info():
                try:
                    idx = int(seleccion.get()) - 1
                    if 0 <= idx < len(juegos):
                        nombre = juegos[idx]
                        nombre_prolog = '"' + nombre.replace('"', '\\"') + '"'
                        query_info = f"informacion_completa({nombre_prolog}, G, P, R, A, M)."

                        info_result = list(prolog.query(query_info, maxresult=1))
                        if info_result:
                            datos = info_result[0]
                            resultado_text.insert("end", "\n--- Información del juego ---\n")
                            resultado_text.insert("end", f"Nombre: {juegos[idx]}\n")
                            resultado_text.insert("end", f"Género: {datos['G']}\n")
                            resultado_text.insert("end", f"Plataforma: {datos['P']}\n")
                            resultado_text.insert("end", f"Rating: {datos['R']}\n")
                            resultado_text.insert("end", f"Año: {datos['A']}\n")
                            resultado_text.insert("end", f"Modo: {datos['M']}\n")
                        else:
                            resultado_text.insert("end", "\n⚠️ No se pudo obtener información del juego.")
                    else:
                        resultado_text.insert("end", "\n⚠️ Selección inválida.")
                except Exception as e:
                    resultado_text.insert("end", f"\n⚠️ Error al procesar: {e}")

            customtkinter.CTkButton(sub, text="Mostrar información", command=mostrar_info).pack(pady=5)

        except Exception as e:
            resultado_text.insert("end", f"❌ Error: {e}")

    customtkinter.CTkButton(sub, text="Buscar", command=buscar).pack(pady=5)




# --------------------------
# Ventana por opción 8: Recomendaciones personalizadas
# --------------------------

def ventana_recomendaciones():
    sub = customtkinter.CTkToplevel()
    sub.title("Recomendaciones Personalizadas")
    sub.geometry("500x700")

    customtkinter.CTkLabel(sub, text="SteamDeidad:- Vamos a afinar tus gustos...", font=("Arial", 14)).pack(pady=10)

    customtkinter.CTkLabel(sub, text="¿Qué género deseas explorar?").pack()
    entrada_genero = customtkinter.CTkEntry(sub, width=250)
    entrada_genero.pack(pady=5)

    customtkinter.CTkLabel(sub, text="¿Cuál es el rating mínimo (1 a 5)?").pack()
    entrada_rating = customtkinter.CTkEntry(sub, width=250)
    entrada_rating.pack(pady=5)

    customtkinter.CTkLabel(sub, text="¿Qué modo de juego prefieres? (solo / multi / ambos)").pack()
    entrada_modo = customtkinter.CTkEntry(sub, width=250)
    entrada_modo.pack(pady=5)

    resultado_text = customtkinter.CTkTextbox(sub, height=300, width=450)
    resultado_text.pack(pady=15)

    def recomendar():
        genero = entrada_genero.get().strip().lower()
        rating = entrada_rating.get().strip()
        modo = entrada_modo.get().strip().lower()

        resultado_text.delete("1.0", "end")

        if genero == "" or rating == "" or modo == "":
            resultado_text.insert("end", "⚠️ Por favor completa todos los campos.\n")
            return

        try:
            rating_val = int(rating)
            if rating_val < 1 or rating_val > 5:
                raise ValueError
        except:
            resultado_text.insert("end", "⚠️ El rating debe ser un número del 1 al 5.\n")
            return

        try:
            query = f"videojuego_filtrado(Nombre, '{genero}', {rating_val}, {modo})."
            juegos = list(prolog.query(query))
            juegos_unicos = list(set(j["Nombre"] for j in juegos))

            if juegos_unicos:
                resultado_text.insert("end", "SteamDeidad:- Aquí tienes tus recomendaciones personalizadas:\n\n")
                for i, juego in enumerate(juegos_unicos, 1):
                    nombre = juego.decode() if isinstance(juego, bytes) else str(juego)
                    resultado_text.insert("end", f"{i} - {nombre}\n")
            else:
                resultado_text.insert("end", "SteamDeidad:- Hmm... No encontré juegos que cumplan con esos criterios.\n")

        except Exception as e:
            resultado_text.insert("end", f"❌ Error al consultar recomendaciones: {e}")

    customtkinter.CTkButton(sub, text="Mostrar Recomendaciones", command=recomendar).pack(pady=10)


# --------------------------
# Función de saludo random
# --------------------------
def obtener_saludo_desde_prolog():
    try:
        consulta = list(prolog.query("saludo_random_python(M)."))
        if consulta:
            mensaje = consulta[0]["M"]
            return mensaje.decode() if isinstance(mensaje, bytes) else str(mensaje)
        else:
            return "SteamDeidad:- Hola humano... (no se pudo cargar el mensaje desde Prolog)"
    except Exception as e:
        return f"SteamDeidad:- Error al obtener saludo: {e}"
    
# --------------------------
# Función de atomos para llamada de juegos
# --------------------------
def escape_prolog_atom(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"



pantalla_bienvenida()

