list_estudantes = []

def estudantes():
    print('\n\n----- [ESTUDANTES] MENU DE OPERAÇÕES -----\n\n' )
    print ('(1) Incluir.')
    print ('(2) Listar.')
    print ('(3) Atualizar.')
    print ('(4) Excluir.')
    print ('(9) Voltar ao menu principal.\n')
    value = int(input("Insira um opção: "))
    return value

def estudantesLoop():
    while True:
        value = estudantes()
        if value == 9:
            break
        elif value < 1 or value > 5:
            continue
        else :
            if value == 1:
                estudantesincluir()
            elif value == 2:
                estudanteslistar()
    return 9

def estudantesincluir():
    print("\n\n ===== INCLUSÂO ===== \n\n")
    name = str(input("Nome do Aluno/Estudante: "))
    global list_estudantes
    list_estudantes.append(name)

def estudanteslistar():
    print("\n\n ===== LISTAGEM ===== \n\n")
    global list_estudantes
    for elemento in list_estudantes:
        print (elemento)
