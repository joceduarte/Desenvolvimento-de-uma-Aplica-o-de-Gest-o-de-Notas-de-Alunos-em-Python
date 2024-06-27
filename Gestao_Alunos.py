''' 
Menu Interativo:
O programa deve exibir um menu com as seguintes opções:
1 - Adicionar aluno
2 - Listar alunos
3 - Remover aluno
4 - Procurar aluno
5 - Listar aprovados
6 - Listar reprovados
7 - Procurar pelo nome do aluno
8 - Média da turma B1
9 - Média da turma B2
10 - Média da turma geral
11 - Diário da turma
0 - Sair

'''

alunos = {}

def menu():
    print('1-Adicionar o Aluno: ')
    print('2- Listar Alunos: ')
    print('3- Remover Aluno: ')
    print('4- Procurar Aluno: ')
    print('5- Listar Aprovados: ')
    print('6- Listar Reprovados: ')
    print('7- Procurar pelo nome do Aluno: ')
    print('8- Média da turma B1: ')
    print('9- Média da turma B2: ')
    print('10- Média da turma Geral: ')
    print('11- Diário da Turma: ')
    print('0- sair')
    opt = input('Digite uma opção: ')
    return opt

def Adicionar_o_Aluno():
    ra = float(input('Digite o RA do Aluno: '))
    nome = input('Digite o nome do Aluno: ')
    B1 = float(input('Adicionar nota de B1: '))
    B2 = float(input('Adicionar nota de B2: '))
    alunos[ra]= {'Nome': nome, 'B1': B1, 'B2' : B2}
    print('Aluno Adicionado com sucesso !!!')
    input('Aperte Enter para continuar...')


def Listar_Alunos():
    for ra, dados in alunos.items():
        print(f'Numero RA: {ra} Dados do Aluno: {dados}')
    input('Aperte Enter tecla para continuar...')

def Remover_aluno():
    ra = input('Digite o RA do Aluno: ')
    if ra in alunos:
        nome = alunos.pop(ra)['name']
        print(f'O {ra} - {nome} foi excluido da lista!') 
    else:
        print(f'O {ra} - não esta na Lista!')
    input('Aperte Enter para continuar...')
    
def procurar_aluno():
    ra = input('Digite o RA do Aluno: ')
    if ra  in alunos:
        dados = alunos[ra]
        print(f'{ra} - {dados},- B1: {dados['B1']}, B2: {dados['B2']}')

def listar_aprovados():
    for ra, dados in alunos.items():
        media = (dados['B1'] + dados ['B2']) / 2
        if media >= 7:
            print(f'{ra}- {dados}- media: {media}')
    input('Aperte Enter para continuar...')

def listar_reprovados():
    for ra,dados in alunos.items():
        media = (dados['B1'] + dados['B2']) / 2
        if media <= 7:
            print(f'{ra} - {dados} - media: {media}')
    input('Aperte Enter para continuar...')

def procurar_nome_aluno():
    nome = input('Digite o nome do Aluno: ')
    for ra, dados in alunos.items():
        if dados == nome.lower():
            print(f'{ra} - {dados['nome']} - B1: {dados['B1']} - B2: {dados['B2']}')
    input('Aperte Enter para continuar...')

def media_da_turma_B1():
    if alunos:
        media = sum(dados['B1'] for dados in alunos.values()) / len(alunos)
        print(f'media da turma B1: {media}')
    else:
        print('Não ha alunos cadastrados.')
    input('Aperte Enter para continuar...')

def media_da_turma_B2():
    if alunos:
        media = sum(dados['B2'] for dados in alunos.values()) / len(alunos)
        print(f'Media da turma de B2: {media}')
    else:
        print('Não ha alunos cadastrados.')
    input('Aperte Enter para continuar...')

def media_da_turma_geral():
    if alunos:
        media = sum((dados['B1'] + dados ['B2']) / 2 for dados in alunos.values()) / len(alunos)
        print(f'A media da turma Geral: {media}')
    else:
        print('Não ha Alunos Cadstrados.')
    input('Aperte qualquer tecla para continuar.')

def formatar_valor(valor, largura, alinhamento = 'left'):
    if alinhamento == 'left':
        return str(valor).ljust(largura)
    elif alinhamento =='right':
        return str(valor).rjust(largura)
    else:
        return str(valor).center(largura)
    
def diario_da_turma():
    print('-------------------------------------------------')
    print(formatar_valor('Diario da turma', 56, 'center'))
    print('-------------------------------------------------')
    print(formatar_valor('RA', 6) + formatar_valor('nome', 25)+ formatar_valor('Nota de B1', 9) + formatar_valor('Nota de B2', 9) + formatar_valor('media', 7))
    print('-------------------------------------------------')


    soma_B1 = 0 
    soma_B2 = 0 
    soma_media = 0
    for ra, dados in alunos.items():
        media = (dados['B1'] + dados['B2']) / 2
        soma_B1 += dados['B1']
        soma_B2 += dados ['B2']
        soma_media += media
        print(formatar_valor(ra, 6) + formatar_valor (dados, 25) + formatar_valor(f'{dados['B1']:.2f}', 9 , 'right') + formatar_valor(f'{dados['B2']:.2F}', 9 , 'right') + formatar_valor(f'{media:.2f}', 7, 'right'))
    
        print('--------------------------------------------------')
    if alunos:
        num_alunos = len(alunos)
        media_da_turma_B1 = soma_B1 / num_alunos
        media_da_turma_B2 = soma_B2 / num_alunos
        media_da_turma_geral = soma_media / num_alunos
        print(formatar_valor('Media da turma', 31) + formatar_valor (f'{media_da_turma_B1:.2f}', 9 , 'right') + formatar_valor(f'{media_da_turma_B2:.2f}',9 , 'right') + formatar_valor(f'{media_da_turma_geral:.2f}', 7, 'right'))
    print('----------------------------------------------')
    input('Aperte qualquer tecla para continuar...')


while True:
    opt = menu()
    if opt == '1':
        Adicionar_o_Aluno()
    elif opt == '2':
        Listar_Alunos()
    elif opt == '3':
        Remover_aluno()
    elif opt == '4':
        procurar_aluno()
    elif opt == '5':
        listar_aprovados()
    elif opt == '6':
        listar_reprovados()
    elif opt == '7':
        procurar_nome_aluno()
    elif opt == '8':
        media_da_turma_B1()
    elif opt == '9':
        media_da_turma_B2()
    elif opt == '10':
        media_da_turma_geral()
    elif opt == '11':
        diario_da_turma()
    elif opt == '0':
        break
    else:
        print('Opção invalida, tente novamente!')
