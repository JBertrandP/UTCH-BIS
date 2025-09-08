#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>


const int SENSOR_PINS[5] = {34, 35, 32, 33, 39};
const char* SENSOR_NAMES[5] = {"S1", "S2", "S3", "S4", "S5"};


Adafruit_MPU6050 mpu;
bool mpu_found = false; 


void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("\n\n--- PRUEBA COMPLETA DEL GUANTE (MODO CONTINUO) ---");

  
  if (mpu.begin()) {
    Serial.println("MPU6050 encontrado");
    mpu_found = true; 
  } else {
    Serial.println("************************************************************");
    Serial.println("No se pudo encontrar el sensor MPU6050.");
    Serial.println("El programa continua, pero sin datos de movimiento.");
    Serial.println("************************************************************");
    mpu_found = false; 
  }
  Serial.println("-----------------------------------------------------------------");
}

void loop() {
 
  Serial.print("Flex: [");
  for (int i = 0; i < 5; i++) {
    Serial.print(analogRead(SENSOR_PINS[i]));
    if (i < 4) {
      Serial.print(", ");
    }
  }
  Serial.print("] | ");


  if (mpu_found) {
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);


    Serial.print("Accel: ");
    Serial.print(a.acceleration.x, 1);
    Serial.print("/");
    Serial.print(a.acceleration.y, 1);
    Serial.print("/");
    Serial.print(a.acceleration.z, 1);
    Serial.print(" | ");

  
    Serial.print("Gyro: ");
    Serial.print(g.gyro.x, 1);
    Serial.print("/");
    Serial.print(g.gyro.y, 1);
    Serial.print("/");
    Serial.println(g.gyro.z, 1);
  } else {
   
    Serial.println("MPU6050: No Detectado");
  }

  delay(250); /
}