#!/usr/bin/env python

import ZeroSeg.led as led
import time
import RPi.GPIO as GPIO
from datetime import datetime, date

# Konfiguracja przycisku
BUTTON1 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1, GPIO.IN)

def time_until_wedding():
    wedding_date = datetime(2025, 9, 13, 17, 0, 0)
    now = datetime.now()
    delta = wedding_date - now
    
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    
    return days, hours, minutes, seconds

def display_countdown(device, deviceId):
    while True:
        days, hours, minutes, seconds = time_until_wedding()
        
        # Domyślnie pokazuj dni
        text = f"{days} DAYS"
        device.write_text(deviceId, text)
        
        # Sprawdź czy przycisk został naciśnięty
        if not GPIO.input(BUTTON1):
            # Pokaż godziny
            text = f"{hours} HRS"
            device.write_text(deviceId, text)
            time.sleep(3)
            
            # Pokaż minuty
            text = f"{minutes} nIn"  # używamy 'n' zamiast 'm' bo wygląda lepiej na wyświetlaczu 7-seg
            device.write_text(deviceId, text)
            time.sleep(3)
            
            # Pokaż sekundy
            text = f"{seconds} SEC"
            device.write_text(deviceId, text)
            time.sleep(3)
            
            # Wróć do wyświetlania dni
            text = f"{days} DAYS"
            device.write_text(deviceId, text)
            
        time.sleep(0.2)  # Małe opóźnienie dla debouncing'u przycisku

device = led.sevensegment()

try:
    display_countdown(device, 0)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
