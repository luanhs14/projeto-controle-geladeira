
print('-------------------------------------')
print('GERENCIAMENTO DE GELADEIRA')
print('1 - Adicionar produto')
print('2 - Editar produto')
print('3 - Excluir produto')
print('-------------------------------------')

opcao = input ('O que você deseja fazer: ')

if opcao == '1' :
    print('Adicionando...')
    nome_prod = input('Qual o nome do produto: ')
    qnt_prod = int (input('Quantos tem: '))
    val_prod = input('Qual a validade: ')
    lista = (nome_prod, qnt_prod, val_prod)
    #TODO incluir código do produto de forma aleatória
    #TODO salvar em algum BD
    print(lista)

elif opcao == '2' :
    print('Editando...')


elif opcao == '3' :
    print('Excluindo...')

else:
    print('Opção errada...')
