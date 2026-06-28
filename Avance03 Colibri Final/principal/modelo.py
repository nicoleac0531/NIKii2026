#modelo.py
#Calculos del sistema de la Planta Colibrí

#Función 1: calcular_eficiencia(producidas, rechazadas)

def calcular_eficiencia(producidas, rechazadas):
    '''Calcula el porcentaje de eficiencia de una determinada línea de producción
    
    Parámetros: 
    producidas (int): Cantidad de bottelas producidas en la línea evaluada.
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




#Función 5: 








#Función para generar un resumen de todo el día 
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
    lineas.append('Total producido: ' + str(gran_total_producido) + 'botellas3')
    lineas.append('Turno más eficiente: ' + str(mejor_turno_numero) + str(round(mejor_turno_eficiencia, 2)) + '%')
    lineas.append('Turno menos eficiente: ' + str(peor_turno_eficiencia) + str(round(peor_turno_eficiencia, 2)) + '%')

    return '\n'.join(lineas)
