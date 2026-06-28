#modelo.py
#Calculos del sistema de la Planta Colibrí

#Función 1: calcular_eficiencia(producidas, rechazadas)
import datetime

def calcular_eficiencia(producidas, rechazadas):
    '''Calcula el porcentaje de eficiencia de una determinada línea de producción
    
    Parámetros: 
    producidas (int): Cantidad de botellas producidas en la línea evaluada.
    rechazadas (int): Cantidad de botellas rechazadas en la línea evaluada.

    Retorna:
    float: El nivel de eficiencia expresado en formato de porcentaje (%).
    '''
    if producidas == 0:
        return 0.0
    return (producidas - rechazadas) / producidas * 100

#Función 2: linea_mas_eficiente(lista_lineas)

def linea_mas_eficiente(lista_lineas):
    '''Recibe una lista de líneas y devuelve cual fue la más eficiente de todas
    
    Parámetros: 
    lista_lineas (list): Lista de diccionarios con los datos de cada línea.

    Retorna:
    str: El nombre de cual fue la línea con el mayor porcentaje de eficiencia.
    '''
    mejor_nombre= ''
    mejor_eficiencia= -1  
    for linea in lista_lineas:
        eficiencia = calcular_eficiencia(linea['producidas'], linea['rechazadas'])  # ✅ Fix
        if eficiencia > mejor_eficiencia:
            mejor_eficiencia = eficiencia
            mejor_nombre = linea['nombre']
    return mejor_nombre

#Función 3: validar_produccion(valor)

def validar_produccion(valor):
    '''Verifica si el valor ingresado es un número entero positivo o es otro caso
    
    Parámetros:
    valor(): El valor a verificar. 

    Retorna: 
    bool: True si es un entero positivo, False en cualquier otro caso que se de.
    '''
    try: 
        numero = int(valor)
        return numero > 0
    except:
        return False

#Función 4: 

#La siguiente función 04 del programa trabajará reportes del turno.
#Se procesará información cuantitativa de los turnos del día ingresados por el usuario.
#Asimismo, el sistema devolverá información cualitativa en un informe completo detallado al usuario. 

def generar_reporte_turno(numero_turno, lista_lineas):
    """
    Genera el reporte del turno como texto

    Parámetros: 
    numero_turno (int): Número del turno a reportar.
    lista_lineas (list): Lista de diccionarios con los datos de cada linea.

    Retorna: 
    str: El reporte completo del turno.
    """ 

    #Se genera las variables clave para que el usuario ingrese los valores de producción del turno.
    total_producidas = 0
    total_rechazadas = 0 

    #Se realiza el inicio del programa para el usuario.
    reporte = f"   Reporte del turno No.{numero_turno}  \n"
    reporte += "Linea\tProducidas\tRechazadas\tEficiencia\n"  

    #Inicia el ciclo para revisar las listas.
    for linea in lista_lineas: 

    #Luego, se extrae los datos de cada diccionario de forma directa.
        nombre = linea["nombre"]
        producidas = linea["producidas"]
        rechazadas = linea["rechazadas"]
            
    #Se realiza una suma de los totales
        total_producidas += producidas
        total_rechazadas += rechazadas
            
    #Se realiza un calculo de la eficiencia de la línea ingresada.
        
        eficiencia = calcular_eficiencia(producidas, rechazadas)
                
    #Se separa las columnas con un espacio largo para que queden ordenadas
        reporte += f"{nombre}\t{producidas}\t{rechazadas}\t{eficiencia:.1f}%\n" 
            
    #Finalmente, se calcula los totales del turno completo.
        
    eficiencia_global = calcular_eficiencia(total_producidas, total_rechazadas)
            
    #Reporte de salida al usuario.
    reporte += " \n" 
    reporte += f"Total Producidas: {total_producidas}\n"
    reporte += f"Total Rechazadas: {total_rechazadas}\n"
    reporte += f"Eficiencia Global: {eficiencia_global:.1f}%\n"
        
    #Se genera un texto final.
    return reporte

#Función 5 (Libre): 

# Resuelve el problema de Mario: Determinar el estado operativo de cada máquina de la Planta Colibrí en  base a su historial de fallas y tiempo de parada.

def calcular_estado_maquina(nombre_maquina: str, fallas_semana: int, tiempo_inactividad_horas: float) -> str:
    '''
    Se encarga de evaluar el estado operativo de una máquina de la planta según la cantidad de fallas en la semana y el tiempo de inactividad.

    Parametros:
        nombre_maquina (str): Nombre de la maquina a evaluar.
        fallas_semana (int): Cantidad de fallas que tuvo la máquina en la semana. 
        tiempo_inactividad_horas (float): Tiempo total en horas que la máquina estuvo inactiva.


    Retorna: 
        str: Estado de la máquina: "NORMAL: La máquina está funcionando correctamente", "ALERTA: la máquina presenta fallas moderadas" o "CRÍTICO: La máquina ha presentado muchas fallas, se recomienda mantenimiendo preventivo".
        Y incluye el nombre de la máquina en el mensaje.  

    '''
    
    # Evaluar el estado de la máquina según las condiciones

    # ESTADO CRÍTICO: muchas fallas o tiempo de inactividad muy largo 

    if fallas_semana >= 4 or tiempo_inactividad_horas >= 10: 
        estado = f"CRÍTICO: La máquina {nombre_maquina} ha presentado muchas fallas, se recomienda mantenimiento preventivo."

    # ESTADO DE ALERTA: algunas fallas o tiempo de inactividad moderado    
    elif fallas_semana >= 2 or tiempo_inactividad_horas >= 4: 
        estado = f"ALERTA: La máquina {nombre_maquina} presenta fallas moderadas, se recomienda revisión."
    
    # ESTADO NORMAL: pocas fallas y tiempo de inactividad corto
    else: 
        estado = f"NORMAL: La máquina {nombre_maquina} está funcionando correctamente."
    
    return f"Máquina: {nombre_maquina} \nFallas presentadas en la semana: {fallas_semana} \nTiempo de inactividad (horas): {tiempo_inactividad_horas} \nEstado operativo: {estado}"

def salvar_reporte(contenido_reporte: str) -> str:

    fecha = datetime.date.today()
    nombre_archivo = f'reporte_{fecha}.txt'
    
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido_reporte)
    
    return nombre_archivo  

# Función para generar un resumen de todo el día 
def generar_resumen_dia(gran_total_producido, mejor_turno_numero, mejor_turno_eficiencia, peor_turno_numero, peor_turno_eficiencia):
    '''
    Genera un resumen global de los datos de todo el día

    Parámetros: 
    gran_total_producido (int): Total de botellas producidas en el día.
    mejor_turno_numero (int): Nombre del turno más eficiente.
    mejor_turno_eficiencia (float): Eficiencia del mejor turno.
    peor_turno_numero (int): Nombre del turno menos eficiente.
    peor_turno_eficiencia (float): Eficiencia del peor turno.

    Retorna:
    str: El resumen global del día como texto.
    '''
    lineas = []
    lineas.append('RESUMEN GLOBAL DEL DÍA - PLANTA COLIBRÍ')
    lineas.append('Total producido: ' + str(gran_total_producido) + ' botellas')
    lineas.append('Turno más eficiente: #' + str(mejor_turno_numero) + ' (' + str(round(mejor_turno_eficiencia, 2)) + '%)')
    lineas.append('Turno menos eficiente: #' + str(peor_turno_numero) + ' (' + str(round(peor_turno_eficiencia, 2)) + '%)')

    resumen = '\n'.join(lineas)
    salvar_reporte(resumen)
    return resumen


def leer_reporte(nombre_archivo: str) -> str:
    '''
    Lee el contenido de un reporte guardado.
    Retorna un mensaje si el archivo no existe.
    '''
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        return 'Archivo no encontrado.'
