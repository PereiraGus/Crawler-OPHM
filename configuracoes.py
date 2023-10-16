from pick import pick #Biblioteca pick: menu controlado por setas

def abrir_configuracoes(p_tempo,p_banco,p_csv):
    tempo_atualizacao = p_tempo
    guardar_no_banco = p_banco
    guardar_csv = p_csv

    opcao_tempo = 'Tempo de atualização: '+str(tempo_atualizacao)

    opcao_banco = 'Salvar no banco de dados: '
    if(guardar_no_banco == 1): opcao_banco += "sim"
    else: opcao_banco += "não"

    opcao_csv = 'Salvar para arquivo CSV: '
    if(p_csv == 1): opcao_csv += "sim"
    else: opcao_csv += "não"

    title = 'Configurações'
    options = [opcao_tempo,opcao_banco,opcao_csv,'Voltar']
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
    
    if(option == opcao_csv):
        title = 'Salvar informações capturadas em arquivo CSV'
        options = ['Sim','Não']
        option, index = pick(options, title,"→")

        if(option == 'Sim'):
            guardar_csv = 1
        else:
            guardar_csv = 0

    return [tempo_atualizacao,guardar_no_banco,guardar_csv]