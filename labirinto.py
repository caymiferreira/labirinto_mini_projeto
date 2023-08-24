from collections import deque
from gera_lab import gera_lab, print_lab

linhas = 6
colunas = 10
comeca = (1,0)
termina = (linhas-2,colunas-1)

def eh_possivel_sair(lab):
    fila = deque([comeca])
    marcado = set()

    while fila:
        atual = fila.popleft()

        if atual == termina:
            return True

        marcado.add(atual)

        linha, coluna = atual
        proximos = [(linha, coluna-1), (linha-1, coluna), (linha, coluna+1), (linha+1, coluna)]

        for proximo in proximos:
            proxima_linha, proxima_coluna = proximo

            if 0 <= proxima_coluna < len(lab[0]) and 0 <= proxima_linha < len(lab) and lab[proxima_linha][proxima_coluna] == ' ' and proximo not in marcado:
                fila.append(proximo)
    return False
