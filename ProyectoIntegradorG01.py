#Programa de control de calidad de la Planta Colibri
operario_revision: str = ''
botellas_producidas: int = 0
botellas_defectuosas: int = 0
porcentaje_defectos: float = 0.0
mensaje:str = ''

#Input

# 1. Pedir al usuario el nombre del operario que está haciendo la revisión.
operario_revision = str ( input ("Digite el nombre del operario a cargo de la revisión "))

# 2. Pedir el número de botellas producidas en el turno (número entero)
botellas_producidas = int ( input ("Digite el número de botellas producidas en el turno "))

# 3. Pedir el número de botellas defectuosas encontradas (número entero)
botellas_defectuosas = int ( input ("Digite el número de botellas defectuosas "))

#Process

# 4. Calculo del porcentaje de defectos (defectuosas / producidas * 100)
porcentaje_defectos=(botellas_defectuosas/botellas_producidas)*100

if porcentaje_defectos <= 5.0:
    mensaje = "Meta cumplida"
else: 
    mensaje = "Meta no cumplida"

#Output

# 5. Mostrar un mensaje que diga si el turno cumplió o no la meta de calidad (< 5%)
print ("El resultado es: " + mensaje )
