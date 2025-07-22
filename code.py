from adafruit_circuitplayground import cp
import time

class Region:
    def __init__(self, leds, color):
        self.__leds = leds
        self.__color = color
    
    def set_leds(self, leds):
        self.__leds = leds
        
    def set_color(self, color):
        self.__color = color

    def get_leds(self):
        return self.__color

    def get_color(self):
        return self.__color
       
    def all_on(self):
        for pixel in self.__leds:
            cp.pixels[pixel] = self.__color

    def all_off(self):
        for pixel in self.__leds:
            cp.pixels[pixel] = (0, 0, 0)

#I turned down the brightness because it was giving me a headache at full brightness
cp.pixels.brightness = .05

red = Region((0, 2, 4, 6, 8), (255, 0, 0))
blue = Region((1, 3, 5, 7, 9), (0, 0, 255))

while True:
    red.all_on()
    time.sleep(0.5)
    red.all_off()
    time.sleep(0.25)
    blue.all_on()
    time.sleep(0.5)
    blue.all_off()
    time.sleep(0.25)