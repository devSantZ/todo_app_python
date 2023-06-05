import os
from time import sleep
import sys


from functions import (scan_os, create_task,list_task,
                       edit_task, del_task, finalize_task)


if __name__ == '__main__':
    
    os.system(scan_os())
    while True:
        user = input('Escolha uma opção para continuar:\n'
            f'(1) Criar tarefa.\n'
            f'(2) Listar tarefa.\n'
            f'(3) Editar tarefa.\n'
            f'(4) Apagar tarefa.\n'
            f'(5) Finalizar tarefa.\n'
            f'(s) Para finalizar o programa.\n'
            f'-> ').lower()

        if user == '1':
            os.system(scan_os())
            create_task()
            
        elif user == '2':
            os.system(scan_os())
            list_task()
            
        elif user == '3':
            os.system(scan_os())
            edit_task()
            
        elif user == '4':
            os.system(scan_os())
            del_task()
            
        elif user == '5':
            os.system(scan_os())
            finalize_task()
            
        elif user == 's':
            os.system(scan_os())
            break
        
        else:
            os.system(scan_os())
            print('Por favor, escolha uma opção válida!')
            
            sleep(3)
            os.system(scan_os())
            continue