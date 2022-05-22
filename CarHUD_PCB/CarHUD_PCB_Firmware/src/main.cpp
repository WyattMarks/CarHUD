#include <Arduino.h>
char message[30];
int messagePos;


void handleCommand(char* message) {
	if (strcmp(message, "name") == 0) {
		Serial.print("ESP\n");
	} else if (strcmp(message, "brightness") == 0) {
		Serial.print(analogRead(33));
		Serial.print('\n');
	}
}

void setup() {
	Serial.begin(115200);
	pinMode(33, INPUT);
	messagePos = 0;
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