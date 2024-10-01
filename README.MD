Projeto utilizado para analisar dados sobre Futebol utilizando python, funções realizadas para:
Etapa 1 - Desenvolva uma função em Python que retorna o nome do time mandante e do
time visitante mais vencedor do campeonato brasileiro entre 2010 e 2020, juntamente
com o total de jogos vencidos durante esse intervalo de tempo.
Etapa 2 - Desenvolva uma função quer retorna os nomes dos três técnicos que venceram
mais partidas entre 2010 e 2020, juntamente com o total de jogos que venceram durante
esse intervalo de tempo.
Etapa 3 - Desenvolva uma função que retorna a quantidade de jogos que cada um dos
técnicos encontrados na solução da questão 2 participou entre 2010 e 2020.
Etapa 4 - Desenvolva uma função que retorna o time mais vitorioso em todo o conjunto de
dados.

Código Inicial:
import csv

def extraiResultadosPorAno(lista, ano):
    listaAno = []
    for linha in lista:
        if (str(linha[0]) == ano):
            listaAno.append(linha)
    lista_ordenada = sorted(listaAno, key=lambda x: x[1])
    return lista_ordenada

def ler_arquivo(arquivo_origem):
    lista = []
    with open(arquivo_origem, 'r', encoding='iso-8859-1') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


lista = ler_arquivo('resultados_jogos.csv')
#lista2012 = extraiResultadosPorAno(lista, '2002')
print(lista)


Arquivo manteve o mesmo, sendo alterado, por mim, para codificação UTF-8 para melhor apresentação do resultado final.