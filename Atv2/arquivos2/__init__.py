from interface2.menus import *

from Atv2.interface2.menus import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("\033[31mHouve um erro na criacao do arquivo!\033[m")
    else:
        print(f'O arquivo {nome} foi criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabecalho('Alunos cadastrados(as)')
        print(a.read())
    finally:
        a.close()

def cadastrarAluno(alunos, nome='desconhecido', email='NAO INFORMADO' , curso= 'NAO INFORMADO'):
    try:
        a = open(alunos, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nome} - {email} - {curso}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados\033[m')
        else:
            print(f'Aluno,  {nome} adicionado.')
            a.close()

