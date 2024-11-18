
import time
from typing import Any


def blink (led: Any, blinkCount: int, blinkPauseSeconds:float)->None:
    """
        Makes an LED blink a specific number of times 
    """
    for _ in range (blinkCount):
        led.on()
        time.sleep(blinkPauseSeconds)
        led.off()
        time.sleep(blinkPauseSeconds)

