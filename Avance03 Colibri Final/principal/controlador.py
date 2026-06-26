from eii_utils import pausar
import principal.vista as vista
import principal.modelo as modelo

def opcion_uno() -> None:
    producidas: int = 0
    rechazadas: int = 0

    modelo.calcular_eficiencia(producidas, rechazadas)

    pausar()

def ejecutar() -> None:

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