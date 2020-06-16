from gpiozero.pins.mock import MockFactory
from gpiozero import Device, CPUTemperature
from time import sleep, strftime, time

Device.pin_factory = MockFactory()

cpu = CPUTemperature()

while True:
    temp = cpu.temperature

    with open("./log.txt", "a") as log:
        log.write("{0} {1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))

    log.close()

    sleep(30)
