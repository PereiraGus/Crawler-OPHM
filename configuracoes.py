from pick import pick #Biblioteca pick: menu controlado por setas

def abrir_configuracoes(p_tempo,p_banco):
    tempo_atualizacao = p_tempo
    guardar_no_banco = p_banco
    opcao_tempo = 'Tempo de atualização: '+str(tempo_atualizacao)

    texto_banco = ""
    if(guardar_no_banco == 1): texto_banco = "Sim"
    else: texto_banco = "Não"
    opcao_banco = 'Salvar no banco de dados: '+str(texto_banco)

    title = 'Opções'
    options = [opcao_tempo,opcao_banco,'Voltar']
    option, index = pick(options, title,"→")

    if(option == opcao_tempo):
        title = 'Tempo de atualização da coleta de dados (em segundos)'
        options = ['1','2','5','10','15','30','60']
        option, index = pick(options, title,"→")
        tempo_atualizacao = int(option)

    if(option == opcao_banco):
        title = 'Salvar informações capturadas no banco de dados'
        options = ['Sim','Não']
        option, index = pick(options, title,"→")

        if(option == 'Sim'):
            guardar_no_banco = 1
        else:
            guardar_no_banco = 0
    
    return [tempo_atualizacao,guardar_no_banco]