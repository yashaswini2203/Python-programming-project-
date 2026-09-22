from machine import Pin
import time
import network
import urequests

# -----------------------------
# Pin definitions
# -----------------------------
led = Pin(5, Pin.OUT)
pir = Pin(19, Pin.IN)

# -----------------------------
# ThingSpeak details
# -----------------------------
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

THINGSPEAK_API_KEY = "3EA6FUTAON66G3EX"

# ThingSpeak update URL
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# -----------------------------
# Connect to Wi-Fi
# -----------------------------
print("Connecting to Wi-Fi...")

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi.isconnected():
    time.sleep(1)
    print("Connecting...")

print("Wi-Fi connected!")
print("IP address:", wifi.ifconfig()[0])

# -----------------------------
# PIR sensor stabilization
# -----------------------------
print("PIR sensor starting...")
time.sleep(10)

print("Ready!")

pir_state = 0

# -----------------------------
# Send data to ThingSpeak
# -----------------------------
def send_to_thingspeak(motion):

    url = THINGSPEAK_URL + "?api_key=" + THINGSPEAK_API_KEY + "&field1=" + str(motion)

    try:
        response = urequests.get(url)

        print("ThingSpeak response:", response.text)

        response.close()

    except Exception as e:
        print("ThingSpeak error:", e)

# -----------------------------
# Main loop
# -----------------------------
while True:

    motion = pir.value()

    if motion == 1:

        # Motion detected
        led.value(1)

        if pir_state == 0:
            print("Motion detected!")

            # Send 1 to ThingSpeak
            send_to_thingspeak(1)

            pir_state = 1

    else:

        # No motion
        led.value(0)

        if pir_state == 1:
            print("Motion ended!")

            # Send 0 to ThingSpeak
            send_to_thingspeak(0)

            pir_state = 0

    time.sleep(0.1)