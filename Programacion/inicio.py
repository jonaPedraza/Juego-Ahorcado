import os #permite ejecutar clear (para limpiar la pantalla)
import time #pausar la ejecución del programa por unos segundo

## -----FUNCION LIMPIAR PANTALLA-------
def limpiar_pantalla(): 
    if os.name == 'nt':     # Verifica si el sistema operativo es Windows ('nt') o Unix/Linux/macOS ('posix')
        os.system('cls')    #una vez verificado reseta
    else:
        os.system('clear')  #caso contrario limpia
        
#    Funcion mostrar pantalla de bienvenida y la borra al continuar."""
def interfaz_bienvenida():
    ancho = 80 # Definimos un ancho para centrar el texto
    limpiar_pantalla()
    print("================================".center(ancho))
    print("    ¡Bienvenido al Ahorcado!    ".center(ancho))
    print("================================".center(ancho))
    print("\nPresiona Enter para empezar...".center(ancho))
    input() #Espera a que el jugador presione la tecla Enter
    limpiar_pantalla()      #limpia nuevamente la pantalla

# Nota: No ejecutes nada aquí, solo define las funciones.
# La llamada a la función se hará desde el otro archivo.