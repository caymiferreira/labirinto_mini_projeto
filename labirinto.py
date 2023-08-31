from collections import deque
from gera_lab import gera_lab, print_lab

linhas = 6
colunas = 10
comeca = (1,0)
termina = (linhas-2,colunas-1)

def eh_possivel_sair(lab):
    pilha = deque([comeca])
    marcado = set()

    while pilha:
        atual = pilha.popleft()

        if atual == termina:
            return True

        linha, coluna = atual
        marcado.add(atual)
        direita = linha, coluna+1
        abaixo = linha+1, coluna
        esquerda = linha, coluna-1
        acima = linha-1, coluna

        proximos = [direita, abaixo, esquerda, acima]

        for proximo in proximos:
            proxima_linha, proxima_coluna = proximo

            if 0 <= proxima_coluna < len(lab[0]) and 0 <= proxima_linha < len(lab) and lab[proxima_linha][proxima_coluna] == ' ' and proximo not in marcado:
                pilha.append(proximo)
    return False

def print_lab(lab):
    lab_str = '\n'.join([''.join(row) for row in lab])
    print(lab_str)

if __name__ == '__main__':

    labirinto = gera_lab(linhas, colunas)

    labirinto1 = [
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
[' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
['#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

    labirinto2 = [
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
[' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' '],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

    resultado_esperado1 = True

    print_lab(labirinto1)
    resultado1 = eh_possivel_sair(labirinto1)

    print(resultado1 == resultado_esperado1)
