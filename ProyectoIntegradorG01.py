nombre_usuario: str = ''
#Input
mensaje:str = ""
operario_revision = str ( input ("Digite el nombre del operario a cargo de la revisión "))
botellas_producidas = int ( input ("Digite el número de botellas producidas en el turno "))
botellas_defectuosas = int ( input ("Digite el número de botellas defectuosas "))
porcentaje_defectos = str

#Process
porcentaje_defectos=(botellas_defectuosas/botellas_producidas)*100
if porcentaje_defectos <= 5.0:
    mensaje = "Meta cumplida"
elif porcentaje_defectos > 5.0:
    mensaje = "Meta no cumplida"

#Output
print ("El resultado es " + mensaje )
