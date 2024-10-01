import csv
from collections import Counter


def extraiResultadosPorAno(lista, ano):
    listaAno = []
    for linha in lista:
        if (str(linha[0]) == ano):
            listaAno.append(linha)
    lista_ordenada = sorted(listaAno, key=lambda x: x[1])
    return lista_ordenada

def ler_arquivo(arquivo_origem):
    lista = []
    with open(arquivo_origem, 'r', encoding='UTF-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


lista = ler_arquivo('resultados_jogos.csv')

def time_mais_vencedor(lista, ano_inicio, ano_fim):
    vitorias_mandante = Counter()
    vitorias_visitante = Counter()
    
    
    for linha in lista[1:]:  
        ano = int(linha[0])
        if ano_inicio <= ano <= ano_fim:
            gols_mandante = linha[17]  
            gols_visitante = linha[18]  
            
            if gols_mandante.isdigit() and gols_visitante.isdigit():
                gols_mandante = int(gols_mandante)
                gols_visitante = int(gols_visitante)
                
                if gols_mandante > gols_visitante:
                    vitorias_mandante[linha[7]] += 1  
                elif gols_visitante > gols_mandante:
                    vitorias_visitante[linha[8]] += 1  
    
    
    time_mandante_mais_vencedor = vitorias_mandante.most_common(1)
    time_visitante_mais_vencedor = vitorias_visitante.most_common(1)
    
    return time_mandante_mais_vencedor, time_visitante_mais_vencedor

time_mandante_mais_vencedor, time_visitante_mais_vencedor = time_mais_vencedor(lista, 2010, 2020)

print(f"Time mandante mais vencedor: {time_mandante_mais_vencedor[0][0]} com {time_mandante_mais_vencedor[0][1]} vitórias")
print(f"Time visitante mais vencedor: {time_visitante_mais_vencedor[0][0]} com {time_visitante_mais_vencedor[0][1]} vitórias")


def tecnicos_mais_vencedores(lista, ano_inicio, ano_fim):
    vitorias_tecnicos = Counter()
    
    for linha in lista[1:]:  
        ano = int(linha[0])
        if ano_inicio <= ano <= ano_fim:
            gols_mandante = linha[17]  
            gols_visitante = linha[18] 
        
            if gols_mandante.isdigit() and gols_visitante.isdigit():
                gols_mandante = int(gols_mandante)
                gols_visitante = int(gols_visitante)
                
                if gols_mandante > gols_visitante:
                    tecnico_mandante = linha[9]
                    if tecnico_mandante:
                        vitorias_tecnicos[tecnico_mandante] += 1
                elif gols_visitante > gols_mandante:
                    tecnico_visitante = linha[10]
                    if tecnico_visitante:
                        vitorias_tecnicos[tecnico_visitante] += 1
    

    tecnicos_mais_vencedores = vitorias_tecnicos.most_common(3)
    
    return tecnicos_mais_vencedores

tecnicos_mais_vencedores = tecnicos_mais_vencedores(lista, 2010, 2020)
print("Os três técnicos com mais vitórias entre 2010 e 2020 são:")
for tecnico, vitorias in tecnicos_mais_vencedores:
    print(f"Técnico: {tecnico}, Vitórias: {vitorias}")


from collections import Counter

def jogos_por_tecnico(lista, tecnicos_mais_vencedores, ano_inicio, ano_fim):
    participacoes_tecnicos = Counter()
    tecnicos_alvo = [tecnico for tecnico, _ in tecnicos_mais_vencedores]
    
    for linha in lista[1:]:  
        ano = int(linha[0])
        if ano_inicio <= ano <= ano_fim:
            tecnico_mandante = linha[9] 
            tecnico_visitante = linha[10]  
            
            if tecnico_mandante in tecnicos_alvo:
                participacoes_tecnicos[tecnico_mandante] += 1
            if tecnico_visitante in tecnicos_alvo:
                participacoes_tecnicos[tecnico_visitante] += 1
    
    return participacoes_tecnicos

participacoes_tecnicos = jogos_por_tecnico(lista, tecnicos_mais_vencedores, 2010, 2020)
print("Participação de jogos dos técnicos mais vitoriosos entre 2010 e 2020:")
for tecnico, jogos in participacoes_tecnicos.items():
    print(f"Técnico: {tecnico}, Jogos: {jogos}")