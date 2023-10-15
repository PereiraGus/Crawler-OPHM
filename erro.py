import sys #Biblioteca sys: recarregar o buffer do print()
import time as t # Biblioteca tempo: pausar a execução do programa

def erro_ophm():
    return """
[!] O servidor do Open Hardware Monitor não foi detectado
Siga as instruções abaixo para iniciá-lo:
    1. Abra seu Open Hardware Monitor.
    2. No menu superior, acesse o item \"Options\" > \"Remote Web Server\" > \"Port\".
    3. Configure a por como 9000.
    4. Volte à opção \"Remote Web Server\" e clique em \"Run\" para iniciar o servidor.
    """

def erro_banco():
    return """
[!] Falha na conexão com o banco de dados
    • Verifique se o serviço \"mysql\" está em execução na sua máquina.
    • Verifique se o banco, a tabela e o usuário foram criados corretamente.
    """

def acusar_erro(tipo,texto_erro):
    print("="*39," Segure ESC para sair ","="*39,end="\n")

    if(tipo == 'ophm'):
        print(erro_ophm())
    elif(tipo == 'banco'):
        print(erro_banco())
    
    print("Texto do erro:\n\t",texto_erro,end="\n\n")
    print("Tentando conectar de novo em 10...")
    contador = 9
    while(contador != 0):
        print(" "+str(contador), end="..."),
        #Recarregando o buffer do print, que fica preso até um '\n' se não for forçando manualmente
        sys.stdout.flush()
        t.sleep(1)
        contador-=1
    print("\n\nTentando se reconectar...")