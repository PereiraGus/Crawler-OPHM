import sys #Biblioteca sys: recarregar o buffer do print()
import time as t # Biblioteca tempo: pausar a execução do programa

def erro_servidor():
    print("="*39," Segure ESC para sair ","="*39,end="\n\n")
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