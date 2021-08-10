'''
'r' -> Somente para ler
'w' -> Somente para escrever
'r+' -> Para ler e escrever
'a' -> Para acrescentar
'''


print('-------------------------------------')
print('GERENCIAMENTO DE GELADEIRA')
print('1 - Adicionar produto')
print('2 - Editar produto')
print('3 - Excluir produto')
print('4 - Visualizar todos os itens')
print('-------------------------------------')

opcao = input ('O que você deseja fazer: ')
tupla = ()

if opcao == '1' :
        print('Adicionando...')
        nome_prod = input('Qual o nome do produto? ')
        qnt_prod = int (input('Quantos tem? '))
        val_prod = input('Qual a validade? ')
        tupla = (nome_prod, qnt_prod, val_prod)
    #TODO incluir código do produto de forma aleatória
        print(tupla)
        
        with open('save.txt','a') as arquivo:
            for valor in tupla:
                arquivo.write(str(valor) + '\n')

elif opcao == '2' :
    print('Editando...')

    #with open('save.txt','r+') as arquivo:
    #        for valor in arquivo:
    #            arquivo.write(str(valor) + '\n')


elif opcao == '3' :
    print('Excluindo...')
    del tupla[ str (input('Quem deseja remover? '))]

elif opcao == '4' :
    tuplas = ()
    with open('save.txt', 'r') as arquivo:
        for valor in arquivo:
            print(valor)
    
else:
    print('Opção errada...')
