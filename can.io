//  SENSOR INFRARED - FÓRMULA E-MOTION UFPB 2022 *********************************************************************
//  AUTOR:  JUAN ALBUQUERQUE
//  OBJETIVO: TRANSMISSÃO DE DADOS ENTRE AS PCBs

#include <SPI.h>
#include <mcp2515.h>                               //A biblioteca para instalação: autowp-mcp2515

struct can_frame canMsg1;                          //Definir variavel

MCP2515 mcp2515(10);                               //Definir variavel

void setup() {

  canMsg1.can_id  = 0x0F6;
  canMsg1.can_dlc = 8;
  canMsg1.data[0] = 0xC8;
  canMsg1.data[1] = 0xC8;
  canMsg1.data[2] = 0xC8;
  canMsg1.data[3] = 0xC8;
  canMsg1.data[4] = 0xC8;
  canMsg1.data[5] = 0xC8;
  canMsg1.data[6] = 0xC8;
  canMsg1.data[7] = 0xC8;

  Serial.begin(9600);                              //A frequência de inicialização do serial

  mcp2515.reset();                                 //A função reset do mcp2515
  mcp2515.setBitrate(CAN_125KBPS, MCP_8MHZ);       //A função propria da biblioteca;CAN_125KBPSreferesse a taxa de bits; MCP_8MHZ referesse ao crystal ligado a ele
  mcp2515.setNormalMode();                         //A função propria da biblioteca indicando 1 dos 3 modos da rede
}

void loop() {

  mcp2515.sendMessage(&canMsg1);                   //A função para realizar o envio dos dados
  Serial.println("Messages sent");                 //Imprimir Mensagem enviado

  delay(500);                                     //Ideal é deixar o delay em 100ms
}