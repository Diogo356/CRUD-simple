from menu import *
from estudantes import *
from disciplinas import *
from matriculas import *
from professores import *
from turmas import *

def callFunctions(valor):
    if valor == 1:
        estudantesLoop()
    elif valor == 2:
        professoresLoop()
    elif valor == 3:
        diciplinasLoop()
    elif valor == 4:
        turmasLoop()
    else:
        matriculasLoop()
    return 9