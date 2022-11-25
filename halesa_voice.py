# gTTS
# Google text-to-speech
# https://gtts.readthedocs.io/en/latest/
# https://pypi.org/project/gTTS/
# pip install gTTS
# 
# playsound
# https://github.com/TaylorSMarks/playsound
# https://pypi.org/project/playsound/
# pip install playsound

#Propias
from datetime import datetime
from time import sleep
from random import randint, choice
#Externas
from gtts import gTTS
from playsound import playsound

language = 'es'

def mostrar_hora():
    ahora = datetime.now()
    return "Son las " + str(ahora.hour) + " y " + str(ahora.minute) + " minutos de la mañana"
def mostrar_temperatura():
    return "Hace 10 grados centígrados"
def mostrar_hora_partido():
    return "España juega a las 11"
def contar_chiste():
    chiste1 = "¿Cómo se dice pañuelo en japonés? Saka-moko."
    chiste2 = "Un pez le pregunta a otro pez: ¿qué hace tu mamá? Este le contesta: Nada, ¿y la tuya qué hace? Nada también."
    chiste3 = "¿Qué le dice un espagueti a otro? ¡El cuerpo me pide salsa!"
    chiste4 = "¿Me da un café con leche corto? Se ha roto la máquina, cambio."
    chistes = (chiste1, chiste2, chiste3, chiste4)
    #return chistes[randint(0,len(chistes)-1)]
    return choice(chistes)#Selecciona un elemento de la colección al azar

def narraRespuesta(texto):
    locucion = gTTS(text=texto, lang=language, slow=False)
    sleep(0.25)#Detiene 0.25 segundos la ejecución del hilo
    locucion.save("respuesta.mp3")
    #sleep(0.25)#Detiene 0.25 segundos la ejecución del hilo
    playsound('respuesta.mp3', True)

orden = "cuentame un chiste"

#OPCIÓN ISABEL/CLAUDIA
respuesta = { x for x in orden.split()}
opcion1 = ({"dime","dame","hora","la"},mostrar_hora)
opcion2 = ({"dime","que","temperatura","hace"},mostrar_temperatura)
opcion3 = ({"hora","juega","partido","españa"},mostrar_hora_partido)
opcion4 = ({"cuentame","cuenta","chiste"},contar_chiste)
opciones = [opcion1, opcion2, opcion3, opcion4]
solucion = max (opciones, key = lambda k: respuesta.intersection(k[0]))
respuesta = solucion[1]()
print(respuesta)
narraRespuesta(respuesta)