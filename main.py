from menu import *
from aux import *
from time import *
def main() :
    while True:
        try:
            valid = menu()
            if valid == 9:
                print("\n\n----- Encerrado Sistema... -----\n\n")
                sleep(2)
                break
            elif valid < 1 or valid > 5 :
                print("\n\nEssa opção não existe. Por favor, Escolha uma das Opções listadas Acima!")
                sleep(2)
                continue
            else :
                while True:
                    value = callFunctions(valid)
                    if value == 9:
                        break
        except KeyboardInterrupt:
            continue
                    
main()