# controlador.py

import modelo
import vista
from eii_utils import pausar


#Genera el reporte del turno

def registrar_turno() -> None:
    cantidad_turnos = vista.pedir_cantidad_turnos()

    gran_total_producido = 0
    gran_total_rechazado = 0
    peor_turno_numero = 0
    peor_turno_eficiencia = 101
    mejor_turno_numero = 0
    mejor_turno_eficiencia = -1

    for numero_turno in range(1, cantidad_turnos + 1):
        vista.pedir_datos_turno(numero_turno)
        cantidad_lineas = vista.pedir_cantidad_lineas()

        lista_lineas = []
        total_producido = 0      
        total_rechazado = 0      

        for _ in range(cantidad_lineas):
            linea = vista.pedir_datos_linea()
            linea["eficiencia"] = modelo.calcular_eficiencia(
                linea["producidas"], linea["rechazadas"]
            )
            total_producido += linea["producidas"]    
            total_rechazado += linea["rechazadas"]    
            lista_lineas.append(linea)
            vista.mostrar_datos_linea_correctos(linea)
            
        reporte = modelo.generar_reporte_turno(numero_turno, lista_lineas)
        vista.mostrar_reporte(reporte)


         #Acumaladores

        eficiencia_turno = modelo.calcular_eficiencia(total_producido, total_rechazado)
        gran_total_producido += total_producido
        gran_total_rechazado += total_rechazado

        if eficiencia_turno < peor_turno_eficiencia:
            peor_turno_eficiencia = eficiencia_turno
            peor_turno_numero = numero_turno

        if eficiencia_turno > mejor_turno_eficiencia:
            mejor_turno_eficiencia = eficiencia_turno
            mejor_turno_numero = numero_turno


    resumen = modelo.generar_resumen_dia(gran_total_producido, mejor_turno_numero, mejor_turno_eficiencia, peor_turno_numero, peor_turno_eficiencia)
    vista.mostrar_reporte(resumen)

#FALTA AGREGAR LO DEL CONTROLADOR DEL MENU Y LAS FUNCIONALIDADES 3 Y 4
    
    
    opcion: int = -1
    while opcion != 0:
        opcion = vista.mostar_menu_principal()
        match opcion:
            case 1:
                opcion_uno()
            case 2:
                print("LUEGO")
            case 3:
                print("LUEGO")
            case 4:
                print("LUEGO")
            case 5:
                print("LUEGO")
            case 6:
                print("LUEGO")
            case 7:
                print("LUEGO")
            case 8:
                print("LUEGO")
            case 9:
                print("LUEGO")
            case 0:
                vista.mostar_final()
