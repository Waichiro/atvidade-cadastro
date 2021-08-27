from interface2.menus import *
from arquivos2 import *

alunos = 'alunos.txt'

alunos_arq = alunos


if not arquivoExiste(alunos):
    criarArquivo(alunos)


while True:
    resposta = menu(['Cadastrar Aluno', 'Listar Alunos', 'Buscar Alunos', 'Remover Alunos', 'Alterar Aluno','Sair do programa'])

# ------------------------------------------------------------------------------------------------------

    if resposta == 1:

        while True:
            r = menu(['Cadastrar Aluno', 'Sair'])
            if r == 1:
                nome = str(input('Nome: '))
                email = str(input('Email: '))
                curso = str(input('Curso: '))
                cadastrarAluno(alunos, nome, email, curso)

            elif r == 2:
                print('Saindo...')
                break

            else:
                print('\033[31mDigite uma opção válida\033[m')

# ------------------------------------------------------------------------------------------------------

    elif resposta == 2:
        while True:
            r = menu(['Mostrar Alunos', 'Sair'])
            if r == 1:
                lerArquivo(alunos)

                print(alunos)
            elif r == 2:
                print('Saindo...')
                break
            else:
                print('\033[31mDigite uma opção válida\033[m')

# ------------------------------------------------------------------------------------------------------

    elif resposta == 3:
        while True:
            r = menu(['Buscar Aluno', 'Sair'])
            if r == 1:
                alunos = open('alunos.txt', 'r')
                nome = input(str("Buscar aluno: "))

                for linha in alunos:
                    if nome in linha:
                        print(linha)

                alunos.close()
            elif r == 2:
                print('Saindo...')
                break
            else:
                print('\033[31mDigite uma opção válida\033[m')

# ------------------------------------------------------------------------------------------------------

    elif resposta == 4:
        while True:
            r = menu(['Remover Aluno', 'Sair'])
            if r == 1:
                alunos = open('alunos.txt', 'r')
                nome = input(str("Buscar aluno: "))

                alunos_arq = alunos.readline()

                count = 0
                for linha in alunos_arq:
                    if nome in linha:
                        alunos_arq.pop(count)

                    count = count + 1

                alunos = open('alunos.txt', 'w')
                alunos.writelines(alunos_arq)

                alunos.close()


            elif r == 2:

                print('Saindo...')

                break

            else:

                print('\033[31mDigite uma opção válida\033[m')

# ------------------------------------------------------------------------------------------------------





    elif resposta == 6:
        cabecalho('Saindo')
        break

    else:
        print('\033[31mDigite uma opção válida\033[m')
