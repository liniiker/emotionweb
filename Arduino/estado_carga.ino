float c = 20;                                                     // Capacidade inicial da bateria (20Ah)
float t0 = 0, tempo_atual, delta_tempo;                           // Variáveis referente ao valor de tempo t em horas
float soc0 = 100;                                                 // Variável referente ao estado de carga inicial (100 = 100%)
float soc1;                                                       // Variável referente ao estado de carga a ser calculado
int v_1;                                                          // Valor de tensão lido no pino analógico A0 do arduino uno
float i;                                                          // Corrente real lida pelo sensor de corrente
float vin = 5;                                                    // Tensão de alimentação do sensor de corrente
float vreal;                                                      // Valor de tensão real

void setup() {

  Serial.begin(9600);                                             // Inicia a comunicação serial

}

void loop() {
    v_1 = analogRead(A0);                                         // Ler o valor de tensão no pino A0. (26,7 mV por Ampère)
    float v = (v_1 * (vin / 1024.0) + 0.01);                      // Variável para armazenar o valor da tensão linda em v_1

    vreal = v - (vin / 2);                                        // Valor real da tensão
    i = ((vreal) / (0.0267) * (5 / vin));                         //  Calculo da corrente
    delay(250);                                                   // delay
    tempo_atual = millis();                                       // Esta variável para armazenar o tempo que o arduino está em execução

    float t1 = tempo_atual * (2.77 * pow(10, -7));                // Calculo para converter Milissegundos em Horas

    delta_tempo = t1 - t0;                                        //
    soc1 = (soc0 + ((i * delta_tempo) / c * 100));                // Calculo do Estado de carga
    t0 += tempo_atual;                                            // Incremento do tempo (funciona como contador)
    t1 += tempo_atual;

    Serial.println("--------Parametros medidos-------");
    Serial.println("Tensao: ");
    Serial.println(v, 3);                                         // Imprime o valor da tensão lida no A0
    Serial.println("Tensao 2: ");
    Serial.println(v_1, 3);                                       // Imprime o valor da tensão após calculo
    Serial.println(" ");
    Serial.println("Corrente: ");
    Serial.println(i, 3);                                         // Imprime o valor da corrente
    Serial.println("Estado de carga: " + String(soc1) + "%");     // Imprime o valor do estado de carga

    delay(1500);
}