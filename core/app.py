import os
from time import sleep
from typing import List

list_of_task: List[str] = []
tasks_finisheds: List[str] = []

def exit_func() -> None:
    """
    Função que exibe uma mensagem de saída e limpa a tela.
    Aguarda por uma entrada do usuário e retorna quando qualquer tecla for pressionada.
    """
    exit_user = input('Pressione qualquer tecla para sair.  ')
    os.system('clear')
    if exit_user:
        return

def create_task() -> None:
    """
    Função que permite ao usuário criar uma nova tarefa.
    Solicita ao usuário que insira o texto da tarefa e a adiciona à lista de tarefas.
    Verifica se a entrada está vazia ou contém apenas espaços em branco antes de adicionar a tarefa.
    Exibe mensagens de erro caso a entrada seja inválida ou a tarefa já esteja na lista.
    """
    try:
        user_task = input('Insira uma tarefa na sua TODO: ')
        if not user_task.strip():
            raise ValueError('A tarefa não pode estar vazia ou conter apenas espaços.')

        if user_task in list_of_task:
            print('A tarefa já está na lista.')
        else:
            list_of_task.append(user_task)
            os.system('clear')
            print(f'Você adicionou "{user_task}" na sua lista de afazeres.')
            sleep(1)
            os.system('clear')
    except ValueError as ve:
        print(f'Erro: {ve}')
    except Exception as e:
        print(f'Erro: {e.__class__.__name__} - {e}')

def list_task() -> None:
    """
    Função que exibe a lista de tarefas atual.
    Percorre a lista de tarefas e exibe cada tarefa com um índice.
    Exibe um marcador "(x)" se a tarefa estiver na lista de tarefas concluídas, caso contrário, exibe "( )".
    Chama a função exit_func() para aguardar uma entrada do usuário antes de retornar.
    """
    if len(list_of_task) == 0:
        print('Voce aind não tem uma tarefa!')
    for i, j in enumerate(list_of_task):
        i = str(i)
        if j in tasks_finisheds:
            print(i.replace(i, '(x)'), j)
        else:
            print(i.replace(i, '( )'), j)
    exit_func()

def edit_task() -> None:
    """
    Função que permite ao usuário editar uma tarefa existente.
    Exibe a lista de tarefas com seus índices e solicita ao usuário que insira o índice da tarefa a ser editada.
    Em seguida, solicita o novo valor para a tarefa e atualiza a lista de tarefas.
    Exibe mensagens de erro caso o índice seja inválido.
    """
    for i, v in enumerate(list_of_task):
        print(i, v)
    try:
        task_for_edit = int(input('Índice a editar: '))
        new_value = input('Reescrevendo tarefa: ')
        list_of_task[task_for_edit] = new_value
        print('Tarefa editada com sucesso')
        sleep(2)
        os.system('clear')
    except IndexError:
        print('Não existe esse índice.')
    except ValueError:
        print('Insira apenas índices válidos.')

def del_task() -> None:
    """
    Função que permite ao usuário excluir uma tarefa existente.
    Exibe a lista de tarefas com seus índices e solicita ao usuário que insira o índice da tarefa a ser removida.
    Remove a tarefa da lista de tarefas e exibe uma mensagem de confirmação.
    Exibe mensagens de erro caso o índice seja inválido.
    """
    for i, v in enumerate(list_of_task):
        print(i, v)
    try:
        task_for_del = int(input('Insira o índice da tarefa a ser removida: '))
        print(f'A tarefa "{list_of_task[task_for_del]}" foi removida com sucesso!')
        sleep(2)
        os.system('clear')
        list_of_task.pop(task_for_del)
    except IndexError:
        print('Não existe esse índice.')
    except ValueError:
        print('Insira apenas índices válidos.')

def finalize_task() -> None:
    """
    Função que permite ao usuário marcar uma tarefa como concluída.
    Exibe a lista de tarefas com seus índices e solicita ao usuário que insira o índice da tarefa a ser concluída.
    Marca a tarefa como concluída adicionando-a à lista de tarefas concluídas.
    Exibe mensagens de erro caso o índice seja inválido ou a tarefa já tenha sido concluída.
    """
    for i, v in enumerate(list_of_task):
        print(i, v)
    try:
        indice = int(input('Tarefa a concluir: '))
        if not indice in tasks_finisheds:
            value = list_of_task[indice]
            tasks_finisheds.append(value)
            print(f'Parabéns, voce concluiu a tarefa {value}')
            sleep(2)
            os.system('clear')
        else:
            print('Essa tarefa já foi concluída')
    except IndexError:
        print('Não existe esse índice.')
    except ValueError:
        print('Insira apenas índices válidos.')

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
        os.system('clear')
        create_task()
    elif user == '2':
        os.system('clear')
        list_task()
    elif user == '3':
        os.system('clear')
        edit_task()
    elif user == '4':
        os.system('clear')
        del_task()
    elif user == '5':
        os.system('clear')
        finalize_task()
    elif user == 's':
        os.system('clear')
        break
    else:
        os.system('clear')
        print('Por favor, escolha uma opção válida!')
        sleep(3)
        os.system('clear')
        continue
