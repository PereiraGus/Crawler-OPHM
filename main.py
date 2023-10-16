import time as t # Biblioteca tempo: pausar a execução do programa
from urllib3 import PoolManager #Biblioteca urllib3: cliente HTTP para Python
from pick import pick #Biblioteca pick: menu controlado por setas
import keyboard as kb #Biblioteca teclado: capturar teclas pressionadas pelo usuário
import sys #Biblioteca sys: fechar o programa

from capturar_dados import capturarDados
from configuracoes import abrir_configuracoes

tempo_atualizacao = 1
guardar_no_banco = 0
guardar_em_csv = 1

while True:
    title = """
     \_______/
 `.,-'\_____/`-.,'
  /`..'\ _ /`.,'\\
 /  /`.,' `.,'\  \    Open
/__/__/     \__\__\__ Hardware
\  \  \     /  /  /   Crawler
 \  \,'`._,'`./  /
  \,'`./___\,'`./
 ,'`-./_____\,-'`.
     /       \\
Arte: https://www.asciiart.eu/animals/spiders

(Utilize as setas para cima e para baixo para escolher uma opção)"""
    options = ['Iniciar','Opções','Sair']
    option, index = pick(options, title,"→")

    if(option == 'Iniciar'):
        print("Carregando...")
        with PoolManager() as pool:
            while True:
                if(kb.is_pressed('esc')):
                    break
                capturarDados(pool,tempo_atualizacao,guardar_no_banco,guardar_em_csv)

    elif(option == 'Opções'):
        configuracoes_definidas = abrir_configuracoes(tempo_atualizacao,guardar_no_banco,guardar_em_csv)
        tempo_atualizacao = configuracoes_definidas[0]
        guardar_no_banco = configuracoes_definidas[1]
        guardar_em_csv = configuracoes_definidas[2]

    elif(option == 'Sair'):
        sys.exit()