#!/usr/bin/python
import time
import os
import sys
import Adafruit_CharLCD as LCD

lcd_rs = 25
lcd_en = 24
lcd_d4 = 12
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 11
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
while True:
	lcd.message("Temp: "+str(sys.argv[1])+"\nPress 2 Avoid")
	time.sleep(5.0)
	lcd.clear()

