from gpiozero import CPUTemperature
from time import sleep, strftime, time

while True:
    temp = cpu.temperature

    with open("./log.txt", "a") as log:
        log.write("{0} {1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))

    log.close()

    sleep(30)
