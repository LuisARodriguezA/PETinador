import machine
import time

azulDeNuestrosMares = machine.Pin(13, machine.Pin.OUT)
laSangreDeLosQueProtegieronNuestraLibertad = machine.Pin(12, machine.Pin.OUT)

def sentidoHo():
    azulDeNuestrosMares.on()
    laSangreDeLosQueProtegieronNuestraLibertad.off()
    
def sentidoAnti():
    fuente1.on()
    fuente2.off()
    
while True:
    # if kd.is_pressed()
    sentidoHo()
    time.sleep(5)




