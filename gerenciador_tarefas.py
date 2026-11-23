import os
tarefas= []

def adicionar(lista):
    palavra = input('\nescreva sua tarefa à ser adicionada: ')
    lista.append(palavra)
    print(f'\nsua tarefa {palavra}, foi adicionada!\n')
                     
def retirar(lista):
    if len(lista) == 0:
        print('\nA lista já está vazia, não há o que retirar!\n')
        return
        
    ret_palavra = input('Escreva sua tarefa ou o número dela para ser retirada: ')
    
    if ret_palavra.isdigit():
        indice = int(ret_palavra) - 1
        if 0 <= indice < len(lista):
            tarefa_removida = lista.pop(indice)
            print(f'\nA tarefa "{tarefa_removida}" foi retirada!\n')
        else:
            print('\nNúmero de tarefa inválido!\n')
            
    else:
        if ret_palavra in lista:
            lista.remove(ret_palavra)
            print(f'\nA tarefa "{ret_palavra}" foi retirada!\n')
        else:
            print('\nTarefa não listada ou escrita errada!\n')

def ver_lista(lista):
  if len(lista) == 0:
    print("\nSua lista de tarefas está vazia!")
  else:
    print("\n--- SUAS TAREFAS ---")
    for indice, tarefa in enumerate(lista, start=1):
      print(f"{indice}. {tarefa}")
     
def sair():
     print('\n---INTERROMPENDO O SISTEMA!!---\n')
            
while True:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\n---MENU PRINCIPAL---\n')
    print('1-adicionar tarefa')
    print('2-retirar tarefa')
    print('3-ver lista de tarefas')
    print('4-sair')
    
    try:
      resposta = int(input('\nDigite o número escolhido: '))
    except ValueError:
      print('\nErro: Digite apenas um número inteiro válido!\n')
      input('Pressione Enter para continuar...')
      continue
    
    if resposta == 1:
        adicionar(tarefas)
        input('\nPressione Enter para voltar ao menu...')
    
    elif resposta == 2:
        retirar(tarefas)
        input('\nPressione Enter para voltar ao menu...')
        
    elif resposta == 3:
        ver_lista(tarefas)
        input('\nPressione Enter para voltar ao menu...')
        
    elif resposta == 4:
        sair()
        break
    else:
        print('\nopção invalida!! escolha um numero entre 1 e 4.\n')
        input('Pressione Enter para continuar...')