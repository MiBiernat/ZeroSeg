#!/usr/bin/env python

import ZeroSeg.led as led
import time
from datetime import datetime, date

def days_until_wedding():
    wedding_date = date(2025, 9, 13)
    today = date.today()
    delta = wedding_date - today
    return delta.days

def display_countdown(device, deviceId):
    # Pobierz liczbę dni
    days = days_until_wedding()
    
    # Konwertuj na string i dodaj "days"
    text = f"{days} DAYS"
    
    # Wyświetl tekst
    device.write_text(deviceId, text)
    # Czekaj 15 minut (900 sekund)
    time.sleep(900)

device = led.sevensegment()

while True:
    display_countdown(device, 0)
