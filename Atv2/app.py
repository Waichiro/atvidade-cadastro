from interface2.menus import *
from arquivos2 import *

carro = 'cadVeiculo.txt'

alunos_arq = carro


if not arquivoExiste(carro):
    criarArquivo(carro)


while True:
    resposta = menu(['Cadastrar carro', 'Listar carro', 'Buscar carro', 'Remover carro', 'Alterar carro','Sair do programa'])

# ------------------------------------------------------------------------------------------------------

    if resposta == 1:

        while True:
            r = menu(['Cadastrar carro', 'Sair'])
            if r == 1:
                marca = "{0:<15}".format(input('Marca: '))
                descricao = "{0:<20}".format(input('descricao: '))
                preco = "{0:<10}".format(input('preco: '))
                ano = "{0:<6}".format(input('ano: '))
                placa = "{0:<10}".format(input('placa: '))
                cadastrarAluno(marca, descricao, preco, ano, placa)

            elif r == 2:
                print('Saindo...')
                break

            else:
                print('\033[31mDigite uma opção válida\033[m')

# ------------------------------------------------------------------------------------------------------

    elif resposta == 2:
        while True:
            r = menu(['Mostrar carro', 'Sair'])
            if r == 1:
                lerArquivo(carro)


                print(carro)
            elif r == 2:
                print('Saindo...')
                break
            else:
                print('\033[31mDigite uma opção válida\033[m')

# ------------------------------------------------------------------------------------------------------

    elif resposta == 3:
        while True:
            r = menu(['Buscar carro', 'Sair'])
            if r == 1:
                carro = open('cadVeiculo.txt', 'r')
                nome = input(str("Buscar carro: "))

                for linha in carro:
                    if nome in linha:
                        print(linha)

                carro.close()
            elif r == 2:
                print('Saindo...')
                break
            else:
                print('\033[31mDigite uma opção válida\033[m')

# ------------------------------------------------------------------------------------------------------

    elif resposta == 4:
        while True:
            r = menu(['Remover carro', 'Sair'])
            if r == 1:
                carro = open('cadVeiculo.txt', 'r')
                nome = input("Informe o carro que deseja remover: ")

                conteudo = carro.readlines()

                cont = 0
                for linha in conteudo:
                    if nome in linha:
                        conteudo.pop(cont)
                    cont = cont + 1

                carro = open('cadVeiculo.txt', 'w')
                carro.writelines(conteudo)
                carro.close()

            elif r == 2:

                print('Saindo...')

                break

            else:

                print('\033[31mDigite uma opção válida\033[m')

# ------------------------------------------------------------------------------------------------------

    elif resposta == 5:
        print("Nao soube fazer esse")
        break

    elif resposta == 6:
        cabecalho('Saindo')
        break

    else:
        print('\033[31mDigite uma opção válida\033[m')
