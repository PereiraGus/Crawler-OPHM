from json import loads #Biblioteca json: ler arquivos JSON
import time as t # Biblioteca tempo: pausar a execução do programa
import datetime as dt #Biblioteca dataHora: pegar a data e hora atual
from urllib3 import PoolManager #Biblioteca urllib3: cliente HTTP para Python
import sys #Biblioteca sys: recarregar o buffer do print()
from pick import pick #Biblioteca pick: menu controlado por setas

def conversor(valor):
    return float(valor[0:4].replace(",", '.'))

tempoAtualizacao = 1

while True:
    title = """API Crawler do Open Hardware Monitor
    (Utilize as setas para cima e para baixo para escolher uma opção)"""
    options = ['Iniciar','Opções']
    option, index = pick(options, title,"→")
    
    if(option == 'Opções'):
        title = 'Opções'
        options = ['Tempo de atualização','Voltar']
        option, index = pick(options, title,"→")

        if(option == 'Tempo de atualização'):
            title = 'Tempo de atualização da coleta de dados (em segundos)'
            options = ['1','2','5','10','15','30','60']
            option, index = pick(options, title,"→")
            tempoAtualizacao = int(option)

    if(option == 'Iniciar'):
        print("Carregando...")
        with PoolManager() as pool:
            while True:

                try:
                    response = pool.request('GET', 'http://localhost:9000/data.json',
                                            timeout=1.0,retries=1)# Timeout de 1 segundo com 1 tentativa
                    data = loads(response.data.decode('utf-8'))

                    root = data['Children'][0]['Children']
                    user = data['Children'][0]['Text']
                    now = dt.datetime.now()

                    print(now.strftime("\n%H:%M:%S - %d/%m/%Y"),end="\t")
                    print("Usuário utilizador: "+user)
                    
                    cpu = root[0]
                    cpuModelo = cpu['Text']
                    cpuTemperatura = cpu['Children'][1]['Children'][4]['Value']
                    cpuPctUso = cpu['Children'][2]['Children'][0]['Value']
                    cpuEnergia = cpu['Children'][3]['Children'][0]['Value']

                    print("CPU:")
                    print("\t• Modelo da CPU: "+cpuModelo,end="\t")
                    print("\t• Temperatura: "+cpuTemperatura)
                    print("\t• Percentual de uso: "+cpuPctUso,end="\t")
                    print("\t• Eletricidade consumida: "+cpuEnergia,end="\n")

                    ram = root[1]
                    ramPctUso = ram['Children'][0]['Children'][0]['Value']
                    ramUsada = ram['Children'][1]['Children'][0]['Value']
                    ramLivre = ram['Children'][1]['Children'][1]['Value']

                    print("RAM:")
                    print("\t• Percentual de uso: "+ramPctUso,end="\t")
                    print("\t• RAM Utilizada: "+ramUsada,end="\t")
                    print("\t• RAm Livre: "+ramLivre,end="\n\n")

                    print("="*100,end="\n")

                    t.sleep(tempoAtualizacao)
                except:
                    print("="*100,end="\n\n")
                    print("[!] O servidor do Open Hardware Monitor não foi detectado")
                    print("Siga as instruções abaixo para iniciá-lo:")
                    print("\t1. Abra seu Open Hardware Monitor.")
                    print("\t2. No menu superior, acesse o item \"Options\" > \"Remote Web Server\" > \"Port\".")
                    print("\t3. Configure a por como 9000.")
                    print("\t4. Volte à opção \"Remote Web Server\" e clique em \"Run\" para iniciar o servidor.")
                    print("Tentando de novo em 10...", end="")
                    contador = 9
                    while(contador != 0):
                        print(" "+str(contador), end="..."),
                        #Recarregando o buffer do print, que fica preso até um '\n' se não for forçando manualmente
                        sys.stdout.flush()
                        t.sleep(1)
                        contador-=1
                    print("\n\nTentando se reconectar...")
