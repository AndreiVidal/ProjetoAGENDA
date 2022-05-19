AGENDA = dict()

def entrada_valores():
    cpf = input('Digite o cpf: ')
    while not cpf.isnumeric():  # verifica se o cpf contém numeros
        print('Cpf deve conter apenas números')
        cpf = input('Digite o cpf novamente: ')
    else:
        email = input('Digite o email: ')
        endereco = input('Digite o endereco: ')
    return cpf, email, endereco


def quantidade_contatos():
    qtd = len(AGENDA)
    if qtd > 1:
        print(f'Existem {qtd} contatos salvos na AGENDA!')
    elif qtd == 1:
        print(f'{qtd} contato salvo na agenda.')
    else:
        print('Nenhum contato salvo na AGENDA.')


def buscar_contato(contato):
    print(f'NOME:{contato.capitalize()}')
    print(f"CPF: {AGENDA[contato]['cpf']}")
    print(f"EMAIL: {AGENDA[contato]['email']}")
    print(f"ENDEREÇO: {AGENDA[contato]['endereco']}")
    print()


def mostrar_contatos():
    if len(AGENDA) == 0:
        print('Agenda vazia!')
    else:
        quantidade_contatos()
        for contato in AGENDA:
            buscar_contato(contato)


def adicionar_contato():
    contato = input('Digite o nome do contato: ')
    contato = contato.capitalize()
    if contato in AGENDA:
        print('Contato já existe')
    else:

        cpf, email, endereco = entrada_valores()
        AGENDA[contato] = {
            'cpf': cpf,
            'email': email,
            'endereco': endereco
        }

        print()
        print(f'Contato {contato} adicionado com sucesso.')


def excluir_contato():
    contato = input('Digite o contato para excluir: ')
    if contato in AGENDA:
        AGENDA.pop(contato)
        print(f'Contato {contato} excluido com sucesso!')
    else:
        print(f'contato {contato} não encontrado!')


def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                contatos = (linha.strip().split(';'))
                AGENDA[contatos[0]] = {
                    'cpf': contatos[1],
                    'email': contatos[2],
                    'endereco': contatos[3]
                }
            salvar()
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as error:
        print(error)


def salvar():
    try:
        with open('dataBase.csv', 'w') as arquivo:
            for contato in AGENDA:
                cpf = AGENDA[contato]['cpf']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato};{cpf};{email};{endereco}\n')
    except Exception as error:
        print(error)


def carregar():
    try:
        with open('dataBase.csv') as arq:
            #('Carregando contatos...')
            linhas = arq.readlines()
            for linha in linhas:
                contatos = (linha.strip().split(';'))
                AGENDA[contatos[0]] = {
                    'cpf': contatos[1],
                    'email': contatos[2],
                    'endereco': contatos[3]
                }

    except:
        quantidade_contatos()


def menu_agenda():
    print('''
    
    MENU:
    [1] - Mostrar contatos:
    [2] - Buscar contatos:
    [3] - Adicionar contato:
    [4] - Editar contato:
    [5] - Excluir contato:
    [6] - Importar contatos:
    [0] - Sair:
     
    ''')


carregar()
salvar()
while True:

    menu_agenda()
    opcao = input('Digite uma opção: ')
    if not opcao.isnumeric():
        print('Digite um número válido.')
        continue
    else:
        opcao = int(opcao)

    if opcao == 1:
        mostrar_contatos()

    elif opcao == 2:
        contato = entrada_valores()
        try:
            buscar_contato(contato)
        except KeyError:
            print('Contato inexistente.')

    elif opcao == 3:
        adicionar_contato()
        salvar()



    elif opcao == 4:
        contato = entrada_valores()

        if not contato[0] in AGENDA:
            print('Contato inexistente!')
            continue
        else:
            adicionar_contato()
            print(f'Contato {contato} editado com sucesso!')
            salvar()

    elif opcao == 5:
        excluir_contato()
        salvar()

    elif opcao == 6:
        diretorio = input('Digite o nome do arquivo para importação: ')
        importar_contatos(diretorio)
        print('Exportação feita com sucesso!!')

    elif opcao == 0:
        break
