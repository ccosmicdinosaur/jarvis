print("pequeño jarvis, creado el 16/11/26 OHSIOHSI, FUNCAAAA")

from datetime import datetime


memoria = {}

def obtener_hora():
    return datetime.now().strftime("%H:%M")

while True:
    comando = input("Yo: ").lower().strip()

    print("DEBUG:", comando)

    if comando == "holi":
        print("Jarvis: HOLIIIIII")

    elif comando == "que boludo":
        print("Jarvis: ey no me digas boludo, soy un pequeño bot :(")

    elif comando == "nombre":
        print("Jarvis: soy Jarvis :)")

    elif comando == "hora":
        print("Jarvis:", obtener_hora())

    elif comando == "salir":
        print("Jarvis: chau, creo...")
        break

    elif comando == "mi color favorito es rojo":
        memoria["color"] = "rojo"
        print("Jarvis: lo recordaré")
        print(memoria)

    elif comando == "cual es mi color favorito":
        print("Jarvis:", memoria.get("color", "todavía no me lo dijiste :("))

    elif comando == "edad":
        print("Jarvis: aproximadamente 5 minutos de vida")

    elif comando == "ostia":
        print("Jarvis: OSTIA TIOOOOOO")

    else:
        print("Jarvis: eh, gugugaga?")


