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
    
    # Obliczanie całkowitych wartości
    total_hours = delta.days * 24 + delta.seconds // 3600
    total_minutes = delta.days * 24 * 60 + delta.seconds // 60
    days = delta.days
    
    return days, total_hours, total_minutes

def display_countdown(device, deviceId):
    while True:
        days, hours, minutes = time_until_wedding()
        
        # Domyślnie pokazuj dni
        text = f"{days}d"
        device.write_text(deviceId, text)
        
        # Sprawdź czy przycisk został naciśnięty
        if not GPIO.input(BUTTON1):
            # Pokaż całkowite godziny
            text = f"{hours}h"
            device.write_text(deviceId, text)
            time.sleep(3)
            
            # Pokaż całkowite minuty
            text = f"{minutes}n"
            device.write_text(deviceId, text)
            time.sleep(3)
            
            # Wróć do wyświetlania dni
            text = f"{days}d"
            device.write_text(deviceId, text)
            
        time.sleep(0.2)

device = led.sevensegment()

try:
    display_countdown(device, 0)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
