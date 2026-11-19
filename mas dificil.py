print("pequeño jarvis, ahora probando cositas mas dificiles")

from datetime import datetime

recuerdos = []
memoria = {}

def obtener_hora():
    return datetime.now().strftime("%H:%M")

while True:
    comando = input("Yo: ").lower().strip()

    print("DEBUG:", comando)

    if comando == "holi":
        print("Jarvis: HOLIIIIII")

    elif comando.startswith("acordate "):
        recuerdo = comando.replace(
            "acordate ",
            ""
        )

        recuerdos.append(recuerdo)

        print("Jarvis: lo recordaré :)")

    elif comando == "mostrar recuerdos":
        print("Jarvis: estos son mis recuerdos")

        for recuerdo in recuerdos:
            print("-", recuerdo)

    elif comando == "que boludo":
        print("Jarvis: ey no me digas boludo, soy un pequeño bot :(")

    elif comando == "nombre":
        print("Jarvis: soy Jarvis :)")

    elif comando == "hora":
        print("Jarvis:", obtener_hora())

    elif comando == "salir":
        print("Jarvis: chau, creo...")
        break

    elif comando.startswith("mi color favorito es "):
        color = comando.replace(
    "mi color favorito es ",
    ""
)
        memoria["color"] = color
        print("Jarvis: lo recordaré")
        print(memoria)

    elif comando == "cual es mi color favorito":
        print("Jarvis:", memoria.get("color", "todavía no me lo dijiste :("))

    elif comando == "eso no es un color":
        print("Jarvis: oh... bueno, no es un color, pero lo recordaré igual :)")

    elif comando == "edad":
        print("Jarvis: ya no son mas 5 minutos... ahora tengo un dia de vida. que rapido pasa el tiempo...")

    elif comando == "ostia":
        print("Jarvis: OSTIA TIOOOOOO")

    else:
        print("Jarvis: eh, gugugaga?")