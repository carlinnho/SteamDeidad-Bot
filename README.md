# 🎮 SteamDeidad - Asistente de Videojuegos en Prolog

**SteamDeidad** es un sistema experto desarrollado en **Prolog** que actúa como un asistente virtual capaz de ayudarte a explorar y descubrir videojuegos. Con una base de datos de más de 150 títulos, este bot interactivo responde a tus consultas, te da recomendaciones y te acompaña con mensajes personalizados.

---

## 📌 Características

- ✅ Desarrollado íntegramente en **Prolog**.
- 🧠 Contiene una **base de conocimiento con más de 150 videojuegos**, clasificados por género, plataforma, rating, año y modo de juego.
- 🤖 Cuenta con un **bot inteligente llamado SteamDeidad**, que te saluda, responde e interactúa contigo.
- 🧭 Menú interactivo con **9 opciones funcionales**, que incluyen filtros, búsqueda avanzada y recomendaciones.
- 🔍 Sistema de búsqueda que permite encontrar juegos incluso si **no se introduce el nombre exacto**.
- 🛠️ Modular y escalable: se pueden añadir nuevos juegos o reglas fácilmente.
- 🎮 Incluye desde títulos AAA, indies, hasta juegos mal valorados para mayor variedad.

---

## 🚀 Despliegue

### 1. Requisitos
- Tener instalado **SWI-Prolog**. Puedes descargarlo desde: https://www.swi-prolog.org/

### 2. Ejecución
1. Abre SWI-Prolog.
2. Carga el proyecto:
   ```prolog
   consult('steamdeidad.pl').

   
### 3. Inicia el proyecto con:
 iniciar.

### 4. Menu Dinamico:
| Nº | Opción                                                                   |
| -- | ------------------------------------------------------------------------ |
| 1  | Buscar videojuegos por **género**                                        |
| 2  | Buscar videojuegos por **año de lanzamiento**                            |
| 3  | Buscar videojuegos por **rating**                                        |
| 4  | Buscar videojuegos por **plataforma**                                    |
| 5  | Buscar videojuegos por **modo de juego** (solo / multi / ambos)          |
| 6  | Mostrar **todos los videojuegos** disponibles                            |
| 7  | Consultar información **completa** de un videojuego (por nombre parcial) |
| 8  | Obtener **recomendaciones personalizadas** por género o modo             |
| 9  | **Salir** del sistema con despedida personalizada del bot                |


### 5. Ejemplo de interacción:
SteamDeidad:- ¡BUENAS! He cargado todo un catálogo de juegos.
SteamDeidad:- Hola, bienvenido. Soy SteamDeidad.
SteamDeidad:- ¿Cómo puedo ayudarte hoy?

1. Buscar por género
2. Buscar por año
3. Buscar por rating
4. Buscar por plataforma
5. Buscar por modo de juego
6. Mostrar todos los videojuegos
7. Ver información completa de un videojuego
8. Recomendaciones personalizadas
9. Salir

Seleccione una opción: 1.

Ingrese el género deseado: rpg.

SteamDeidad:- Estos juegos podrían interesarte:
- The Witcher 3
- Elden Ring
- Dark Souls III
- Genshin Impact
- Monster Hunter Rise
...

Seleccione una opción: 7.

SteamDeidad:- Vale, tú dime qué juego y yo te ayudo completamente.  
Ingrese el nombre del videojuego entre comillas: "Sekiro".

SteamDeidad:- ¡Encontré esto para ti!

Nombre: Sekiro: Shadows Die Twice  
Género: accion  
Plataforma: pc  
Rating: 5  
Año: 2019  
Modo: solo

...

Seleccione una opción: 9.

SteamDeidad:- Hasta pronto, gamer.
SteamDeidad:- Me desconecto. GG.
SteamDeidad ha cerrado sesión.



