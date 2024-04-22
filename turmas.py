list_turmas = []

def turmas():
    print('\n\n----- [TURMAS] MENU DE OPERAÇÕES -----\n\n')
    print ('(1) Incluir.')
    print ('(2) Listar.')
    print ('(3) Atualizar.')
    print ('(4) Excluir.')
    print ('(9) Voltar ao menu principal.\n')
    value = int(input("Insira um opção: "))
    return value

def turmasLoop():
    while True:
        value = turmas()
        if value == 9:
            break
        elif value < 1 or value > 5:
            continue
        else :
            if value == 1:
               turmasincluir()
            elif value == 2:
               turmaslistar()
    return 9

def turmasincluir():
    print("\n\n ===== INCLUSÂO ===== \n\n")
    name = str(input("Nome do Aluno/Estudante: "))
    global list_turmas
    list_turmas.append(name)

def turmaslistar():
    print("\n\n ===== LISTAGEM ===== \n\n")
    global list_turmas
    for elemento in list_turmas:
        print (elemento)