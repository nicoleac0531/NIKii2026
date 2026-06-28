Ahora sí están corregidos los dos errores. Solo falta agregar las funciones de Mario y actualizar los imports. Te paso la vista completa con todo incluido:

```python
# vista.py
# Interfaz de usuario del sistema Planta Colibrí
from eii_utils import leer_rango_enteros, limpiar_consola, leer_entero, leer_flotante, leer_texto, pausar, mostrar_menu, imprimir_titulo_decorado

# Función 1: Muestra el menú principal
def mostrar_menu_principal() -> int: 
    '''
    Le muestra el menú principal al usuario y le devuelve la opción que escogió
    Retorna: 
    int: La opción que el usuario escogió
    '''
    limpiar_consola()
    return mostrar_menu(
        "SISTEMA PLANTA COLIBRÍ",
        [
            "REGISTRAR TURNO DE PRODUCCIÓN",
            "ESTADO OPERATIVO DE MÁQUINAS",
            "VER REPORTE",
            "VER ESTADÍSTICAS",
        ]
    )

# Función 2: Pide la cantidad de turnos del día
def pedir_cantidad_turnos() -> int:
    '''
    Solicita al operario la cantidad de turnos del día.
    Retorna:
    int: Cantidad de turnos entre el 1 y el 3.
    '''
    limpiar_consola()
    imprimir_titulo_decorado('SISTEMA DE PRODUCCIÓN - PLANTA COLIBRÍ')
    return leer_rango_enteros("Cantidad de turnos del dia", 1, 3)

# Función 3: Mostrar el encabezado del turno actual
def pedir_datos_turno(numero_turno):
    '''
    Muestra el encabezado del turno en la pantalla del usuario
    Parámetros:
    numero_turno (int): Número del turno a procesar
    '''
    limpiar_consola()
    imprimir_titulo_decorado('REPORTE DE TURNO #' + str(numero_turno) + '- PLANTA COLIBRÍ')

# Función 4: Pide la cantidad de líneas activas en cada turno
def pedir_cantidad_lineas() -> int:
    '''
    Le solicita al operario la cantidad de líneas activas en cada turno del día
    Retorna: 
    int: Cantidad de líneas activas entre el 1 y el 3. 
    '''
    return leer_rango_enteros('Cantidad de lineas activas en el turno', 1, 3)

# Función 5: Pedir los datos que genera cada línea activa
def pedir_datos_linea() -> dict:
    '''
    Le solicita al operario los datos que la línea generó durante el día
    Retorna:
    dict: Diccionario con nombre, producidas y rechazadas.
    '''
    nombre = input('Inserte el nombre o número de la línea: ')
    producidas = leer_entero('Inserte la cantidad de botellas producidas')
    rechazadas = leer_entero('Inserte la cantidad de botellas rechazadas')
    return {'nombre': nombre, 'producidas': producidas, 'rechazadas': rechazadas}

# Función 6: Muestra el reporte al usuario
def mostrar_reporte(reporte: str) -> None:
    '''
    Muestra el reporte del turno del cual se ingresaron los datos
    Parámetros: 
    reporte (str): El texto del reporte a mostrar.
    '''
    limpiar_consola()
    print(reporte)
    pausar()

def mostrar_datos_linea_correctos(linea: dict) -> None:
    '''
    Muestra los datos de las líneas de producción con formato legible
    Parámetros: 
    linea (dict): Diccionario con nombre, producidas y rechazadas.
    '''
    print(linea["nombre"] + ": " + str(linea["producidas"]) + " producidas | " + 
          str(linea["rechazadas"]) + " rechazadas | Eficiencia: " + 
          str(round(linea["eficiencia"], 2)) + "%")

def mostrar_mensaje(mensaje: str) -> None:
    """
    Muestra un mensaje general en pantalla.
    Parámetros:
    mensaje (str): El texto a mostrar.
    """
    print(mensaje)

def mostrar_despedida() -> None:
    '''
    Muestra el mensaje de cierre para el sistema
    '''
    limpiar_consola() 
    print('Sesión finalizada')



# -------- Funciones de la Función modularizada 5 (Mario) : estado operativo de máquinas-----------

# Función para pedir los datos de la máquina al usuario
def pedir_datos_maquina() -> dict:
    '''
    Se encarga de solicitar al usuario los datos de la máquina que va a evaluar.
    Retorna:
    dict: Diccionario con nombre_maquina, fallas_semana y tiempo_inactividad_horas.
    '''
    limpiar_consola()
    imprimir_titulo_decorado('ESTADO DE MÁQUINAS - PLANTA COLIBRÍ')
    nombre_maquina = leer_texto('Ingrese el nombre de la máquina')
    fallas_semana = leer_entero('Ingrese la cantidad de fallas en la semana')
    tiempo_inactividad_horas = leer_flotante('Ingrese el tiempo de inactividad en horas')
    return {'nombre_maquina': nombre_maquina, 'fallas_semana': fallas_semana, 'tiempo_inactividad_horas': tiempo_inactividad_horas}

# Función para mostrar el estado de la máquina
def mostrar_estado_maquina(resultado: str) -> None:
    '''
    Muestra el resultado del estado operativo de la máquina evaluada.
    Parámetros:
    resultado (str): Texto con la evaluación de la máquina.
    '''
    limpiar_consola()
    imprimir_titulo_decorado('DIAGNÓSTICO DE MÁQUINA')
    print(resultado)
    pausar()

#FUNCIONALIDAD 3 - PARA VEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEER

def opcion_ver_historial():
    """
    Pide al usuario la fecha del reporte que desea consultar
    y lo muestra en pantalla si existe.
    """
    print("Reportes históricos")
    print("Formato de fecha: YYYY-MM-DD  (ejemplo: 2026-06-25)")

    fecha_ingresada = input("Ingrese la fecha del reporte: ").strip()
    nombre_archivo = f"reporte_{fecha_ingresada}.txt"

    contenido = controlador.ejecutar_leer_reporte(nombre_archivo)

    if contenido:
        print(f"Contenido de '{nombre_archivo}'")
        print(contenido)
    else:
        print(f"No se encontró un reporte para la fecha '{fecha_ingresada}'.")
