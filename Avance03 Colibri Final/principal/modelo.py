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
        if linea['eficiencia'] > mejor_eficiencia:
            mejor_eficiencia = linea ['eficiencia']
            mejor_nombre = linea ['nombre']
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