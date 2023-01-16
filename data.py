import serial
import csv
from datetime import datetime

# Selecionar porta que o arduino está conectado
PORT = 'COM15'
ser = serial.Serial(PORT, 9600)

while True:
        message = ser.readline()
        data = message.strip().decode()
        split_string = data.split(',')  #percorrendo a string

        #charge = int(split_string[0])  # convert first part of string into float
        velocidade =  int(split_string[0])
        estado_carga = int(split_string[1])
        #t1 = float(split_string[3])
        #t2 = float(split_string[4])
        #t3 = float(split_string[5])
        #t4 = float(split_string[6])
        #r1 = float(split_string[7])
        #r2 = float(split_string[8])
        #r3 = float(split_string[9])
        #r4 = float(split_string[10])


        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

        print(dt_string, velocidade, estado_carga)
        #print(dt_string, velocidade, estado_carga, t1, t2, t3, t4, r1, r2, r3, r4)

        with open("data.csv", "a") as f:
            writer = csv.writer(f, delimiter = ",")
            # writer.writerow([dt_string, charge])
            writer.writerow([dt_string, velocidade, estado_carga])
            #writer.writerow([dt_string, velocidade, estado_carga, t1, t2, t3, t4, r1, r2, r3, r4])
            # writer.writerow([dt_string, bitcoin_rank, bitcoin_currency, bitcoin_price, bitcoin_change, bitcoin_market_cap])