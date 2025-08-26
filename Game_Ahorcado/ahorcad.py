# Importa la función 'interfaz_bienvenida' del archivo 'inicio.py'
from inicio import interfaz_bienvenida

# Importar los dibujos desde el nuevo archivo 'dibujos.py'
from dibujos import dibujo_ahorcado

import random #permite obtener de forma aleatoria un palabra del array

#Funcion para obetner palabra
def obtener_palabra():
    lista_palabras=["perro","gato","comida","video","ahorcado"]
    palabra_aleatoria=random.choice(lista_palabras)
    return palabra_aleatoria

#Funcion para palabra secreta, para mostrar el estado actual del juego
def mostrar_palabra(palabra_secreta, letras_adivinadas):
    ancho=80
    palabra=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas: #compara si esta dentro de letras adivinadas
            palabra+=letra #aumento contador
        else:
            palabra+="_" #aumento un guion bajo en la palabra
    print(palabra.center(ancho))
    

#funcion principal del juego del ahorcado
def jugar_ahorcado():
    palabra_secreta=obtener_palabra()
    letras_adivinadas=set() #incia como conjunto vacio y se usa para almacenar letras
    intentos_restantes=6
    ancho = 80 
    # Llama a la función de bienvenida que importaste
    interfaz_bienvenida()
    
    while intentos_restantes>0:
        # Se imprime el dibujo del ahorcado según los intentos restantes
        print(dibujo_ahorcado[6 - intentos_restantes].center(ancho))
        
        mostrar_palabra(palabra_secreta, letras_adivinadas)
        print(f"Te quedan {intentos_restantes} intentos.")
        print(f"Letras usadas: {' '.join(sorted(list(letras_adivinadas)))}") #sorted es para orden alfabetico y el join para agregar
        
        letra=input("Introduce una letra: ").lower() #la transformor a miniscula
       
        #Condicion si la letra ingresada es mas de 1 letra o es un numero
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue
        
        #Condicion si la letra ingresada se repite
        if letra in letras_adivinadas:
            print(f"Letra ya ingresada, ingrese una letra")
            continue #me salto todos los demas pasos y regreso al inicio de while
        
        # Se agrega la letra ingreasda al conjunto de letras usadas
        letras_adivinadas.add(letra) #para añadir letras al conjutno vacio
        
        if letra in palabra_secreta:
            print("\n")
            print("¡Letra correcta!")
            if set(letras_adivinadas).issuperset(set(palabra_secreta)): #set permite crear un conjutno de elemento unicos, es decir elmina los du
                print("\n")
                print("------F E L E C I D A D E S------".center(ancho))
                print("---------------------------------".center(ancho))
                print("Gano el Jugador".center(ancho))
                print("---------------------------------".center(ancho))
                print(f"La palabra era: {palabra_secreta}".center(ancho))
                print("---------------------------------".center(ancho))
                break
        else:
            intentos_restantes-=1
            print("\n")
            print("¡Letra incorrecta!")
    
    if intentos_restantes==0:
        print(dibujo_ahorcado[6].center(ancho))
        print("\n")
        print("-------G A M E    O V E R--------".center(ancho))
        print("---------------------------------".center(ancho))
        print("Has perdido el juego!".center(ancho))
        print("---------------------------------".center(ancho))
        print(f"La palabra era: {palabra_secreta}".center(ancho))
        print("---------------------------------".center(ancho))
        
    

# ---  Lógica para jugar múltiples partidas con la repeticion WHILE ---
continuar_jugando = "si"
while continuar_jugando.lower() == "si": #le hace minisculas sin importar lo que ingrese el usuario
                                        #se repite mientras la repsuesta sea SI
    # Llama a la función de principal del juego       
    jugar_ahorcado()
    print("\n¿Quieres jugar de nuevo? (si/no)")
    continuar_jugando = input().lower()

print("¡Gracias por jugar!")

