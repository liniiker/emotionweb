import serial

# Configurar a porta serial
porta_serial = serial.Serial('/dev/ttyUSB0', 9600)  # Substitua '/dev/ttyUSB0' pela porta serial correta
porta_serial.timeout = 1

# Dicionário para armazenar os dados
dados = {}


# Função para processar as mensagens
def processar_mensagem(mensagem):
    # Separar os campos da mensagem
    campos = mensagem.split(' ')

    # Extrair os valores
    id = int(campos[1])
    dlc = int(campos[3])
    data = campos[5:5 + dlc]

    # Armazenar os valores no dicionário
    dados[id] = data


# Loop para ler as mensagens da porta serial
while True:
    # Ler uma linha da porta serial
    linha = porta_serial.readline().decode().strip()

    # Verificar se a linha contém uma mensagem válida
    if linha.startswith("ID:") and linha.endswith("DATA:"):
        mensagem = linha + " " + porta_serial.readline().decode().strip()
        processar_mensagem(mensagem)

    # Verificar se todas as mensagens foram recebidas
    if len(dados) == 3:  # Substitua 3 pelo número total de IDs esperados
        break

# Imprimir os valores de DATA para cada ID
for id, data in dados.items():
    print(f"ID: {id}, DATA: {' '.join(data)}")





#===================================================================================================

import csv
import serial

# Configurar a porta serial
porta_serial = serial.Serial('/dev/ttyUSB0', 9600)  # Substitua '/dev/ttyUSB0' pela porta serial correta
porta_serial.timeout = 1

# Dicionário para armazenar os dados
dados = {}


# Função para processar as mensagens
def processar_mensagem(mensagem):
    # Separar os campos da mensagem
    campos = mensagem.split(' ')

    # Extrair os valores
    id = int(campos[1])
    dlc = int(campos[3])
    data = campos[5:5 + dlc]

    # Armazenar os valores no dicionário
    dados[id] = data


# Loop para ler as mensagens da porta serial
while True:
    # Ler uma linha da porta serial
    linha = porta_serial.readline().decode().strip()

    # Verificar se a linha contém uma mensagem válida
    if linha.startswith("ID:") and linha.endswith("DATA:"):
        mensagem = linha + " " + porta_serial.readline().decode().strip()
        processar_mensagem(mensagem)

    # Verificar se todas as mensagens foram recebidas
    if len(dados) == 3:  # Substitua 3 pelo número total de IDs esperados
        break

# Salvar os valores de DATA em um arquivo CSV
nome_arquivo = "guardar.csv"
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    # Escrever o cabeçalho
    escritor_csv.writerow(['ID', 'DATA'])

    # Escrever os valores de DATA para cada ID
    for id, data in dados.items():
        escritor_csv.writerow([id, ' '.join(data)])

print(f"Os valores de DATA foram salvos no arquivo '{nome_arquivo}'.")
