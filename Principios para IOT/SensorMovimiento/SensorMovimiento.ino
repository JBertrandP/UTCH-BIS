#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>


const int buttonPin = 5;          
const int ledPins[] = {13,12,11,10,9};
const int pinServo = 6;           
const int pinFotoresistencia = A0; 
const int TRIGGER = 4;           
const int ECHO = 3;               


LiquidCrystal_I2C lcd(0x27, 16, 2);

bool systemActive = false;        
bool errorState = false;         
bool nightTime = false;          
int lastButtonState = HIGH;      
bool buttonLock = false;          
bool sensorWasDisconnected = false; 


const float DISTANCE_THRESHOLDS[] = {50.0, 40.0, 30.0, 20.0, 10.0};
const int LIGHT_THRESHOLD = 700;  


Servo myServo;
int servoPos = 90;                
bool sweepingRight = true;       
unsigned long lastDistanceTime = 0;
const int DISTANCE_INTERVAL = 300; 


unsigned long lastServoTime = 0;
const int SERVO_INTERVAL_NORMAL = 20;  
const int SERVO_INTERVAL_ERROR = 20;   


float lastValidDistance = 0;
unsigned long lastLEDUpdate = 0;
const int LED_UPDATE_INTERVAL = 100;  

void setup() {
  Serial.begin(9600);
  lcd.backlight();
  
  
  pinMode(buttonPin, INPUT_PULLUP);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);

  
  myServo.attach(pinServo);
  myServo.write(servoPos);

  
  lcd.begin(16, 2);
  updateDisplay("Sistema Listo", "Presiona Boton");
  Serial.println("Sistema Inicializado");
}

void loop() {
  checkLightSensor();
  
  if (!errorState && !buttonLock) {
    checkButton();
  }

  unsigned long currentMillis = millis();
  
  moveServo();

  if (currentMillis - lastDistanceTime >= DISTANCE_INTERVAL) {
    if (shouldOperate()) {
      float distance = measureDistance();
      if (distance > 0) {
        lastValidDistance = distance;
        String distStr = String(distance) + "cm";
        if (errorState) {
          updateDisplay("ERROR: Sensor Luz", distStr);
        } else {
          updateDisplay("Activo", distStr);
        }
        Serial.println("Distancia: " + distStr);
      }
      updateLEDs();
    } else if (systemActive && !nightTime && !errorState) {
      updateDisplay("Activo - Dia", "Esperando noche");
      Serial.println("Sistema activo - Es de dia");
      resetLEDs();
    }
    lastDistanceTime = currentMillis;
  }
  
  if (currentMillis - lastLEDUpdate >= LED_UPDATE_INTERVAL) {
    if (!shouldOperate()) {
      resetLEDs();
    } else {
      updateLEDs();
    }
    lastLEDUpdate = currentMillis;
  }
}

bool shouldOperate() {
  return (systemActive && nightTime) || errorState;
}

void checkButton() {
  int currentButtonState = digitalRead(buttonPin);
  
  if (currentButtonState == LOW && lastButtonState == HIGH) {
    delay(50);
    if (digitalRead(buttonPin) == LOW) {
      systemActive = !systemActive;
      if (systemActive) {
        updateDisplay("Activando...", nightTime ? "Noche" : "Dia");
        Serial.println("Sistema ACTIVADO");
      } else {
        updateDisplay("Sistema", "Inactivo");
        Serial.println("Sistema DESACTIVADO");
        resetLEDs();
      }
    }
  }
  lastButtonState = currentButtonState;
}

void checkLightSensor() {
  int lightValue = analogRead(pinFotoresistencia);

  if (lightValue <= 0 || lightValue >= 1023) {
    if (!errorState) {
      errorState = true;
      buttonLock = true;
      nightTime = true;
      sensorWasDisconnected = true;
      updateDisplay("Activo", distStr);
      Serial.println("Distancia: " + distStr);
      if (!systemActive) {
        systemActive = true;
        Serial.println("Sistema ACTIVADO (modo error)");
      }
    }
  } else {
    if (errorState) {
      errorState = false;
      buttonLock = false;
      if (sensorWasDisconnected) {
        updateDisplay("Sensor OK", "Reconectado");
        Serial.println("Sensor de luz reconectado.");
        delay(1000);
        sensorWasDisconnected = false;
      }
    }
    nightTime = (lightValue < LIGHT_THRESHOLD);
    if (!nightTime && !errorState) {
      resetLEDs();
    }
  }
}

void moveServo() {
  unsigned long currentMillis = millis();
  int servoInterval = errorState ? SERVO_INTERVAL_ERROR : SERVO_INTERVAL_NORMAL;
  
  if (currentMillis - lastServoTime >= servoInterval) {
    if (shouldOperate()) {
      servoPos += sweepingRight ? 2 : -2;
      if (servoPos >= 180) { sweepingRight = false; servoPos = 180; }
      else if (servoPos <= 0) { sweepingRight = true; servoPos = 0; }
      myServo.write(servoPos);
    }
    lastServoTime = currentMillis;
  }
}

float measureDistance() {
  digitalWrite(TRIGGER, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER, LOW);

  long duration = pulseIn(ECHO, HIGH);
  return duration * 0.034 / 2;
}

void updateLEDs() {
  int ledsToLight = map(constrain(lastValidDistance, 10, 50), 10, 50, 5, 1);
  for (int i = 0; i < 5; i++) {
    digitalWrite(ledPins[i], i < ledsToLight ? HIGH : LOW);
  }
}

void resetLEDs() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(ledPins[i], LOW);
  }
}

void updateDisplay(String line1, String line2) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(line1);
  lcd.setCursor(0, 1);
  lcd.print(line2);
}

