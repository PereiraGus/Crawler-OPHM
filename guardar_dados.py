import mysql.connector #Conector MySql
import datetime as dt #Biblioteca dataHora: pegar a data e hora atual

from erro import acusar_erro

def cortador(valor,casas):
    tamanho = len(str(valor))
    return valor[0:tamanho-casas]

def conversor(valor):
    return float(valor.replace(",", '.'))

def abrir_conexao():
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='userCrawler',
            password='urubu100',
            database='db_web_crawler'
        )
        return con
    except Exception as e:
        acusar_erro('banco',e)

def inserir_banco(infos):
    con = abrir_conexao()
    cursor = con.cursor()

    sql = "INSERT INTO tb_registro VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"

    infos['cpu_temp'] = conversor(cortador(infos['cpu_temp'],3))
    infos['cpu_uso'] = conversor(cortador(infos['cpu_uso'],2))
    infos['cpu_energia'] = conversor(cortador(infos['cpu_energia'],2))
    infos['ram_uso'] = conversor(cortador(infos['ram_uso'],2))
    infos['ram_utilizada'] = conversor(cortador(infos['ram_utilizada'],3))
    infos['ram_livre'] = conversor(cortador(infos['ram_livre'],3))

    val = [
        infos['nome_pc'],
        infos['cpu_modelo'],
        infos['cpu_temp'],
        infos['cpu_uso'],
        infos['cpu_energia'],
        infos['ram_uso'],
        infos['ram_utilizada'],
        infos['ram_livre']
    ]

    try:
        cursor.execute(sql,val)
        con.commit()
        print("Salvo no banco de dados!")
    except Exception as e:
        acusar_erro('banco',e)

def gravar_csv(infos):
    infos['cpu_temp'] = conversor(cortador(infos['cpu_temp'],3))
    infos['cpu_uso'] = conversor(cortador(infos['cpu_uso'],2))
    infos['cpu_energia'] = conversor(cortador(infos['cpu_energia'],2))
    infos['ram_uso'] = conversor(cortador(infos['ram_uso'],2))
    infos['ram_utilizada'] = conversor(cortador(infos['ram_utilizada'],3))
    infos['ram_livre'] = conversor(cortador(infos['ram_livre'],3))

    now = dt.datetime.now()
    nomeArquivo = "logs/dados"+now.strftime("%d-%m-%Y")+".csv"

    try:
        arquivo = open(nomeArquivo,"x")
        arquivo.close()

        arquivo = open(nomeArquivo,"wt")
        for key in infos:
            arquivo.write(key+",")
        arquivo.write("\n")
    except Exception as e:
        try:
            arquivo = open(nomeArquivo,"at")
            for key, value in infos.items():
                arquivo.write(str(value)+",")
            arquivo.write("\n")
        except Exception as e:
            print("Erro CSV")
            print(e)
    finally:
        arquivo.close()