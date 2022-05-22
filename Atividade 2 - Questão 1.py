# Algoritmo de ordenação por troca
def ordenacao_troca(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenado = False

lista = [4, 5, 3, 3, 4, 7, 0, 4, 7, 1, 9, 5, 8, 3, 4]
ordenacao_troca(lista)
print(f"Lista ordenada por troca: {lista}")

# Algoritmo de Ordenação por Inserção
def ordenacao_insercao(lista):
     elemento = len(lista)
     for i in range(1, elemento):
         chave = lista[i]
         j = i - 1
         while j >= 0 and lista[j] > chave:
             lista[j + 1] = lista[j]
             j = j - 1
         lista[j + 1] = chave

lista = [5, 3, 2, 8, 6, 0, 1, 3, 2, 5, 6, 3, 5, 8, 2]
ordenacao_insercao(lista)
print(f"Lista ordenada por inserção: {lista}")

# Algoritmo de Ordenação por Seleção
def ordenacao_selecao(lista):
    elemento = len(lista)
    for i in range(elemento):
        minimo = i
        for j in range(i + 1, elemento):
            if lista[minimo] > lista[j]:
                minimo = j
            lista[i], lista[minimo] = lista[minimo], lista[i]

lista = [0, 3, 1, 5, 6, 8, 9, 7, 3, 5, 3, 7, 8]
ordenacao_selecao(lista)
print(f"Lista ordenada por seleção: {lista}")

# Algoritmo de Ordenação por Intercalação
def ordenacao_intercalacao(lista):
    if len(lista) > 1:
        dividir = len(lista) // 2
        metade_esquerda = lista[:dividir]
        metade_direita = lista[dividir:]

        ordenacao_intercalacao(metade_esquerda)
        ordenacao_intercalacao(metade_direita)

        i = 0
        j = 0
        k = 0
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i = i + 1
            else:
                lista[k] = metade_direita[j]
                j = j + 1
            k = k + 1

        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i = i + 1
            k = k + 1

        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j = j + 1
            k = k + 1

lista = [4, 5, 2, 0, 7, 8, 9, 5, 6, 8, 0, 9, 0]
ordenacao_intercalacao(lista)
print(f"Lista ordenada por intercalação: {lista}")

# Algoritmo de ordenação rápida
def ordenacao_rapida(lista):
    ajudante_ordenacao_rapida(lista, 0, len(lista)-1)

def ajudante_ordenacao_rapida(lista, primeiro, ultimo):
    if primeiro < ultimo:
        ponto_de_divisao = particao(lista, primeiro, ultimo)
        ajudante_ordenacao_rapida(lista, primeiro, ponto_de_divisao - 1)
        ajudante_ordenacao_rapida(lista, ponto_de_divisao + 1, ultimo)

def particao(lista, primeiro, ultimo):
    pivo = lista[primeiro]
    ponto_esquerdo = primeiro + 1
    ponto_direito = ultimo
    done = False

    while not done:

        while ponto_esquerdo <= ponto_direito and lista[ponto_esquerdo] <= pivo:
            ponto_esquerdo = ponto_esquerdo + 1

        while lista[ponto_direito] >= pivo and ponto_direito >= ponto_esquerdo:
            ponto_direito = ponto_direito - 1

        if ponto_direito < ponto_esquerdo:
            done = True
        else:
            temp = lista[ponto_esquerdo]
            lista[ponto_esquerdo] = lista[ponto_direito]
            lista[ponto_direito] = temp

    temp = lista[primeiro]
    lista[primeiro] = lista[ponto_direito]
    lista[ponto_direito] = temp

    return ponto_direito

lista = [0, 4, 9, 6, 7, 2, 3, 4, 5, 6, 7, 2, 4, 0, 8]
ordenacao_rapida(lista)
print(f"Lista ordenada pelo método rápida: {lista}")

# Algoritmo de Ordenação por Amontoamento
def ordenacao_amontoado(lista):
    tamanho = len(lista)
    for i in range(tamanho // 2 - 1, -1, -1):
        amontoador(lista, tamanho, i)

    for i in range(tamanho - 1, 0, -1):
        lista[i]
        amontoador(lista, i, 0)

def amontoador(lista, tamanho, i):
    maior = i
    direita = 2 * i + 1
    esquerda = 2 * i + 2
    if esquerda < tamanho and lista[i] < lista[esquerda]:
        maior = esquerda

    if direita < tamanho and lista[maior] < lista[direita]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        amontoador(lista, tamanho, maior)

lista = [3, 5, 1, 0, 7, 8, 5, 6, 1, 0, 0, 5, 9, 8]
ordenacao_amontoado(lista)
print(f"Lista ordenada por amontoamento: {lista}")

# Algoritmo de Busca Sequencial
def busca_sequencial(lista, chave):
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == chave:
            posicoes.append(i)

    if posicoes != []:
        print(f"O item está na lista nas posições: {posicoes}")

    elif posicoes == []:
        print("Esse elemento não está em nenhuma posição da lista.")

lista = [0, 3, 4, 5, 6, 2, 3, 8, 4, 5, 6, 7, 2, 4, 6]
chave = int(input("Digite o elemento que você que encontrar na lista, através da busca sequencial: "))
busca_sequencial(lista, chave)

# Algoritmo de Busca Binária
def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim)//2
        if lista[meio] == chave:
            return meio
        elif lista[meio] > chave:
            fim = meio - 1
        else:
            inicio = meio + 1
        return print("O elemento não está em nenhuma posição da lista")

lista = [0, 3, 2, 5, 6, 7, 4, 8, 7, 6, 4, 1, 2, 3, 4, 7, 6, 8, 5, 8, 9, 0]
ordenacao_troca(lista)
chave = int(input("Digite o elemento que procura: "))
print(f"O elemento está na posição: {busca_binaria(lista, chave)}")
print(f"Lista ordenada que foi feita a busca binária: {lista}")