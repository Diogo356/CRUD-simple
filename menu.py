from disciplinas import *

def menu(): 
    print ('\n\n----- MENU PRINCIPAL -----\n\n')
    print ('(1) Gerenciar estudantes.')
    print ('(2) Gerenciar professores.')
    print ('(3) Gerenciar disciplina.')
    print ('(4) Gerenciar turmas.')
    print ('(5) Gerenciar matriculas.')
    print ('(9) Sair.\n')
    valor = int(input("Escolha uma Opção: ")) 
    return valor
