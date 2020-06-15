#from gpiozero import CPUTemperature
from time import sleep, strftime, time

temp = 0

with open("./log.txt", "a") as log:
    while True:
        #temp = cpu.temperature
        log.write("{0} {1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))
        sleep(30)
        temp = temp + 1