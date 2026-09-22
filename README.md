
Smart Home Security System
1. Project Title
Smart Home Security System Using ESP32, PIR Sensor and ThingSpeak
2. Problem Statement
Home security is important for detecting unwanted movement inside a house. A simple motion detection system can help monitor movement in a particular area.
This project uses an ESP32 and PIR motion sensor to detect movement. When motion is detected, the ESP32 turns ON an LED as an indication. The motion status is also sent to the ThingSpeak cloud platform for monitoring through a graph.
3. Objectives
•	To detect movement using a PIR motion sensor.
•	To use ESP32 for receiving and processing the sensor signal.
•	To turn ON an LED when motion is detected.
•	To turn OFF the LED when there is no motion.
•	To send motion data to the ThingSpeak platform.
•	To display the motion status using a graph.
•	To understand the basic working of an IoT-based home security system.
4. Components and Software Used
Hardware:
•	ESP32
•	PIR Motion Sensor
•	LED
•	Connecting wires
Software and Platforms:
•	Wokwi
•	Arduino/C++ programming
•	ThingSpeak
•	GitHub
5. Circuit Diagram
The PIR motion sensor and LED are connected to the ESP32 as follows:
•	PIR VCC → ESP32 5V/VIN
•	PIR OUT → ESP32 GPIO 19
•	PIR GND → ESP32 GND
•	LED → ESP32 GPIO 5
•	LED GND → ESP32 GND
The PIR sensor is used as the input device and the LED is used as the output indicator.
Circuit Diagram:
Upload your Wokwi circuit screenshot here as:
circuit_diagram.png
6. Working Principle
The PIR motion sensor detects movement in its surrounding area.
When motion is detected, the PIR sensor gives a HIGH signal to the ESP32 through GPIO 19. The ESP32 reads this signal and turns ON the LED connected to GPIO 5.
When no motion is detected, the PIR sensor gives a LOW signal. The ESP32 then turns OFF the LED.
The motion data is also monitored using ThingSpeak. The sensor status is represented using values:
•	1 → Motion detected
•	0 → No motion
ThingSpeak displays these readings in the form of a graph, allowing the motion status to be monitored over time.
7. Program Explanation
The program is written using Arduino/C++ for the ESP32.
First, the LED and PIR sensor pins are defined:
const int ledpin = 5;
const int PIRinput = 19;
Here, GPIO 5 is used for the LED and GPIO 19 is used for the PIR sensor.
The program sets the LED as an output and the PIR sensor as an input:
pinMode(ledpin, OUTPUT);
pinMode(PIRinput, INPUT);
The ESP32 continuously reads the PIR sensor using:
digitalRead(PIRinput);
If the PIR sensor gives a HIGH signal, motion is detected. The ESP32 turns ON the LED:
digitalWrite(ledpin, HIGH);
If the PIR sensor gives a LOW signal, there is no motion and the LED is turned OFF:
digitalWrite(ledpin, LOW);
The program also uses Serial Monitor messages such as "Motion detected!" and "Motion ended!" to show the sensor status.
The motion readings are monitored on ThingSpeak, where the values are displayed using a graph.
8. Output
The Wokwi simulation shows the ESP32 connected to the PIR motion sensor and LED.
When motion is detected:
PIR Sensor → ESP32 → LED ON
When motion is not detected:
PIR Sensor → ESP32 → LED OFF
The ThingSpeak channel displays the PIR motion readings as a graph.
The ThingSpeak graph contains:
•	Field 1 → PIR Motion
•	1 → Motion detected
•	0 → No motion
Output Screenshot:
Upload your Wokwi screenshot as:
wokwi_output.png
ThingSpeak Graph:
Upload your ThingSpeak graph as:
thingspeak_output.png
9. Applications
•	Home security systems
•	Room monitoring
•	Motion detection
•	Entry detection
•	Basic intrusion monitoring
•	Smart home systems
•	IoT-based security monitoring
10. Limitations
•	The system depends on the PIR sensor for motion detection.
•	PIR sensor cannot identify the person who caused the motion.
•	The detection range depends on the sensor.
•	The project is implemented as a Wokwi simulation.
•	ThingSpeak monitoring requires internet connectivity.
•	The basic project only provides an LED indication and does not include a buzzer or camera.
11. Future Scope
•	Add a buzzer for an alarm when motion is detected.
•	Add a camera for visual monitoring.
•	Send mobile notifications when motion is detected.
•	Add door and window sensors.
•	Use a real ESP32 and PIR sensor hardware setup.
•	Develop a mobile or web dashboard for security monitoring.
•	Store and analyze motion data for a longer period.
12. Team Members' Details
Team Members:
1.	Niveditha k-U03ZW24S0091
2.	Yashaswini NS-U03ZW24S0094
3.	Maria shobha A-U03ZW24S0090
13. Wokwi Project Link
https://wokwi.com/projects/475605312743188481
14. ThingSpeak Channel Link
https://thingspeak.mathworks.com/channels/3500296/private_show

