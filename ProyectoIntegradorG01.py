operario_revision: str = ''
botellas_producidas: int = 0
botellas_defectuosas: int = 0
porcentaje_defectos = float = 0.0
mensaje:str = ''

#Input
operario_revision = str ( input ("Digite el nombre del operario a cargo de la revisión "))
botellas_producidas = int ( input ("Digite el número de botellas producidas en el turno "))
botellas_defectuosas = int ( input ("Digite el número de botellas defectuosas "))

#Process
porcentaje_defectos=(botellas_defectuosas/botellas_producidas)*100
if porcentaje_defectos <= 5.0:
    mensaje = "Meta cumplida"
else porcentaje_defectos > 5.0:
    mensaje = "Meta no cumplida"

#Output
print ("El resultado es: " + mensaje )

prueba mmmmm
