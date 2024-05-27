from gpiozero import LEDBoard, Button
from time import sleep
from signal import pause

leds = LEDBoard(5, 6, 13, 19, 26)
increase_delay_button = Button(3)
decrease_delay_button = Button(2)


time_delay = 0.1

def IncreaseTimeDelay():
    global time_delay
    while increase_delay_button.is_held:
        time_delay += 0.0000001
        print(time_delay)

def DecreaseTimeDelay():
    global time_delay
    while decrease_delay_button.is_held:
        print(time_delay)
        time_delay -= 0.0000001
        if time_delay < 0:
            time_delay = 0

increase_delay_button.when_held = IncreaseTimeDelay
decrease_delay_button.when_held = DecreaseTimeDelay
increase_delay_button.hold_time = 0.1  # Set hold time to 0.1 seconds
decrease_delay_button.hold_time = 0.1  # Set hold time to 0.1 seconds


while True:
    for led in leds:
        led.on()
        sleep(time_delay)
        led.off()
        sleep(time_delay)

pause()
