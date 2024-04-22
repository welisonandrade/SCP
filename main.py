from empresa import Empresa
from funcionarios import *
from controle_acesso import ControleDeAcesso

empresa = Empresa()
admin = Admin('Welison', 'Gerente', 'Desenvolvimento', 15696584358)
# func = NotAdmin('Flávio','Software Engineer', 'Desenvolvimento', 68794852612)


ControleDeAcesso.register(Admin)
ControleDeAcesso.register(NotAdmin)

def retornarAdmin():
    print('\nDeseja retornar?')
    print('1 - Sim')
    #print('2 - Não')
    esc = input('---> ')
    if esc == '1':
        print('\n'*6)
        areaAdmin()
    else:
        #exit()
        print('\n'*6)
        areaAdmin()

def retornarFunc(obj):
    print('\nDeseja retornar?')
    print('1 - Sim')
    #print('2 - Não')
    esc = input('---> ')
    if esc == '1':
        print('\n'*6)
        areaFunc(obj)
    else:
        #exit()
        print('\n'*6)
        areaFunc(obj)

def menu():
    print('SISTEMA DE CONTROLE DE PONTO')
    print('\n1 - Área do administrador')
    print('2 - Área do funcionário')
    op1 = input('---> ')
    print('\n'*6)

    if op1 == '1':
        #ÁREA ADMINISTRADOR

        print('SISTEMA DE CONTROLE DE PONTO - ADMIN')
        print('\n\nEssa é uma ala reservada para administradores,\npor favor insira a senha:')
        userPass = input('---> ')
        print('\n'*6)
        
        #verifica se é admin
        if userPass == admin.getSenha:
            #chama a func pela primeira vez
            areaAdmin()
        else:
            print('Senha incorreta! Tente novamente.')
            menu()

    elif op1 == '2':
        #ÁREA FUNCIONÁRIO
        
        #verifica se já existe ao menos uma pessoa cadastrada.
        if not bool(empresa.getFuncionarios):
            print("O administrador não cadastrou nenhum funcionário até o momento.")
            menu()
        else:
            print('SISTEMA DE CONTROLE DE PONTO - FUNCIONÁRIO')
            print('\nPara logar, use seu nome como username e cpf como senha.')
            
            username = input('\nNome de usuário: ')
            senha = input('Senha: ')

            aux_obj = NotAdmin('a','b','c',999)
            aux_obj = aux_obj.realizaLogin(empresa,username,senha)

        #retorna false se não existe, ou se a senha ou username estão errados. Do contrário, retorna um objeto.
        if type(aux_obj) == bool:
            print('\n'*6)
            print("Usuário ou senha incorreto(a)")
            menu()
        else:
            print('\n'*6)
            print('\nVocê está logado como {}'.format(aux_obj._nome))
            areaFunc(aux_obj)

    #tratamento de erro
    elif type(op1) == str:
        menu()

def areaAdmin():
    print('SISTEMA DE CONTROLE DE PONTO - ADMIN: {}'.format(admin.getName))
    print('\n1 - Cadastrar funcionario')
    print('2 - Excluir funcionario ')
    print('3 - Verificar frequência de funcionário ')
    print('4 - Exibir lista de funcionários que podem logar ')
    print('5 - Voltar ao menu principal ')
    op2 = input('---> ')
    print('\n'*6)

    #cadastra login de funcionario
    if op2 == '1':
        print('SISTEMA DE CONTROLE DE PONTO - ADMIN - CADASTRO')
        nome = input('\nDigite o nome: ')
        cpf = input('Digite o cpf: ')
        cargo = input('Digite o cargo: ')
        setor = input('Digite o setor: ')

        if nome.isnumeric() or cargo.isnumeric() or setor.isnumeric():
            print('\n'*6)
            print('Funcionário não cadastrado. Nome, cargo ou setor não podem ser números.')
            areaAdmin()
        
        if type(cpf)==str:
            try:
                int(cpf)
            except:
                print('\n'*6)
                print("Funcionário não cadastrado. CPF não pode conter letras.")
                areaAdmin()

        aux_name = nome
        aux_name = NotAdmin(nome,cargo,setor,cpf)
        admin.cadastraLogin(aux_name,empresa)
        print('\n'*6)

        print('Funcionário cadastrado com sucesso!')
        areaAdmin()

    #exclui login do funcionario    
    elif op2 == '2':
        if not bool(empresa.getFuncionarios):
            print("Não existe nenhum funcionário a ser apagado.")
            areaAdmin()
        else:
            print('Lista de funcionários que podem logar:\n')
            empresa.imprimirF()
            choice = input("Digite o cpf da pessoa que deseja excluir da lista: ")
            if type(choice) == str:
                try: 
                    int(choice)
                    if choice in empresa._funcionarioLogaveis.keys():
                        empresa.getFuncionarios.pop(choice)
                        print('\n'*6)
                        print('Cadastro excluído com sucesso!')
                        areaAdmin()
                    else:
                        print('\n'*6)
                        print('\nCPF digitado é inexistente!')
                        areaAdmin()
                except:
                    print('\n'*6)
                    print("\nVocê não digitou um número.")
                    areaAdmin()
    elif op2 == '3':
        #verifica frequencia do funcionario
        print('\n'*6)
        print('SISTEMA DE CONTROLE DE PONTO - ADMIN: {}'.format(admin.getName))
        #Verifica se tem ao menos um funcionario cadastrado
        if not bool (empresa.getFuncionarios):
            print('\n'*6)
            print('Cadastre ao menos um funcionário antes de ver o seu histórico.')
            areaAdmin()
        else:
            print('Funcionários cadastrados no sistema: ')
            empresa.imprimirFName()
            dado = input('\nDigite o cpf do usuário que deseja verificar frequência: ')
            print('\n'*6)

            #verifica se o cpf ao menos existe dentro do dicionario
            if dado in empresa.getFuncionarios.keys():
                #Agr que sabe que existe, procura por ele pra localizar de qual objeto ele pertence
                for x in empresa.getFuncionarios.keys():
                    if dado == x:
                        if not bool(empresa.getFuncionarios[x]._historico):
                            print('\n'*6)
                            print('{} ainda não registrou nenhum ponto.'.format(empresa.getFuncionarios[x]._nome))
                            retornarAdmin()
                        else:
                            print('\nHistórico de {}'.format(empresa.getFuncionarios[x]._nome))
                            print(empresa.getFuncionarios[x]._historico)
                            retornarAdmin()
            else:
                print('\n'*6)
                print('\nCPF digitado é inexistente!')
                areaAdmin()

    elif op2 == '4':
        #verifica se já foi cadastrado alguém na lista de login
        if not bool(empresa.getFuncionarios):
            print('\n'*6)
            print("Nenhum funcionário foi cadastrado até o momento.")
            areaAdmin()
        else:
            print('Funcionários que podem logar:\n')   
            empresa.imprimirF()
            retornarAdmin()

    elif op2 == '5':
        print('\n'*6)
        menu()

def areaFunc(objeto):
    print('SISTEMA DE CONTROLE DE PONTO - FUNCIONÁRIO')
    print('1 - Registrar ponto')
    print('2 - Visualizar histórico de frequência')
    print('3 - Deslogar')

    pick = input('---> ')

    if pick == '1':
        print('\n'*6)
        objeto.registraPonto()
        areaFunc(objeto)
    
    elif pick == '2':
        print('\n'*6)
        
        if not bool(objeto.getHistorico):
            print('\n'*6)
            print('Você ainda não possue nenhum registro de ponto.')
            areaFunc(objeto)
        else:
            print('Esse é seu histórico de pontos batidos:')
            objeto.imprimirHistorico()
            print('\n')
            retornarFunc(objeto)

    elif pick == '3':
        print('\n'*6)
        menu()

    elif type(pick) == str:
        pass

menu()