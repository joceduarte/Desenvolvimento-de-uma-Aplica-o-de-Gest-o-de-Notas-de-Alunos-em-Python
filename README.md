# Desenvolvimento-de-uma-Aplica-o-de-Gest-o-de-Notas-de-Alunos-em-Python
Professor Ariel

Começamos o projeto com o fazendo um dicionario para alocamento dos dados 
alunos = {}

Em seguida inserimos o comando DEF, para que o menu e os comando a seguir sejam repeditos e executados quantas vezes forem necessario
Ex: def menu(): 

depois das menu interativo para usuario usamos uma VARIAVEL ligada ao menu para ser selecionada as opcões e um RETURN para a opção escolhida 
Ex: opt = input('Digite uma opção: ')
    return opt

E entao vamos montado cada coluna de comando DEF seguindo da sequencia do MENU interativo do usuario.
Ex: def Adicionar_o_Aluno():
    def Listar_Alunos():
E cada coluna de comando com suas respectivas comando 
tantos como IF, FOR, WHILE.

O FOR para buscar dados e verificar, buscando no os dados adicionado ao dicionario 
Ex: for ra, dados in alunos.items():
        media = (dados['B1'] + dados['B2']) / 2
        soma_B1 += dados['B1']
        
O IF E ELSE, para podermos estar validando as opções escolhidas pelos usuarios e dando retorno de comando que estejam ou nao dentro da programação
procurada pelo usuario.
Ex: if alunos:
        media = sum(dados['B2'] for dados in alunos.values()) / len(alunos)
        print(f'Media da turma de B2: {media}')
    else:
        print('Não ha alunos cadastrados.')
        
Temos o WHILE TRUE, que faz com que tenhamos as repeticoes das nossas colunas quando verdadeiras, assim agilizando o processo de resposta ao usuario.
Ex: while True:
    opt = menu()
    if opt == '1':
        Adicionar_o_Aluno()
    elif opt == '2':
        Listar_Alunos()
    elif opt == '3':
