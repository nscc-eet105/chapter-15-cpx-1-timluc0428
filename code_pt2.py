from adafruit_circuitplayground import cp
import time

class Region:
    def __init__(self, leds, color, tone):
        self.__tone = tone
        self.__leds = leds
        self.__color = color
    
    def set_leds(self, leds):
        self.__leds = leds
        
    def set_color(self, color):
        self.__color = color

    def set_tone(self, tone):
        self.__tone = tone

    def get_leds(self):
        return self.__color

    def get_color(self):
        return self.__color
       
    def get_tone(self):
        return self.__tone
       
    def all_on(self):
        for pixel in self.__leds:
            cp.pixels[pixel] = self.__color

    def all_off(self):
        for pixel in self.__leds:
            cp.pixels[pixel] = (0, 0, 0)

    def play_tone(self, duration):
        cp.start_tone(self.__tone)
        time.sleep(duration)
        cp.stop_tone()
        
#I turned down the brightness because it was giving me a headache at full brightness
cp.pixels.brightness = .05

regions = {
    "yellow": Region((5, 6, 7), (255, 255, 0), 252),
    "blue": Region((2, 3, 4), (0, 0, 255), 209),
    "red": Region((7, 8, 9), (255, 0, 0), 310),
    "green": Region((0, 1, 2), (0, 255, 0), 415)
}


while True:
    for name, object in regions.items():
        object.all_on()
        object.play_tone(0.5)
        time.sleep(0.5)
        object.all_off()
        time.sleep(0.25)
