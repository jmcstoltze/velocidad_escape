#importa la librería necesaria
import math

#usuario ingresa valor radio
radio_planeta = input('Ingrese el radio del planeta en kilómetros: ')

#usuario ingresa constante gravitacional
constante_gravitacional = input('Ingrese la constante gravitacional en m/s^2: ')

#se calcula la velocidad de escape usando librería math (redondea en un decimal)
velocidad_escape = round(math.sqrt(2*float(constante_gravitacional)*float(radio_planeta)*1000), 1)

#imprime en pantalla el resultado
print(f"La velocidad de escape en m/s es de: {velocidad_escape}")