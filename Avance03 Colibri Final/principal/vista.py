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