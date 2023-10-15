from json import loads #Biblioteca json: ler arquivos JSON
import time as t # Biblioteca tempo: pausar a execução do programa
import datetime as dt #Biblioteca dataHora: pegar a data e hora atual

from guardar_banco import inserir_banco
from erro import acusar_erro

def capturarDados(pool, tempo_atualizacao, guardar_banco):
    try:
        response = pool.request('GET', 'http://localhost:9000/data.json',
                                timeout=1.0,retries=1)# Timeout de 1 segundo com 1 tentativa
        data = loads(response.data.decode('utf-8'))

        root = data['Children'][0]['Children']
        pc = data['Children'][0]['Text']
        now = dt.datetime.now()

        print(now.strftime("\n%H:%M:%S - %d/%m/%Y"),end="\t")
        print("Nome do computador: "+pc)
                    
        cpu = root[0]
        cpu_modelo = cpu['Text']
        cpu_temperatura = cpu['Children'][1]['Children'][4]['Value']
        cpu_pct_uso = cpu['Children'][2]['Children'][0]['Value']
        cpu_energia = cpu['Children'][3]['Children'][0]['Value']

        print("CPU:")
        print("\t• Modelo da CPU: "+cpu_modelo,end="\t")
        print("\t• Temperatura: "+cpu_temperatura)
        print("\t• Percentual de uso: "+cpu_pct_uso,end="\t")
        print("\t• Eletricidade consumida: "+cpu_energia,end="\n")

        ram = root[1]
        ram_pct_uso = ram['Children'][0]['Children'][0]['Value']
        ram_usada = ram['Children'][1]['Children'][0]['Value']
        ram_livre = ram['Children'][1]['Children'][1]['Value']

        print("RAM:")
        print("\t• Percentual de uso: "+ram_pct_uso,end="\t")
        print("\t• RAM Utilizada: "+ram_usada,end="\t")
        print("\t• RAm Livre: "+ram_livre,end="\n\n")

        if(guardar_banco == 1):
            infos = {
                'nome_pc':pc,
                'cpu_modelo':cpu_modelo,
                'cpu_temp':cpu_temperatura,
                'cpu_uso':cpu_pct_uso,
                'cpu_energia':cpu_energia,
                'ram_uso':ram_pct_uso,
                'ram_utilizada':ram_usada,
                'ram_livre':ram_livre
            }
            inserir_banco(infos)
        
        print("="*39," Segure ESC para sair ","="*39,end="\n")
        t.sleep(tempo_atualizacao)
    except Exception as e:
        acusar_erro('ophm',e)