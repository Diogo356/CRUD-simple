list_disciplinas = []

def diciplinas() :
    print('\n\n----- [DISCIPLINAS] MENU DE OPERAÇÕES -----\n\n')
    print ('(1) Incluir.')
    print ('(2) Listar.')
    print ('(3) Atualizar.')
    print ('(4) Excluir.')
    print ('(9) Voltar ao menu principal.\n')
    value = int(input("Insira um opção: "))
    return value

def diciplinasLoop():
    while True:
        value = diciplinas()
        if value == 9:
            break
        elif value < 1 or value > 5:
            continue
        else :
            if value == 1:
                diciplinasincluir()
            elif value == 2:
                diciplinaslistar()
    return 9

def diciplinasincluir():
    print("\n\n ===== INCLUSÂO ===== \n\n")
    name = str(input("Nome do Aluno/Estudante: "))
    global list_disciplinas
    list_disciplinas.append(name)

def diciplinaslistar():
    print("\n\n ===== LISTAGEM ===== \n\n")
    global list_disciplinas
    for elemento in list_disciplinas:
        print (elemento)