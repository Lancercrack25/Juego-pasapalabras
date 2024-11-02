###menu de juego pasapalabras###
#from IPython.display import Image, display, clear_output #Biblioteca que nos permite tener distintas funciones de pantalla, como desplegar imágenes, tablas, borrar la terminal, etc
import random
import os
from os import system
import time #Biblioteca que nos permite ingresar al tiempo del sistema
from colorama import init, Fore, Back, Style, Cursor
import math
import pygame

#menu de juego #
def animate_typing(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def animacion_tipeo(texto):
    for caracter in texto:
        print(caracter, end='', flush=True)
        time.sleep(0.05)
    print()

def registro(nombres):
    system("cls")
    print(Fore.LIGHTMAGENTA_EX+"Has seleccionado la opción Registro."+ Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+'Si el nombre de usuario que elijas ya esta registrado, debes de ingresar uno nuevo'+Style.RESET_ALL)
    usuario = input(Fore.LIGHTWHITE_EX + "Ingresa tu nombre: " + Style.RESET_ALL)
    if usuario.isnumeric():
        raise ValueError(Fore.RED+("Error, el usuario solo debe contener letras")+Style.RESET_ALL)
        return registro(nombres)
    elif usuario in nombres:
        input(Fore.LIGHTWHITE_EX+"Usuario ya registrado, presiona enter para continuar... "+Style.RESET_ALL)
        return registro(nombres)
    else:
        nombres.append(usuario)
        return usuario

def mostrar_usuarios(usuarios):
    system("cls")
    print(Fore.LIGHTMAGENTA_EX+"Usuarios registrados: "+Style.RESET_ALL)
    for usuario in usuarios:
        print(Fore.LIGHTWHITE_EX+ usuario + Style.RESET_ALL)
    else:
        print(Fore.RED+"No hay usuarios registrados."+ Style.RESET_ALL)
        registro(usuarios)

def ver_puntuacion(puntuaciones_usuario, puntuajes_usuario):
    opcion = input(Fore.LIGHTMAGENTA_EX +'¿Qué deseas ver?\n 1.- Puntuación personal\n 2.- Puntuación global\n'+ Style.RESET_ALL)
    if opcion == '1':
        nombre = input(Fore.LIGHTCYAN_EX +"Introduce el nombre del usuario cuya puntuación deseas ver: "+Style.RESET_ALL)
        if nombre in puntuaciones_usuario:
            datos_usuario = puntuaciones_usuario[nombre]
            partida = datos_usuario['partidas']
            puntuacion = datos_usuario['puntuaciones']
            print(f"{Fore.LIGHTWHITE_EX}Nombre: {nombre} {Style.RESET_ALL}")
            print(f"{Fore.LIGHTWHITE_EX}Partidas: {partida} {Style.RESET_ALL}")
            print(f"{Fore.LIGHTWHITE_EX}Puntuaciones: {puntuacion} {Style.RESET_ALL}")
        else:
            print(Fore.RED+"El nombre de usuario ingresado no se encuentra en los registros."+Style.RESET_ALL)
        input(Fore.LIGHTYELLOW_EX+"Presione enter para continuar"+Style.RESET_ALL)
    elif opcion == '2':
        print(Fore.LIGHTMAGENTA_EX+'\t\t\t\t\t\t\t\t===========Puntuaciones Globales=========='+ Style.RESET_ALL)
        puntuaciones_ordenadas = sorted(puntuaciones_usuario.items(), key=lambda x: x[1]['puntuaciones'], reverse=True)
        for nombre, datos_usuario in puntuaciones_ordenadas:
            partida = datos_usuario['partidas']
            puntuacion = datos_usuario['puntuaciones']
            print(f"{Fore.LIGHTCYAN_EX}Nombre: {nombre}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTCYAN_EX}Partidas: {partida}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTCYAN_EX}Puntuaciones: {puntuacion}{Style.RESET_ALL}\n")
        input("Presione enter para continuar")
        system("cls")
    else:
        print(Fore.RED+"Opción inválida. Intente nuevamente."+Style.RESET_ALL)
        input(Fore.LIGHTYELLOW_EX+"Presione enter para continuar"+Style.RESET_ALL)
    return


"""letras = {
    "A": (0, 0, 0), "\033[0;30m"
    "B": (255, 255, 255), "\033[0;31m"
    "C": (255, 255, 255), "\033[0;32m"
    "D": (255, 255, 255), "\033[0;33m"
    "E": (255, 255, 255), "\033[0;34m"
    "F": (255, 255, 255), "\033[0;35m"
    "G": (255, 255, 255), "\033[0;36m"
    "H": (255, 255, 255), "\033[0;37m"
    "I": (255, 255, 255),"\033[0;31m"
    "J": (255, 255, 255), 

}


animacion = [
        f"          {letras['A']}  {letras['B']}",
        f"     {letras['J']}            {letras['C']}",
        f"   {letras['I']}        ?        {letras['D']}",
        f"     {letras['H']}            {letras['E']}",
        f"          {letras['G']}  {letras['F']}"
    ]


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def mostrar_animacion(letra_actual):
    t = 0
    angular_speed = 0.1

    while True:
        rotated_animacion = [""] * len(animacion)

        for i in range(len(animacion)):
            x_offset = int(math.sin(t) * 5)
            y_offset = int(math.cos(t) * 3)

            if i != 0:
                animacion[i] = [letra if letra != letra_actual else "!" for letra in animacion[i]]

            rotated_animacion[(i + y_offset) % len(animacion)] += "".join(animacion[i])

        screen.fill((0, 0, 0))

        for i, line in enumerate(rotated_animacion):
            for j, letra in enumerate(line):
                if letra == "!":
                    pygame.draw.rect(screen, (255, 0, 0),(j * 20 + x_offset, i * 20, 20, 20))
                else:
                    pygame.draw.rect(screen, letras[letra], (j * 20 + x_offset, i * 20, 20, 20))

        pygame.display.flip()

        t += angular_speed
        clock.tick(30) """# Limitar el framerate a 30 fps, cambiar a una frecuencia mas alta si se desea

"""def cambiar_letra():
    letras = ["A", "B", "C","D", "E", "F", "G", "H", "I", "J"]
    for letra in letras:
        mostrar_animacion(letra)
        pygame.time.wait(1000)"""

"""cambiar_letra()"""
            
####  
#       
# Animacion del juego
import time
from colorama import Fore, Back, Style

def mostrar_animacion(letra_actual):
    letras = {
        'A': 'A',
        'B': 'B',
        'C': 'C',
        'D': 'D',
        'E': 'E',
        'F': 'F',
        'G': 'G',
        'H': 'H',
        'I': 'I',
        'J': 'J'
    }

    animacion = [
        f"          {letras['A']}  {letras['B']}",
        f"     {letras['J']}            {letras['C']}",
        f"   {letras['I']}        ?        {letras['D']}",
        f"     {letras['H']}            {letras['E']}",
        f"          {letras['G']}  {letras['F']}"
    ]

    rotated_animacion = [''] * len(animacion)

    for i in range(len(animacion)):
        if i != 0:
            animacion[i] = animacion[i].replace(letras[letra_actual], f"{Fore.GREEN}{letras[letra_actual]}{Style.RESET_ALL}")

        rotated_animacion[i] += animacion[i]

    for line in rotated_animacion:
        print(line)

    time.sleep(10)
    print("\033[2J")  # Borra la pantalla

letra_actual = 'A'



"""def mostrar_animacion(letra_actual):
    letras = {
        'A': '\033[30mA\033[0m',
        'B': 'B',
        'C': 'C',
        'D': 'D',
        'E': 'E',
        'F': 'F',
        'G': 'G',
        'H': 'H',
        'I': 'I',
        'J': 'J'
    }
    animacion = [
        f"          {letras['A']}  {letras['B']}",
        f"     {letras['J']}            {letras['C']}",
        f"   {letras['I']}        ?        {letras['D']}",
        f"     {letras['H']}            {letras['E']}",
        f"          {letras['G']}  {letras['F']}"
    ]
    for i in range(len(animacion)):
        if i != 0:
            animacion[i] = animacion[i].replace(letras[letra_actual], f"\033[30m{letras[letra_actual]}\033[0m")
        print(animacion[i])"""

def mostrar_pregunta(letra, pregunta):
    print(f"¡Vamos con la letra {letra}!")
    mostrar_animacion(letra)
    print(pregunta)

def categoria_juegos():
    system("cls")
    preguntas = {
        'A': 'juego gratuito disponible en la web en el que eres un circulo y debe de comerse a otros para hacerse mas grande para ganar',
        'B': 'Videojuego que  nos cuenta la historia de Booker DeWitt, un veterano de guerra de dudosa moral que debe capturar a una joven, Elizabeth, en la ciudad de Columbia para saldar una deuda',
        'C': 'Nombre del protagonista del videojuego donde el villano es un cientifico loco con una N en la cabeza, el protagonista posee una mascara llamada aku-aku que controla a los monstruos',
        'D': 'Videojuego en el cual han surgido bastantes memes los cuales dicen que se puede correr hasta en una prueba de embarazo',
        'E': 'Nombre del videojuego en el cual el protagonista es un felino que lleva botas',
        'F': 'Videojuego popular en el cual es conocido por sus famosos bailes y sus diversas skins',
        'G': 'Videojuego en el cual el protagonista viaja a una ciudad destrozada por las bandas, las drogas y la corrupción en la que las estrellas de cine y los millonarios hacen lo posible por evitar a los traficantes y a los pandilleros',
        'H': 'Videojuego que se centra en una guerra interestelar entre la humanidad y una alianza teocrática de alienígenas conocidos como Covenant.',
        'I': 'Nombre del fantasma azul del videojuego de pacman',
        'J': 'Nombre del personaje de overwatch que siempre acompaña a roadhog, suele usar muchas bombas y su forma de ser te hace "Explotar" de la risa'
    }
    respuestas = {
        'A': ['agar.io', "agario"],
        'B': ['Bioshock Infinite', "bioshock infinite","Bioshock","bioshok"],
        'C': ['crash bandicoot','crash'],
        'D': ['doom eternal', 'doom','Doom','Doom Eternal'],
        'E': ['el gato con botas','El gato con botas'],
        'F': ['fornite', 'Fortnite'],
        'G': ['gta', 'GTA'],
        'H': ['halo', 'Halo'],
        'I': ['inky', 'Inky'],
        'J': ['junkrat', 'Junkrat']
    }
    puntos = 0
    for letra in sorted(preguntas.keys()):
        print(f"\n¡Vamos con la letra {letra}!")
        pregunta = preguntas[letra]
        print(pregunta)
        mostrar_animacion(letra_actual=letra)
        
        respuesta = input(Fore.LIGHTWHITE_EX+'Tu respuesta: '+Style.RESET_ALL)
        if respuesta in respuestas[letra]:
            print(Fore.GREEN + "¡Correcto!" + Style.RESET_ALL)
            puntos += 15
        elif respuesta == 'pasapalabra':
            print("¡Pasapalabra! Pasamos a la siguiente.")
            puntos -= 3
        else:
            print(f"{Fore.RED}¡Incorrecto! La respuesta correcta era {respuestas[letra]}.{Style.RESET_ALL}")
    if puntos == 150:       ###Evaluar puntuacion final
        puntos == puntos *2
        animacion_tipeo(Fore.LIGHTGREEN_EX+"\n¡Felicidades, lo hiciste perfecto!"+Style.RESET_ALL)
    else:
        animacion_tipeo("¡Sigue practicando!")
    print(f"{Fore.LIGHTWHITE_EX}Juego terminado. Obtuviste {puntos} puntos.{Style.RESET_ALL}")
    return puntos

def categoria_matematicas(): ####Categoria de matematicas#####
    system("cls")
    preguntas = {
        "A":"Recta que se encuentra asociada a la gráfica de algunas curvas y que se comporta como un límite gráfico hacia la cual la gráfica se aproxima indefinidamente pero nunca la toca ni la cruza",
        "B":"Expresión algebraica formada por la suma o la diferencia de dos términos o monomios.",
        "C":"son las líneas que sirven para determinar la posición de un punto, y los ejes o planos a que se refieren aquellas líneas.",
        "D":"conjunto de todos los posibles valores de entrada de la función. Por ejemplo,  de f(x)=x² consiste de todos los números reales, y  de g(x)=1/x consiste de todos los números reales excepto x=0",
        "E":"Forma de expresar la multiplicación de una expresión por sí misma un número determinado de veces",
        "F":"Relación que hay entre una magnitud y otra, cuando el valor de la primera depende de la segunda.",
        "G":"representación en unos ejes de coordenadas de los pares ordenados de una tabla. describen relaciones entre dos variables."
            "La variable que se representa en el eje horizontal se llama variable independiente o variable x,"
            "La que se representa en el eje vertical se llama variable dependiente o variable y."
            "La variable y está en función de la variable x.",
        "H":"Cual es el lado opuesto al ángulo recto en un triángulo rectángulo, resultando ser su lado de mayor longitud.",
        "I":"se refiere a una operación que resulta en un nuevo conjunto que contiene únicamente los elementos que son comunes a dos o más conjuntos dados.",
        "J":"unidad derivada del Sistema Internacional utilizada para medir energía, trabajo y calor.",
    }
    respuestas = {
        "A": ["Asintota", "asintota"],
        "B": ["Binomio", "binomio"],
        "C": ["Coordenadas", "coordenadas"],
        "D": ["Dominio", "dominio"],
        "E": ["Exponente", "Exponentes", "exponentes", "exponente"],
        "F": ["Funcion", "funcion"],
        "G": ["Grafica", "grafica"],
        "H": ["Hipotenusa", "hipotenusa"],
        "I": ["Interseccion", "interseccion"],
        "J": ["Julios", "julios"]
    }
    puntos = 0  
    for letra in sorted(preguntas.keys()):
        print(f"\n¡Vamos con la letra {letra}!")

        pregunta = preguntas[letra]
        print(pregunta)
        mostrar_animacion(letra_actual=letra)
        respuesta = input('Tu respuesta: ')
        if respuesta in respuestas[letra]:
            print(Fore.GREEN + "¡Correcto!" + Style.RESET_ALL)
            puntos += 15
        elif respuesta == 'pasapalabra':
            print(Fore.LIGHTBLUE_EX + "¡Pasapalabra! Pasamos a la siguiente." + Style.RESET_ALL)
            puntos -= 3
        else:
            print(Fore.RED + f"¡Incorrecto! La respuesta correcta era {respuestas[letra]}." + Style.RESET_ALL)
    if puntos == 150:       ###Evaluar puntuacion final########
        puntos == puntos *2
        animacion_tipeo("\n¡Felicidades, lo hiciste perfecto!")
    else:
        animacion_tipeo("¡Sigue practicando!")
    print(f"Juego terminado. Obtuviste {puntos} puntos.")
    return puntos

def categoria_programacion():   ########## preguntas por default.... falta agregar########
    system("cls")
    preguntas = {
        'A': 'Como se le llama a la variable que posee un conjunto de datos almaenados en la memoria que pueden ser de distinto tipo como entero,decimal,cadena,boleano, esta suele declararse con []',
        'B': 'Tipo de dato que puede tener una variable, este solo puede ser True o False ',
        'C': 'Accion en programacion al unir distintas variables dentro de otra, el mas conocido para realizarlo es usando el signo "+"',
        'D': 'como se le llama a la Variable que contiene una clave y un valor,suele declararse de muchas formas, la mas comun es usando {} ',
        'E': 'Nombre del tipo de dato de variable que solo puede tener numeros no decimales',
        'F': 'como se le llama al fragmento de codigo que no afecta al codigo en general,solamente cuando este es llamado',
        'G': 'Apellido del famoso cofundador de Microsoft',
        'H': 'Nombre de la funcion que te permiten “enganchar” el estado de React y el ciclo de vida desde componentes de función.',
        'I': 'Accion de repetir varias veces algo mediante ya sea un ciclo for o while',
        'J': 'Lenguaje de programacion que ayuda a una mejor interaccion con el usuario en un sitio web'
    }
    respuestas = {
        'A': ['Array','array'],
        'B': ['Boleano','boleano','Bolean','bolean'],
        'C': ['Concatenar','concatenar'],
        'D': ['Diccionario','diccionario'],
        'E': ['Entero','entero'],
        'F': ['Funcion','funcion'],
        'G': ['Gates','gates'],
        'H': ['Hook','hook'],
        'I': ['Iterar','iterar'],
        'J': ['JavaScript','javascript']
    }
    puntos = 0
    for letra in sorted(preguntas.keys()):
        print(f"\n¡Vamos con la letra {letra}!")
        pregunta = preguntas[letra]
        mostrar_animacion(letra_actual=letra)
        print(pregunta)
        respuesta = input('Tu respuesta: ')
        if respuesta in respuestas[letra]:
            print(Fore.GREEN + "¡Correcto!" + Style.RESET_ALL)
            puntos += 15
        elif respuesta == 'pasapalabra':
            print(Fore.LIGHTBLUE_EX + "¡Pasapalabra! Pasamos a la siguiente." + Style.RESET_ALL)
            puntos -= 3
        else:
            print(Fore.RED + f"¡Incorrecto! La respuesta correcta era {respuestas[letra]}." + Style.RESET_ALL)
    if puntos == 150:       ###Evaluar puntuacion final########
        puntos == puntos *2
        animacion_tipeo("\n¡Felicidades, lo hiciste perfecto!")
    else:
        animacion_tipeo("¡Sigue practicando!")
    print(f"Juego terminado. Obtuviste {puntos} puntos.")
    return puntos

def categoria_equipos_fut():  ####Categoria de quipos de futbol#####
    system("cls")
    preguntas = {
        'A': 'Selección de fútbol que tiene 4 copas del mundo en sus vitrinas.',
        'B': 'Pais donde se jugo el mundial en 2014.',
        'C': 'Equipo de fútbol profesional con sede en Guadalajara.',
        'D': 'Nombre de jugar leyenda de argentina con apellido "Maradona".',
        'E': 'Pais donde se encuentra la sede el FC Barcelona.',
        'F': 'Equipo ganador del mundial 2018.',
        'G': 'Selección importante del continente africano.',
        'H': 'Equipo que le robo un penal a mexico en el mundial 2014.',
        'I': 'Apellido de futbolista sueco que por nombre lleva "Zlatan".',
        'J': 'Nombre de exfutbolista mexicano portero que destaco en la década de los 90, Usaba trajes de colores muy llamativos.'
    }
    respuestas = {
        'A': 'alemania',
        'B': 'brasil',
        'C': 'chivas',
        'D': 'diego',
        'E': 'españa',
        'F': 'francia',
        'G': 'ghana',
        'H': 'holanda',
        'I': 'ibrahimovic',
        'J': 'jorge'
    }
    
    puntos = 0
    for letra in sorted(preguntas.keys()):
        print(f"¡Vamos con la letra {letra}!")
        pregunta = preguntas[letra]
        print(pregunta)
        mostrar_animacion(letra_actual=letra)
        respuesta = input('Tu respuesta: ')
        respuesta = respuesta.lower()
        if respuesta == respuestas[letra]:
            print(Fore.GREEN + "¡Correcto!" + Style.RESET_ALL)
            puntos += 15
            
        elif respuesta == 'pasapalabra':
            print(Fore.LIGHTBLUE_EX + "¡Pasapalabra! Pasamos a la siguiente." + Style.RESET_ALL)
            puntos -= 3
        else:
            print(f"{Fore.RED}¡Incorrecto! La respuesta correcta era {respuestas[letra]}.{Style.RESET_ALL}")
            
        #pausa de dos segundos antes de pasar a la siguiente pregunta
    if puntos == 150:       ###Evaluar puntuacion final######
        puntos == puntos *2
        animacion_tipeo("¡Felicidades, lo hiciste perfecto!")
    else:
        animacion_tipeo("¡Sigue practicando!")

    print(f"Juego terminado. Obtuviste {puntos} puntos.")
    return puntos

def verificar_usuario(nombres):
    user = input(Fore.LIGHTGREEN_EX+"Ingrese el nombre del jugador que jugara: "+Style.RESET_ALL)
    if user in nombres:
        guardar_archivo(user)
    else:
        input(Fore.RED+"Usuario no encontrado, vuelve a indicar otro nombre. Presiona enter para continuar..."+Style.RESET_ALL)
        return verificar_usuario(nombres) 
    return

def guardar_archivo(user):
    respuesta = input(f"Desea guardar el archivo como '{user}_puntuacion.txt' ? (S/N): ")
    if respuesta.lower() == "s":
        try:
            with open(f"{user}_puntuacion.txt", "w") as archivo:
                archivo.write("Contenido del archivo")
            input("Archivo guardado exitosamente. \nPresiona enter para continuar...")
        except IOError:
            print("Error al guardar el archivo.")
    else:
        input("Archivo no guardado. \n El jugador pude jugar pero se perderan los datos una vez finalice el juego.\n Presiona enter para continuar.")
    return                            
                
def jugar(nombres):
    system("cls")
    #verificar_usuario(nombres)
    print(Fore.LIGHTMAGENTA_EX+"Has seleccionado la opción Juego."+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX+'Elija una catergoria...\n'+Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX+'1.- Juegos \n2.- Programacion \n3.- Equipos de futbol \n4.-Matematicas'+Style.RESET_ALL)
    categoria = int(input(' '))
    if categoria == 1 :
        puntos = categoria_juegos()
    elif categoria == 2:
        puntos = categoria_programacion()
    elif categoria == 3:
        puntos = categoria_equipos_fut()
    elif categoria == 4:
        puntos = categoria_matematicas()
    else:
        print(Fore.RED+'ERROR. CATEGORIA NO INCLUIDA'+Style.RESET_ALL)
        time.sleep(2)
        input(Fore.YELLOW+"Presione enter para continuar..."+Style.RESET_ALL)
        return jugar(nombres)
    return puntos

##### Main #####
def main():
    init()
    nombres = []
    puntuajes_usuario = {}
    usuario = ""
    n = 0
    in_menu = True
    system("cls")
    print(Cursor.POS(15, 2) + Fore.LIGHTWHITE_EX + " \t\t\t\t\t\t----------------------------Pasapalabras--------------------------\n" + Style.RESET_ALL)
    #time.sleep(2)
    print(Cursor.POS(15, 3) + Fore.LIGHTWHITE_EX +" \t\t\t\t\t\t---------------------------¡Bienvenido!----------------------------\n"+ Style.RESET_ALL)
    #time.sleep(2)
    while True:
        while in_menu == True:
            print(Cursor.POS(8, 4) +Fore.LIGHTWHITE_EX + "\t\t\t\t\t\t\t\t\tSeleccione una opción del menú: "+ Style.RESET_ALL)
            usuarios = []
            print(Cursor.POS(9, 5) +Fore.LIGHTWHITE_EX + "\t\t\t\t\t\t\t\t-=========MENU=========-\n"+ Style.RESET_ALL)
            #time.sleep(1)
            print(Cursor.POS(10, 6) +Fore.LIGHTWHITE_EX + "\t\t\t\t\t\t\t\t-1. Registro-\n"+ Style.RESET_ALL)
            #time.sleep(1)
            print(Cursor.POS(10, 7) +Fore.LIGHTWHITE_EX + "\t\t\t\t\t\t\t\t-2. Ver puntuación-\n"+ Style.RESET_ALL)
            #time.sleep(1)
            print(Cursor.POS(10, 8) +Fore.LIGHTWHITE_EX + "\t\t\t\t\t\t\t\t-3. Jugar-\n"+ Style.RESET_ALL)
            #time.sleep(1)
            print(Cursor.POS(10, 9) +Fore.LIGHTWHITE_EX + "\t\t\t\t\t\t\t\t-4. Salir-\n"+ Style.RESET_ALL)
            #time.sleep(1)
            try:
                seleccion = int(input(Cursor.POS(8, 10) + "\t\t\t\t\t\t\t\t\t¿Qué desea hacer? "))
                if seleccion >= 1 and seleccion <= 4:
                    in_menu = False
                    break
                else:
                    print(Fore.RED+"Numero fuera de rango, ingrese un numero del 1 al 4 de las opcioens del menu."+Style.RESET_ALL)
            except:
                print(Fore.LIGHTYELLOW_EX+"Solo se permiten numero enteros positivos del 1 al 4."+Style.RESET_ALL)
                
        while in_menu == False:
            if seleccion == 1:
                usuario = registro(nombres) #Ejecutar el registro y verificacion del usuario
                if usuario in nombres:
                    input(Fore.LIGHTGREEN_EX+"Usuario registrado con exito, presione enter para continuar..."+Style.RESET_ALL)
                    puntuajes_usuario[usuario] = {
                        'partidas': [],
                        'puntuaciones': []
                    }
                    system("cls")
                    in_menu = True
                    break
            elif seleccion == 2:
                ver_puntuacion(puntuajes_usuario, puntuajes_usuario)
                in_menu = True
                break
            elif seleccion == 3:
                user = input(Fore.LIGHTWHITE_EX+"Introduce el nombre del jugador: "+Style.RESET_ALL)
                if user.isnumeric():
                    input(Fore.RED+"Solo se permiten texto."+Style.RESET_ALL)
                elif user not in nombres:
                    resp = input(Fore.LIGHTYELLOW_EX+"Usuario no registrado, ¿desea registrar? ingresa la letra s para confirmar y n para no hacer el registro"+Style.RESET_ALL)
                    if resp.lower() == "s":
                        usuario = registro(nombres)
                        puntuajes_usuario[usuario] = {
                        'partidas': [],
                        'puntuaciones': []
                    }
                        if usuario in nombres:
                            input(Fore.LIGHTGREEN_EX+"Usuario registrado con extio."+Style.RESET_ALL)
                    if resp.lower() == "n":
                        input(Fore.LIGHTYELLOW_EX+"Es necesario un nombre de usuario para jugar y registrar su puntuación."+Style.RESET_ALL)
                else:
                    puntos = jugar(nombres)
                    if puntuajes_usuario[user]['partidas'] == []:
                        n = 1
                        puntuajes_usuario[user]['partidas'].append(n)
                        puntuajes_usuario[user]['puntuaciones'].append(puntos)
                    else:
                        n += 1
                        puntuajes_usuario[user]['partidas'].append(n)
                        puntuajes_usuario[user]['puntuaciones'].append(puntos)
                    input(Fore.LIGHTYELLOW_EX+"Presione enter para continuar..."+Style.RESET_ALL)
                    system("cls")
                    in_menu = True  
                    break
            elif seleccion == 4:
                system("cls")
                print(Fore.LIGHTWHITE_EX+"Gracias por jugar..."+Style.RESET_ALL)
                time.sleep(1.0)
                system.exit()
            else:
                input(Fore.RED+"Opción no válida. Presione enter para continuar..."+Style.RESET_ALL)
main()