#include <WiFi.h>
#include <ArduinoWebsockets.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <ArduinoJson.h>

using namespace websockets;

const char* ssid = "WIFI UA BIS";
const char* password = "";
const char* websocket_server_host = "10.100.0.104";
const uint16_t websocket_server_port = 8000;

const int SENSOR_PINS[5] = {34, 35, 32, 33, 39};
Adafruit_MPU6050 mpu;
WebsocketsClient client;

void onWebsocketEvent(WebsocketsEvent event, String data) {
    if (event == WebsocketsEvent::ConnectionOpened) Serial.println("Conexion WebSocket establecida.");
    else if (event == WebsocketsEvent::ConnectionClosed) Serial.println("Conexion WebSocket cerrada.");
}

void setup() {
    Serial.begin(115200); Wire.begin();
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
    Serial.println("\nWi-Fi conectado!");
    if (!mpu.begin()) { Serial.println("🚨 Error MPU6050"); while (1); }
    Serial.println("MPU6050 inicializado.");
    client.onEvent(onWebsocketEvent);
    
   
    client.connect(websocket_server_host, websocket_server_port, "/ws/glove");
}

void loop() {
    client.poll();
    static unsigned long lastSendTime = 0;
    if (client.available() && (millis() - lastSendTime > 100)) {
        StaticJsonDocument<512> jsonDoc;
        JsonArray flexData = jsonDoc.createNestedArray("flex");
        for (int i = 0; i < 5; i++) { flexData.add(analogRead(SENSOR_PINS[i])); }
        sensors_event_t a, g, temp;
        mpu.getEvent(&a, &g, &temp);
        JsonObject accelData = jsonDoc.createNestedObject("accel");
        accelData["x"] = a.acceleration.x; accelData["y"] = a.acceleration.y; accelData["z"] = a.acceleration.z;
        JsonObject gyroData = jsonDoc.createNestedObject("gyro");
        gyroData["x"] = g.gyro.x; gyroData["y"] = g.gyro.y; gyroData["z"] = g.gyro.z;
        String jsonData;
        serializeJson(jsonDoc, jsonData);
        client.send(jsonData);
        lastSendTime = millis();
    }
}