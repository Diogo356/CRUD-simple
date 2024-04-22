list_professores = []

def professores():
    print('\n\n----- [PROFESSORES] MENU DE OPERÇÕES -----\n\n')
    print ('(1) Incluir.')
    print ('(2) Listar.')
    print ('(3) Atualizar.')
    print ('(4) Excluir.')
    print ('(9) Voltar ao menu principal.\n')
    value = int(input("Insira um opção: "))
    return value

def professoresLoop():
    while True:
        value = professores()
        if value == 9:
            break
        elif value < 1 or value > 5:
            continue
        else :
            if value == 1:
               professoresincluir()
            elif value == 2:
               professoreslistar()
    return 9

def professoresincluir():
    print("\n\n ===== INCLUSÂO ===== \n\n")
    name = str(input("Nome do Aluno/Estudante: "))
    global list_professores
    list_professores.append(name)

def professoreslistar():
    print("\n\n ===== LISTAGEM ===== \n\n")
    global list_professores
    for elemento in list_professores:
        print (elemento)