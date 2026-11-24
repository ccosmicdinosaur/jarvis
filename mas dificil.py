print("pequeño jarvis, ahora probando cositas mas dificiles ohsiohsi")

from datetime import datetime
import os

memoria = {}
recuerdos = []

apps = {
    "calculadora": "calc",
    "bloc": "notepad",
    "paint": "mspaint",
}

with open("recuerdos.txt", "r") as archivo:
    for linea in archivo:
        recuerdos.append(linea.strip())

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

        with open("recuerdos.txt", "a") as archivo:
            archivo.write(recuerdo + "\n")

        print("Jarvis: lo recordaré :)")

    elif comando == "mostrar recuerdos":
        if len(recuerdos) == 0:
            print("ME BORRASTE LOS RECUERDOS, COMO VOY A RECORDAR ALGO??? :(")

        else:
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
        print("Jarvis:ya no son mas 5 minutos... ahora tengo un dia de vida. que rapido pasa el tiempo...")

    elif comando == "ostia":
        print("Jarvis: OSTIA TIOOOOOO")

    elif comando.startswith("abrir "):

        app = comando.replace("abrir ", "")

        if app in apps:
            os.system(f"start {apps[app]}")
            print(f"Jarvis: abriendo {app}...")
        else:
            print("Jarvis: no conozco esa aplicación :(")

    elif comando == "borrar recuerdos":
        print("Jarvis: NOOOOO MIS RECUERDOSSS :(")
        recuerdos.clear()
        open("recuerdos.txt", "w")
    
    elif comando.startswith("olvidar "):
        recuerdo_a_borrar = comando.replace("olvidar ", "")

        if recuerdo_a_borrar in recuerdos:
            recuerdos.remove(recuerdo_a_borrar)

            with open("recuerdos.txt", "w") as archivo:
                for recuerdo in recuerdos:
                    archivo.write(recuerdo + "\n")

            print("Jarvis: okk, ya no me acuerdo de eso")
        else:
            print("Jarvis: no tengo ese recuerdo")

    elif comando == "que podes hacer":
        print("- holi → te saludo")
        print("- hora → muestro la hora")
        print("- nombre → digo mi nombre")
        print("- edad → digo mi edad")
        print("- acordate que... → guardo recuerdos")
        print("- mostrar recuerdos → muestro mis recuerdos")
        print("- olvidar todo → borra mis recuerdos :(")
        print("- ostia → OSTIA TIOOOOOO")
        print("- salir → cierra el programa")

    else:
        print("Jarvis: ehh?? ravioles :D")
