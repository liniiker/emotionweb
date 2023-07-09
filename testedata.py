import csv
import random
import time

# Função para gerar valores aleatórios
def generate_random_values():
    values = []
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    values.append(current_time)
    for _ in range(5):
        value = round(random.uniform(0, 5000), 1)
        values.extend([value, value])
    return values

# Caminho do arquivo CSV
csv_file_path = 'data3.csv'

# Loop para gerar e salvar valores aleatórios a cada segundo
while True:
    # Gera os valores aleatórios
    random_values = generate_random_values()

    # Salva os valores no arquivo CSV
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(random_values)

    # Aguarda 1 segundo
    time.sleep(0.1)
