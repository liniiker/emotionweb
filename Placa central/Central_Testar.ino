#include <SPI.h>                                  // Inclui a biblioteca SPI para comunicação com o MCP2515
#include <mcp2515.h>                              // Inclui a biblioteca MCP2515 para comunicação com a rede CAN
#include <Wire.h>                                 // Inclui a biblioteca Wire para comunicação com o MPU6050 e o MLX90614
#include <MPU6050.h>                              // Inclui a biblioteca MPU6050 para ler os valores do acelerômetro e do giroscópio
#include "Adafruit_MLX90614.h"                    // Inclui a biblioteca Adafruit_MLX90614 para ler os valores do sensor de temperatura
#include <SoftwareSerial.h>                       // Inclui a biblioteca SoftwareSerial para comunicação com o GPS
#include <TinyGPS.h>                              // Inclui a biblioteca TinyGPS para ler os valores do GPS

#define pino_1 2                                  // Define o pino 1 como 2
#define pino_2 3                                  // Define o pino 2 como 3

#define SENSOR_PIN 2                              // Define o pino do sensor LJ12A3-4-Z/BX como 2
#define NUM_HOLES 10                              // Define o número de furos no disco de freio como 10

float rpm;
int holeCount = 0;                                // Inicializa o contador de furos como 0
unsigned long startTime = 0;                      // Inicializa o tempo de início da contagem como 0

struct can_frame canMsg1;                         // Cria uma estrutura para armazenar a mensagem CAN 1
struct can_frame canMsg2;                         // Cria uma estrutura para armazenar a mensagem CAN 2

SoftwareSerial porta(8, 7);                       // Cria uma porta serial de software nos pinos 8 e 7
TinyGPS gps;                                      // Cria um objeto TinyGPS

Adafruit_MLX90614 mlx_0 = Adafruit_MLX90614();    // Cria um objeto Adafruit_MLX90614 para o sensor de temperatura mlx_0
Adafruit_MLX90614 mlx_1 = Adafruit_MLX90614();    // Cria um objeto Adafruit_MLX90614 para o sensor de temperatura mlx_1

MCP2515 mcp2515(10);                              // Cria um objeto MCP2515 no pino 10

int vel;                                          // Declara a variável vel (velocidade)

MPU6050 mpu;                                      // Cria um objeto MPU6050

void setup() {

 Wire.begin();                                    // Inicializa a comunicação I2C
 mpu.initialize();                                // Inicializa o sensor MPU6050

 canMsg1.can_id = 0x002;                          // Define o ID da mensagem CAN 1 como 0x002
 canMsg1.can_dlc = 8;                             // Define o tamanho da mensagem CAN 1 como 8 bytes
 canMsg1.data[0] = 0x00;                          // Inicializa o primeiro byte da mensagem CAN 1 como 0x00
 canMsg1.data[1] = 0x00;                          // Inicializa o segundo byte da mensagem CAN 1 como 0x00
 canMsg1.data[2] = 0x00;                          // Inicializa o terceiro byte da mensagem CAN 1 como 0x00
 canMsg1.data[3] = 0x00;                          // Inicializa o quarto byte da mensagem CAN 1 como 0x00
 canMsg1.data[4] = 0x00;                          // Inicializa o quinto byte da mensagem CAN 1 como 0x00
 canMsg1.data[5] = 0x00;                          // Inicializa o sexto byte da mensagem CAN 1 como 0x00
 canMsg1.data[6] = 0x00;                          // Inicializa o sétimo byte da mensagem CAN 1 como 0x00
 canMsg1.data[7] = 0x00;                          // Inicializa o oitavo byte da mensagem CAN 1 como 0x00

 canMsg2.can_id = 0x003;                          // Define o ID da mensagem CAN 2 como 0x003
 canMsg2.can_dlc = 3;                             // Define o tamanho da mensagem CAN 2 como 3 bytes
 canMsg2.data[0] = 0x00;                          // Inicializa o primeiro byte da mensagem CAN 2 como 0x00
 canMsg2.data[1] = 0x00;                          // Inicializa o segundo byte da mensagem CAN 2 como 0x00
 canMsg2.data[2] = 0x00;                          // Inicializa o terceiro byte da mensagem CAN 2 como 0x00
 
 mlx_0.begin(0x58);                               // Inicializa o sensor de temperatura mlx_0 com o endereço I2C 0x58
 mlx_1.begin(0x57);                               // Inicializa o sensor de temperatura mlx_1 com o endereço I2C 0x57

 pinMode(SENSOR_PIN, INPUT);                      // Configura o pino do sensor LJ12A3-4-Z/BX como entrada

 porta.begin (9600);                              // Inicializa a comunicação serial de software na porta com a velocidade de 9600 bps
 Serial.begin(9600);                              // Inicializa a comunicação serial na porta Serial com a velocidade de 9600 bps

 mcp2515.reset();                                 // Reseta o MCP2515
 mcp2515.setBitrate(CAN_125KBPS, MCP_8MHZ);       // Configura a taxa de bits da rede CAN como 125 kbps e a frequência do oscilador como 8 MHz
 mcp2515.setNormalMode();                         // Coloca o MCP2515 em modo normal

}

void loop() {

 int sensorValue = digitalRead(SENSOR_PIN);       // Lê o valor do sensor LJ12A3-4-Z/BX
 if (sensorValue == HIGH) {                       // Se o sensor detectar metal
 if (holeCount == 0) {                            // Se for o primeiro furo detectado
 startTime = millis();                            // Registra o tempo de início da contagem
 }
 holeCount++;                                     // Incrementa o contador de furos
 Serial.print("Furo detectado: ");
 Serial.println(holeCount);
 while (digitalRead(SENSOR_PIN) == HIGH) {        // Aguarda até que o sensor não detecte mais metal
 delay(10);
 }
 }
 if (holeCount >= NUM_HOLES) {                      // Se todos os furos foram detectados
 unsigned long elapsedTime = millis() - startTime;  // Calcula o tempo decorrido desde o início da contagem
 float rpm = (60000.0 / elapsedTime) * NUM_HOLES;   // Calcula o RPM da roda
 Serial.print("RPM: ");
 Serial.println(rpm);
 holeCount = 0;                                     // Reinicia o contador de furos
 }
//-----------------------------------------------------

 int16_t ax, ay, az;
 int16_t gx, gy, gz;
 mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);      // Lê os valores do acelerômetro e do giroscópio

 Serial.print(ax);
 Serial.print(" ");
 Serial.print(ay);
 Serial.print(" ");
 Serial.print(az);
 Serial.print(" ");
 Serial.print(gx);
 Serial.print(" ");
 Serial.print(gy);
 Serial.print(" ");
 Serial.println(gz);

 canMsg1.data[4] = ax;                              // Armazena o valor do acelerômetro no eixo X na mensagem CAN 1
 canMsg1.data[5] = ay;                              // Armazena o valor do acelerômetro no eixo Y na mensagem CAN 1
 canMsg1.data[6] = az;                              // Armazena o valor do acelerômetro no eixo Z na mensagem CAN 1
 canMsg2.data[0] = gx;                              // Armazena o valor do giroscópio no eixo X na mensagem CAN 2
 canMsg2.data[1] = gy;                              // Armazena o valor do giroscópio no eixo Y na mensagem CAN 2
 canMsg2.data[2] = gz;                              // Armazena o valor do giroscópio no eixo Z na mensagem CAN 2

//----------------------------------------------------- 

bool dados = false;
 for (unsigned long start = millis(); millis() - start < 1000;) 
 {
 while (porta.available()) 
 {
 char x = porta.read(); 
 if (gps.encode (x)) {dados = true;}
 }
 } 
 if (dados){ 
 vel = gps.f_speed_kmph();                            // Lê a velocidade do GPS em km/h
 Serial.println(vel);
}

 canMsg1.data[0] = mlx_0.readObjectTempC()/2;         // Armazena a temperatura lida pelo sensor mlx_0 na mensagem CAN 1
 canMsg1.data[1] = mlx_1.readObjectTempC()/2;         // Armazena a temperatura lida pelo sensor mlx_1 na mensagem CAN 1
 canMsg1.data[2] = rpm;                               // Armazena o RPM da roda na mensagem CAN 1
 canMsg1.data[3] = vel;                               // Armazena a velocidade lida pelo GPS na mensagem CAN 1

 mcp2515.sendMessage(&canMsg1);                       // Envia a mensagem CAN 1
 mcp2515.sendMessage(&canMsg2);                       // Envia a mensagem CAN 2
 Serial.println("Messages sent");
 
 Serial.print("RPM: ");
 Serial.println(rpm);

 delay(1000);
}