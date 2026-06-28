from eii_utils import ( limpiar_consola, mostrar_menu, leer_entero, leer_entero_opcional, leer_flotante, leer_flotante_opcional, leer_texto,leer_texto_opcional,leer_booleano, imprimir_titulo_decorado, pausar)

def mostar_menu_principal() -> int:
    """
    Muestra el menú principal y devuelve la opción elegida por el usuario.
    """
    limpiar_consola()
    return mostrar_menu(
        "Laboratorio Colíbri",
        [
            "Cargar datos prueba",
            "Ver inventario",
            "Ver producto / materia prima",
            "Agregar producto / materia prima",
            "Modificar producto / materia prima",
            "Eliminar producto / materia prima",
            "Ver materias primas",
            "Ver productos finales",
            "Agregar materia prima a producto final",
            "Mostrar disponibilidad requerimientos por producto"
        ],
    )

def mostar_final() -> None:
    """
    Muestra un mensaje de despedida cuando el usuario sale del programa.
    """
    limpiar_consola()
    imprimir_titulo_decorado("Muchas gracias por usar nuestra aplicación")

pausar()



#Voy a agregar lo que trabaje apartir de acá por cualquier cosa
# vista.py
# Interfaz de usuario del sistema Planta Colibrí

from eii_utils import leer_rango_enteros, limpiar_consola, leer_entero, pausar, mostrar_menu, imprimir_titulo_decorado

#Función 1: Muestra el menú principal
def mostrar_menu_principal()  -> int: 
    '''
    Le muestra el menú principal al usuario y le devuelve la opción que escogió

    Retorna: 
    int: La opción que el usuario escogió
    '''
    limpiar_consola()
    return mostrar_menu( 
        'SISTEMA PLANTA COLIBRÍ',
        [ 'REGISTRAR TURNO DE PRODUCCIÓN',
          'VER REPORTE',
          'VER ESTADÍSTICAS'
        ],

    )

#Función 2: Pide la cantidad de turno del día
def pedir_cantidad_turnos() -> int:
    '''
     Solicita al operario la cantidad de turnos del día.

    Retorna:
    int: Cantidad de turnos entre el 1 y el 3.
     '''
    limpiar_consola()
    imprimir_titulo_decorado('SISTEMA DE PRODUCCIÓN - PLANTA COLIBRÍ')
    return leer_rango_enteros("Cantidad de turnos del dia", 1, 3)

#Función 3: Mostrar el encabezado del turno actual
def pedir_datos_turno(numero_turno):
    '''
    Muestra el encabezado por el apartado del turno en la pantalla del usuario
    
    Parámetros:
    numero_turno (int): Número del turno a procesar
    '''
    limpiar_consola()
    imprimir_titulo_decorado('REPORTE DE TURNO #' + str(numero_turno) + '- PLANTA COLIBRÍ')

#Función 4: Pide la cantidad de lineas activas que hubo en cada turno 
def pedir_cantidad_lineas() -> int:
    '''
    Le solicita al operario la cantidad de lineas activas en cada turno del día

    Retorna: 
    int: Cantidad de lineas activas entre el 1 y el 3. 
    '''
    return leer_rango_enteros('Cantidad de lineas activas en el turno', 1, 3)

#Función 5: Pedir los datos que genera cada linea activa. 
def pedir_datos_linea() -> dict:
    '''
    Le solicita al operario los datos que la línea generó durante el día

    Retorna:

    dict: Diccionario con nombre, producidas y rechazadas.
    '''
    nombre = input ('Inserte el nombre o número de la línea: ')
    producidas = leer_entero('Inserte la cantidad de botellas producidas')
    rechazadas = leer_entero('Inserte la cantidad de botellas rechazadas')

    return {'nombre': nombre, 'producidas': producidas, 'rechazadas': rechazadas} 

#Función #6: Muestra el reporte al usuario
def mostrar_reporte(reporte: str)  -> None:
    '''
    Muestra el reporte del turno del cual se ingresaron los datos
    Parámetros: 
    reporte (str): Esta variable es el texto del reporte a mostrar.
    '''
    limpiar_consola()
    print(reporte)
    pausar()

def mostrar_datos_linea_correctos(linea: dict) -> None:
    '''
    Muestra los datos de las líneas de producción con un formato diferente al de el diccionario

    Parámetros: 
    linea (dict): Diccionario con nombre, producidas y rechazadas.
    '''
   print(linea["nombre"] + ": " + str(linea["producidas"]) + " producidas | " + 
          str(linea["rechazadas"]) + " rechazadas | Eficiencia: " + 
          str(round(linea["eficiencia"], 2)) + "%"
        )
def mostrar_mensaje(mensaje: str) -> None:
    """
    Muestra un mensaje general en pantalla, ayuda a que no se rompa la funcionalidad del modelo MVC el mensaje que vaya a salir para por vista. 

    Parámetros:
    mensaje (str): El texto a mostrar que se escoja dentro del controlador.
    """
    print(mensaje)
