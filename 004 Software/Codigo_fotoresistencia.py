import machine, onewire, ds18x20, time

pin_heater = machine.Pin(18, machine.Pin.OUT)

ds_pin = machine.Pin(21)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)



def temp():
    ds_sensor.convert_temp()
    time.sleep_ms(1)
    for rom in roms:
        print(ds_sensor.read_temp(rom))
        return ds_sensor.read_temp(rom)

def conv(temp):
    if temp < 175:
        pin_heater.on()
    elif temp >= 175:
        pin_heater.off()
    
while True:
    conv(temp())