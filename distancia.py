import PySimpleGUI as sg
import csv
import win32gui
import win32con

sg.theme('DarkAmber')  # Adiciona um toque de cor

# Lê o arquivo CSV e retorna o último valor da segunda coluna
def get_last_value(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        if data:
            last_row = data[-1]
            if len(last_row) > 1:
                return last_row[1]
    return None

# Caminho do arquivo CSV
csv_file_path = r'C:\Users\elima\Desktop\UFPB\E-MOTION\emotionweb\data3.csv'


# conteudo da Janela
layout = [
    [sg.Text('Último valor da segunda coluna do arquivo CSV:')],
    [sg.Text(size=(20, 1), key='-OUTPUT-')],
    [sg.Button('Sair')]
]

# Cria a Janela
window = sg.Window('Título da Janela', layout, finalize=True)  # Adicione o parâmetro finalize=True

# Maximiza a janela
window.maximize()

# Obtém o valor inicial do arquivo CSV
last_value = get_last_value(csv_file_path)
window['-OUTPUT-'].update(last_value)

# Exibe a barra de tarefas
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# Loop de Eventos para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read(timeout=1)  # Verifica eventos a cada 1 segundo
    if event == sg.WIN_CLOSED or event == 'Sair':  # Se o usuário fechar a janela ou clicar em sair
        break

    # Verifica se houve alteração no arquivo CSV
    new_value = get_last_value(csv_file_path)
    if new_value != last_value:
        last_value = new_value
        window['-OUTPUT-'].update(last_value)

window.close()
