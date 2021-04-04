def quickSortIterativo (lista, pivoTipo):

    limites = [(0, len(lista)-1)]

    while len(limites) != 0:
        bot, top = limites.pop()

        if (top - bot < 1):
            continue
        elif (top-bot == 1):
            if(lista[bot] < lista[top]):
                continue
            else:
                lista[bot], lista[top] = lista[top], lista[bot]
                continue
       
        if (pivoTipo == "inicio"):
            pivot = lista.pop(bot)
        elif (pivoTipo == "fim"):
            pivot = lista.pop(top)
        elif (pivoTipo == "meio"):
            pivot = lista.pop((bot+top)//2)
        else :
            raise ValueError("Pivo incorreto")

        i = bot
        j = top-1
        while (True):
            while (lista[i] < pivot): 
                i += 1
                if (i > j): break

            while (lista[j] >= pivot): 
                j -=1
                if (i > j): break
            
            if (i > j): break
            lista [i], lista[j] = lista[j], lista[i]

        if (i == bot): 
            lista.insert(i,pivot)
            i += 1
        elif (j == top-1): 
            lista.insert(top,pivot)
        else:
            lista.insert(i,pivot)


        limites.append((bot,j))
        limites.append((i,top))

    return lista


def quickSortRecursivo(lista, pivoTipo):
    tam = len(lista)

    if(tam <= 1): return lista

    if (pivoTipo == "inicio"):
        pivot = lista.pop(0)
    elif (pivoTipo == "fim"):
        pivot = lista.pop(-1)
    elif (pivoTipo == "meio"):
        pivot = lista.pop(tam//2)
    else :
        raise ValueError("Pivo incorreto")

    menores = []
    maiores = []
    for i in range (tam-1):
        if (lista[i] < pivot):
            menores.append(lista[i])
        elif lista[i] >= pivot: 
            maiores.append(lista[i])

    return quickSortRecursivo(menores,pivoTipo) + [pivot] + quickSortRecursivo(maiores,pivoTipo)


def mergeSort(lista):
    tam = len(lista)
    half = tam//2

    if (tam <= 1):
        return lista
    elif(tam == 2):
        a,b = (lista.pop(),lista.pop())
        if(a > b):
            return [b,a]
        else:
            return [a,b]

    esquerda = mergeSort(lista[:half]) 
    direita = mergeSort(lista[half:])

    merged = []
    for _ in range(tam):
        if(len(esquerda) == 0):
            return merged + direita

        if(len(direita) == 0):
            return merged + esquerda

        if (direita[0] < esquerda[0]):
            merged.append(direita.pop(0))
        else:
            merged.append(esquerda.pop(0))


def insertionSort(lista):
    tam = len(lista)
    for i in range(tam):
        temp = tam-1
        trocou = False
        for j in range(tam-2, i-1, -1):
            if (lista[j] > lista[temp]):
                lista[temp], lista[j] = lista[j], lista[temp]
                temp = j
                trocou = True
            else:
                temp = j

        if(not trocou):
            return lista

    return lista

def mergeInsertionSort(lista):
    tam = len(lista)
    half = tam//2

    if(tam < 36):
        return insertionSort(lista)

    esquerda = mergeSort(lista[:half]) 
    direita = mergeSort(lista[half:])

    merged = []
    for _ in range(tam):
        if(len(esquerda) == 0):
            return merged + direita

        if(len(direita) == 0):
            return merged + esquerda

        if (direita[0] < esquerda[0]):
            merged.append(direita.pop(0))
        else:
            merged.append(esquerda.pop(0))


def heapify(lista, start, end):
    if(start*2 > end): # não tem nenhum filho
        return
    elif(start*2+1 > end): # tem apenas um filho
        if (lista[start-1] < lista[start*2-1]):
            lista[start-1],lista[start*2-1] = lista[start*2-1], lista[start-1]
        return
    
    # tem os dois filhos
    maiorFilho = start*2 if lista[start*2-1] > lista[start*2+1-1] else start*2+1

    if(lista[start-1] < lista[maiorFilho-1]):
        lista[start-1],lista[maiorFilho-1] = lista[maiorFilho-1], lista[start-1]
        heapify(lista, maiorFilho, end)

    return lista

def heapSort(lista):
    tam = len(lista)
    for i in range(tam, -1, -1):
        heapify(lista, i+1, tam)

    tam -= 1
    while(tam > 0):
        lista[tam], lista[0] = lista[0], lista[tam]
        tam -= 1
        heapify(lista, 1, tam+1)

    return lista


# nota: hGen deve eventualmente
# retornar 1 e 0 em sequencia
# e nao deve retornar n, tal que n>=size
def shellSort(lista, hGen):
    tam = len(lista) -1
    if tam <= 1 : return lista

    gen = hGen(tam+1)
    h = next(gen)

    while(h != 0):
        for i in range(tam, 0, -h):
            aux = tam

            for j in range(tam-h, tam-i-1, -h):
                if (lista[j] < lista[aux]):
                    aux = j
                else:
                    lista[aux], lista[j] = lista[j], lista[aux]
                    aux = j
        h = next(gen)

    return lista

#Exemplos de hGens
def knuthsSequence(size):
    h = 1
    for _ in range((size+1)//9): h = 3*h+1

    while (h > 0):
        yield h
        h = (h-1)//3
    yield 0
    
def marcinCiuraSequence(size):
    seq = [0,1,4,10,23,57,137,301,701,1750]
    seq.reverse()

    for i in seq:
        if (i < size):
            yield i

def powers2minus1sequence(size):
    seq = []
    aux = 1
    i = 1
    while (aux < size):
        seq.append(aux)
        aux = 2**i -1
        i += 1

    seq.pop(0)
    seq.reverse()
    for i in seq:
        yield i

    yield 0
