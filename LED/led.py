import gpiozero
import time

def blink (led, blinkCount, blinkPauseSeconds):
    for _ in range (blinkCount):
        led.on()
        time.sleep(blinkPauseSeconds)
        led.off()
        time.sleep(blinkPauseSeconds)

led = gpiozero.LED(4)
i = 5
while i > 0:
    blink(led,5,.1)
    led.off()
    time.sleep(1)
    i -= 1
