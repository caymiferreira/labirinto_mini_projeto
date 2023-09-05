from gera_lab import gera_lab, print_lab

linhas = 6
colunas = 10
comeca = (1, 0)
termina = (linhas - 2, colunas - 1)

def eh_possivel_sair(lab):
    # Inicializa uma lista como uma pilha com a posição de início
    pilha = [comeca]
    # Inicializa um conjunto para rastrear as posições já visitadas
    marcado = set()

    # Enquanto a pilha não estiver vazia, continue explorando o labirinto
    while pilha:
        # O atual vai ser o elemento do topo da pilha (última posição explorada)
        atual = pilha.pop()

        # Verifica se a posição atual é igual à posição de término
        if atual == termina:
            return True

        # Obtém as coordenadas da posição atual
        linha, coluna = atual
        # Adiciona a posição atual ao conjunto de posições marcadas como visitadas
        marcado.add(atual)

        # Calcula as coordenadas das posições vizinhas nas direções: direita, abaixo, esquerda e acima
        direita = linha, coluna + 1
        abaixo = linha + 1, coluna
        esquerda = linha, coluna - 1
        acima = linha - 1, coluna

        # Cria uma lista com as coordenadas das posições vizinhas
        proximos = [direita, abaixo, esquerda, acima]

        # Itera sobre as posições vizinhas
        for proximo in proximos:
            proxima_linha, proxima_coluna = proximo

            # Verifica se a próxima posição está dentro dos limites do labirinto,
            # se é uma posição válida (espaço vazio) e se não foi marcada como visitada
            if (
                0 <= proxima_coluna < len(lab[0])
                and 0 <= proxima_linha < len(lab)
                and lab[proxima_linha][proxima_coluna] == " "
                and proximo not in marcado
            ):
                # Adiciona a próxima posição à pilha para explorá-la posteriormente
                pilha.append(proximo)

    # Se o loop terminar e não encontrar uma saída, retorna False
    return False

def print_lab(lab):
    for i in lab:
        # Junta os caracteres em cada linha do labirinto em uma única string
        # e imprime a linha
        print("".join(i))

# Verifica se o script está sendo executado como o programa principal
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
