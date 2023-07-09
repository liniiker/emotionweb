import serial
import csv
import pandas as pd

# Configurações da porta serial
port = 'COM17'  # Substitua pela porta serial correta
baudrate = 9600

# Abre a porta serial
ser = serial.Serial(port, baudrate)

# Loop infinito para ler a porta serial
while True:
    # Lê uma linha da porta serial
    line = ser.readline().decode().strip()

    # Ignora a mensagem "Received:"
    line = line.replace("Received:", "")

    # Separa os dados usando o caractere '|'
    data = line.split("|")

    # Verifica se há dados suficientes
    if len(data) >= 2:
        # Extrai o ID e os dados
        id = data[0].strip()
        dados = [d.strip() for d in data[1:]]

        # Remove colchetes e apóstrofos dos dados
        dados_formatados = [d.replace("[", "").replace("]", "").replace("'", "") for d in dados]

        # Cria um novo DataFrame com um único registro
        new_row = pd.DataFrame([[id] + dados_formatados])

        # Carrega o arquivo CSV existente (se houver)
        try:
            df = pd.read_csv('dados.csv', header=None)
        except FileNotFoundError:
            df = pd.DataFrame()

        # Verifica se o DataFrame existe e possui colunas suficientes
        if not df.empty and df.shape[1] >= 6:
            last_row = df.tail(1)
            t1_r1 = int(last_row.iloc[0, 1])
            u1_r1 = int(last_row.iloc[0, 5])
            rpm1 = int(last_row.iloc[0, 8])

            # Realize as ações necessárias com t1_r1, u1_r1 e rpm1
            if t1_r1 < 80:
                # Faça algo quando t1_r1 for menor que 80
                pass

        # Adiciona o novo registro ao DataFrame
        df = df.append(new_row, ignore_index=True)

        # Salva os dados no arquivo CSV
        df.to_csv('dados.csv', header=False, index=False)

        print(f"Dados recebidos - ID: {id}, Dados: {dados_formatados}")
