# main.py

from eii_utils import limpiar_consola, leer_rango_enteros, pausar
import principal.controlador as controlador
from colorama import Fore, Style

if __name__ == "__main__":
    limpiar_consola()
    controlador.ejecutar()


