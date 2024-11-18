from led import blink
import gpiozero
import time


class rpi_test:
    def button_pressed_test(gpio_num:int):
        button = gpiozero.Button(gpio_num)
        while True:
            if button.is_pressed:
                print("button is pressed")
            else:
                print("not pressed")


    def led_blink_test(gpio_num:int):
        led = gpiozero.LED(gpio_num)
        i = 5
        while i > 0:
            blink(led,15,.1)
            led.off()
            time.sleep(1)
            i -= 1

    def blink_on_button_press(gpio_btn_num:int,gpio_led_num:int):
        button = gpiozero.Button(gpio_btn_num)
        led = gpiozero.LED(gpio_led_num)
        while True:
            if button.is_pressed:
                blink(led,5,1)
            else:
                print('Not a pressed button')

if __name__ == '__main__':
    rp = rpi_test
    #rp.led_blink_test(27)
    #rp.button_pressed_test(17)
    rp.blink_on_button_press(17,27)
