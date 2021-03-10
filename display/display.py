#/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch4
from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
def draw_miss_code(draw, mis_code):
    logging.info("draw text")
    Font3 = ImageFont.truetype("./Font/Font02.ttf",150)
    draw.text((20, 0), mis_code[0], fill = "BLACK", font = Font3)
    draw.text((20, 150), mis_code[1], fill = "BLACk", font = Font3)

def main():
    try:
        # display with hardware SPI:
        ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
        #disp = LCD_2inch4.LCD_2inch4(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
        disp = LCD_2inch4.LCD_2inch4()
        # Initialize library.
        disp.Init()
        # Clear display.
        disp.clear()

        # Create blank image for drawing.
        image1 = Image.new("RGB", (disp.width, disp.height ), "WHITE")
        draw = ImageDraw.Draw(image1)

        mis_code = ['123', '321']
        draw_miss_code(draw, mis_code)
        image1=image1.rotate(180)
        disp.ShowImage(image1)
        disp.module_exit()
        logging.info("quit:")
    except IOError as e:
        logging.info(e)    
    except KeyboardInterrupt:
        disp.module_exit()
        logging.info("quit:")
        exit()

if __name__ == '__main__':
    main()
