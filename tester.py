import ordenacao as o
import time, random, sys

def isSorted(lista):
    for i in range(len(lista)-1):
        if (lista[i] > lista[i+1]):
            print (str(lista[i]) + " é maior do que " + str(lista[i+1]) )
            print ("erro na posicao: " + str(i))
            return False
    return True

def novaLista(tamanho):
    with open("amostra",'w') as f:
        for item in random.sample(range(-int(1e10),int(1e10)), tamanho):
            f.write(str(item)+"\n")

        f.flush()
        f.close()

def carregarAmostra():
    temp = []
    with open("amostra",'r') as f:
        for item in f.readlines():
            temp.append(int(item))
        f.close()

    return temp


#É recomendado ocultar alguns algorimos se o tempo de cada ordenação
#exceder 3 minutos. Confira a tabela de resultados para esses dados.
def algoritmos():
    return {
        #'MergeSort':             lambda x: o.mergeSort(x),
        #'MergeInsertionSort':    lambda x: o.mergeInsertionSort(x),
        #'QuickSortR-inicio':     lambda x: o.quickSortRecursivo(x, "inicio"),
        #'QuickSortR-Fim':        lambda x: o.quickSortRecursivo(x, "fim"),
        #'QuickSortR-meio':       lambda x: o.quickSortRecursivo(x, "meio"),
        #'QuickSortI-inicio':     lambda x: o.quickSortIterativo(x, "inicio"),
        #'QuickSortI-Fim':        lambda x: o.quickSortIterativo(x, "fim"),
        #'QuickSortI-meio':       lambda x: o.quickSortIterativo(x, "meio"),
        #'heapSort':              lambda x: o.heapSort(x),
        #'ShellSort-marcinCiura': lambda x: o.shellSort(x, o.marcinCiuraSequence),
        #'ShellSort-knuths':      lambda x: o.shellSort(x, o.knuthsSequence),
        #'ShellSort-powers2-1':   lambda x: o.shellSort(x, o.powers2minus1sequence),
    }

#print("Quantas amostras?")
#novaLista(int(input()))
novaLista(5_000_000)
amostra = carregarAmostra()
print("\n\n\n\n\n\n\n\n\n")
print("arquivo carregado, amostra com: " + str(len(amostra)) + " numeros")


for nome, algo in algoritmos().items():
    tempoTotal = 0
    interacoes = 10

    for it in range(interacoes):
        parcial = amostra.copy()
        random.shuffle(parcial)

        inicio = time.time()
        ordenado = algo(parcial) 
        fim = time.time()

        if not isSorted(ordenado): 
            print("FALHA "+ nome)
            tempoTotal = -1
            break
        else:
            delta = int((fim-inicio)*100_000)/100_000
            print(str(it)+" parcial: "+str(delta))
            tempoTotal += delta
    
    if(tempoTotal != -1):
        tempoMedio = int((tempoTotal)*100_000)/(100_000 * interacoes)

        print("SUCESSO "+ nome)
        print("Tempo medio: "+ str(tempoMedio) +"s")
        #input()


print("\n\n\n")