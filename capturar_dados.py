from json import loads #Biblioteca json: ler arquivos JSON
import time as t # Biblioteca tempo: pausar a execução do programa
import datetime as dt #Biblioteca dataHora: pegar a data e hora atual
from erro_servidor import erro_servidor

def capturarDados(pool, tempo_atualizacao):
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

        print("="*39," Segure ESC para sair ","="*39,end="\n")

        t.sleep(tempo_atualizacao)
    except:
        erro_servidor()