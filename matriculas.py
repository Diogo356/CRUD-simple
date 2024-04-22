list_matriculas = []

def matriculas():
    print('\n\n----- [MATRICULAS] MENU DE OPERAÇÕES -----\n\n')
    print ('(1) Incluir.')
    print ('(2) Listar.')
    print ('(3) Atualizar.')
    print ('(4) Excluir.')
    print ('(9) Voltar ao menu principal.\n')
    value = int(input("Insira um opção: "))
    return value

def matriculasLoop():
    while True:
        value = matriculas()
        if value == 9:
            break
        elif value < 1 or value > 5:
            continue
        else :
            if value == 1:
               matriculasincluir()
            elif value == 2:
               matriculaslistar()
    return 9

def matriculasincluir():
    print("\n\n ===== INCLUSÂO ===== \n\n")
    name = str(input("Nome do Aluno/Estudante: "))
    global list_matriculas
    list_matriculas.append(name)

def matriculaslistar():
    print("\n\n ===== LISTAGEM ===== \n\n")
    global list_matriculas
    for elemento in list_matriculas:
        print (elemento)