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
