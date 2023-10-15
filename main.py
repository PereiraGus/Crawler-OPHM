import time as t # Biblioteca tempo: pausar a execução do programa
from urllib3 import PoolManager #Biblioteca urllib3: cliente HTTP para Python
from pick import pick #Biblioteca pick: menu controlado por setas
import keyboard as kb #Biblioteca teclado: capturar teclas pressionadas pelo usuário
import sys #Biblioteca sys: fechar o programa

from capturar_dados import capturarDados
from configuracoes import abrir_configuracoes

def conversor(valor):
    return float(valor[0:4].replace(",", '.'))

tempo_atualizacao = 1
guardar_no_banco = 1

while True:
    title = """API Crawler do Open Hardware Monitor
    (Utilize as setas para cima e para baixo para escolher uma opção)"""
    options = ['Iniciar','Opções','Sair']
    option, index = pick(options, title,"→")

    if(option == 'Iniciar'):
        print("Carregando...")
        with PoolManager() as pool:
            while True:
                if(kb.is_pressed('esc')):
                    break
                capturarDados(pool,tempo_atualizacao)

    elif(option == 'Opções'):
        configuracoes_definidas = abrir_configuracoes(tempo_atualizacao,guardar_no_banco)
        tempo_atualizacao = configuracoes_definidas[0]
        guardar_no_banco = configuracoes_definidas[1]

    elif(option == 'Sair'):
        sys.exit()