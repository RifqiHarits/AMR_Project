#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include "ESPAsyncWebServer.h"

//#include <Wire.h>

const char* ssid = "AMCMES_Guest";
const char* password = "guest123";

//AsyncWebServer server(80);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println();
  Serial.print("WiFi connecting to ");
  Serial.println(ssid);

  WiFiClient wifi;
  WiFi.begin(ssid,password);

  Serial.println();
  Serial.print("Connecting");

  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("WiFi Connected Success!");
  Serial.print("NodeMCU IP Address: ");
  Serial.println(WiFi.localIP());

  IPAddress IP = WiFi.localIP();
  
  HTTPClient http;
  http.begin(wifi, "http://central_server_ip/task");
  http.addHeader("Content-Type","application/json");

  String task_data = "{'task': 1}";

  int httpCode = http.POST(task_data);
  String response = http.getString();

  Serial.println(httpCode);
  Serial.println(response);

  http.end();

  /*server.on("/task", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", "Task 1");
  });

  server.begin();*/
}

void loop() {
  // put your main code here, to run repeatedly:

}
