import machine
import time
from machine import ADC
pin = machine.Pin(15, machine.Pin.IN)
azul = machine.Pin(21, machine.Pin.OUT)
amarello = machine.Pin(18, machine.Pin.OUT)
rojo = machine.Pin(22, machine.Pin.OUT)

adc = ADC(pin)

def porcentajeLuz(ADC):
    return (-0.0015259021*ADC)+100


while True:
    val = adc.read_u16()
    porcentaje = porcentajeLuz(val)
    print(porcentaje)
    if porcentaje <= 33.333333 and porcentaje > 0:
        rojo.on()
    elif porcentaje > 33.33333 and porcentaje < 66.66666:
        amarello.on()
    else:
        azul.on()
    time.sleep(0.05)
    azul.off()
    amarello.off()
    rojo.off()