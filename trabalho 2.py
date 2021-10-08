def criarUsuario (): ## Função para o cadastro de usuário com nome e email
    novoUsuario = {}
    novoUsuario ['nome'] = input('\nInsira o nome completo do usuário: \n')
    novoUsuario['email'] = input('Insira o email do usuário: ')
    return novoUsuario

def main (): ## Função para adicionar os usuários a uma lista
    listaUsuarios = []
    listaUsuarios.append(criarUsuario())
    menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.' /
    '\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.'/
    '\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.'/
    '\nDigite 4 para buscar um participante pelo nome'/
    '\nDigite 5 para remover um participante pelo email.'/
    '\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail'/
    '\nDigite qualquer outro número para sair '))
    while menu == 1:
        main ()
    if menu == 2:
        print('Lista de usuários: ', listaUsuarios)
    elif Escolha == 2:
       print('Lista por ordem alfabetica:', listaUsuarios.sort) #mostra por ordem alfabética
    elif Escolha == 3:
       print('Busca por nome:', listaUsuarios)#precisamos resolver issso
    elif Escolha == 4:
       print('excluindo por email:', listaUsuarios(input("inserir email de usuario")))#terminar essa lógica

        
if _name_ == '_main_':
    main ()

#coisas restantes:
#resolver o problema de cadastro de usuario ter máximo de 1, estou vendo no repplit alguma maneira de resolve-lo
#busca por nome
#excluir através do email: (criamos funções para a lógica ou escrevemos dentro da mesma?)