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
        cabecalho('Caros cadastrados')
        print("{0:<15}".format("Marca"), "{0:<22}".format("Descricao"), "{0:<12}".format("Preco"),
              "{0:<8}".format("Ano"), "{0:<15}".format("Placa"))
        print(a.read())
    finally:
        a.close()

def cadastrarAluno(marca, descricao='desconhecido', preco='NAO INFORMADO' , ano= 'NAO INFORMADO', placa= "nao informado" ):
    try:
        a = open('cadVeiculo.txt', 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{marca} {descricao} {preco} {ano} {placa}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados\033[m')
        else:
            print(f'Carro {marca} adicionado.')
            a.close()

