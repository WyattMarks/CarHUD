#include <Arduino.h>
#include <DS1631.h> 

char message[30];
int messagePos;
DS1631_Class DS1631;

int getTemperature() {
	int ambientTemperature = 0;
	for (int i = 0; i < DS1631.thermometers; i++) {
		ambientTemperature += DS1631.readTemp(i);  // Add readings
	}                                            // of for-next every thermometer found
	ambientTemperature = ambientTemperature / DS1631.thermometers;

  	return (int) ambientTemperature * 6.25;
}

void handleCommand(char* message) {
	if (strcmp(message, "name") == 0) {
		Serial.print("ESP\n");
	} else if (strcmp(message, "brightness") == 0) {
		Serial.print(analogRead(33));
		Serial.print('\n');
	} else if (strcmp(message, "temp") == 0) {
		Serial.print(getTemperature());
		Serial.print('\n');
	}
}

void setup() {
	Serial.begin(115200);
	pinMode(33, INPUT);
	messagePos = 0;
	Serial.print("ESP\n");

	while (!DS1631.begin()) {
		Serial.println(F("Unable to find a DS1631. Checking again in 3 seconds."));
		delay(3000);
	}
	int ambientTemperature = 0;

	Serial.print(F("Found "));
	Serial.print(DS1631.thermometers);
	Serial.println(F(" DS1631 device(s)"));

	for (int i = 0; i < DS1631.thermometers; i++) {
		DS1631.setPrecision(i, 12);  // Set maximum 12bit precision = 0.0625/degC
		DS1631.setContinuous(i);     // Activate continuous mode
	} 

	delay(750); 

	for (int i = 0; i < DS1631.thermometers; i++) {
		ambientTemperature += DS1631.readTemp(i);  // Add readings
	}                                            // of for-next every thermometer found
	ambientTemperature = ambientTemperature / DS1631.thermometers;

	Serial.print(F("Ambient = "));
  	Serial.print(ambientTemperature * 0.0625, 3);
}

void loop() {
	uint x = Serial.available();
	while (x > 0) {
		char buffer[10];
		x = Serial.readBytes(buffer, x);
		
		for (int i = 0; i < x; i++) {
			message[messagePos + i] = buffer[i];
		}
		messagePos += x;

		for (int i = messagePos - x; i < messagePos; i++) {
			if (message[i] == '\n') {
				message[i] = 0;
				messagePos = 0;

				handleCommand(message);
			}
		}

		x = Serial.available();
	}
}