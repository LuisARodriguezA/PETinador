import machine, time
from machine import ADC
pin_heater = machine.Pin(4, machine.Pin.OUT)
led = machine.Pin(35, machine.Pin.IN)
inp = ADC(led)



def temp():
    total = 0 
    count = 0
    while count < 1000:
        adc = inp.read_u16()
        adc_to_v = (3.3*adc)/65535
        paso1 = 3.3 - adc_to_v
        paso2 = paso1/500
        if paso2 != 0:
            paso3 = adc_to_v/paso2
        total += paso3
        count += 1
    print(total/count)
    return total/count

def conv(tem):
    if tem < 73:
        pin_heater.on()
    elif tem >= 83:
        pin_heater.off()
    
while True:
    pin_heater.on()
    conv(temp())
