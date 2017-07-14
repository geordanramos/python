import random
from random import randrange
import timeit
import matplotlib.pyplot as p
import math
 
lista = []
tempo1 = []
tempo2 = []
tempo3 = []
tempo4 = []
tempo5 = []
tempo6 = []
tempo7 = []
tempo8 = []
tempo9 = []
 
def listarandom (tam):
    random.seed()
    i = 0
    while i < tam:
        num = random.randint(1, 10 * tam)
        if num not in lista:
            lista.append(num)
            i += 1
 
def selectionsort (lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1,len(lista)):
            if (lista[j]<lista[menor]):
                menor = j
        if (i != menor):
            temp = lista[i]
            lista[i] = lista[menor]
            lista[menor] = temp

def bubblesort (lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if (lista[j]>lista[j+1]):
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
 
 def insertionsort(lista):
    for i in range(1,len(lista)):
        temp = lista[i]
        j = i
        while j > 0 and temp < lista[j-1]:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = temp
 
def pqsort(lista,começo,fim,pivo):
    lista[pivo],lista[fim] = lista[fim],lista[pivo]
    indice = começo
    for i in range(começo,fim):
        if lista[i] < lista[fim]:
            lista[i],lista[indice] = lista[indice],lista[i]
            indice += 1
    lista[indice],lista[fim] = lista[fim],lista[indice]
    return indice
 
def quicksort(lista,começo,fim):
    if começo >= fim:
        return lista
    pivo = randrange(começo,fim+1)
    new_pivo = pqsort(lista,começo,fim,pivo)
    quicksort(lista,começo,new_pivo-1)
    quicksort(lista,new_pivo+1,fim)
 
def merge(lista, começo, fim, pivo):
    n1 = fim - começo + 1
    n2 = pivo - fim
    right, left = [], []
    for i in range(n1):
        left.append(lista[começo + i])
    for j in range(n2):
        right.append(lista[fim + j + 1])
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(começo, pivo + 1):
        if left[i] <= right[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1
 
def mergesort(lista, começo, pivo):
    if começo < pivo:
        fim = (começo + pivo) // 2
        mergesort(lista, começo, fim)
        mergesort(lista, fim + 1, pivo)
        merge(lista, começo, fim, pivo)
 
def shellsort(lista):
     aux = len(lista) // 2
     while aux > 0:
         for i in range(aux, len(lista)):
             val = lista[i]
             j = i
             while j >= aux and lista[j - aux] > val:
                 lista[j] = lista[j - aux]
                 j -= aux
             lista[j] = val
         aux //= 2
 
def countingsort(lista, maxval):
    n = len(lista)
    m = maxval + 1
    count = [0] * m
    for a in lista:
        count[a] += 1
        i = 0
    for a in range(m):
        for c in range(count[a]):
            lista[i] = a
            i += 1
    return lista
 
def radixsort(lista):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
  
  while not maxLength:
    maxLength = True
    buckets = [list() for _ in range( RADIX )]
  
    for  i in lista:
      tmp = i // placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
  
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        lista[a] = i
        a += 1
  
    placement *= RADIX
 
def hashing(lista):
    m = lista[0]
    for i in range(1, len(lista)):
        if ( m < lista[i] ):
            m = lista[i]
    result = [m,int(math.sqrt( len(lista)))]
    return result
 
def re_hashing(i, code ):
    return int(i/code[0]*(code[1]-1))
 
def bucketsort(lista):
    code = hashing(lista)
    buckets = [list() for _ in range( code[1] )]
    for i in lista:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        insertionsort(bucket)
         
    ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            lista[ndx] = v
            ndx += 1
 
tamanho = [250,500,750,1000]
for g in range(len(tamanho)):
    del lista[:]
    listarand(tamanho[z])
    tempo = timeit.timeit("bubblesort({})".format(lista),setup="from __main__ import bubblesort", number=1)
    tempos1.append(tempo)
    tempo = timeit.timeit("selectionsort({})".format(lista),setup="from __main__ import selectionsort", number=1)
    tempos2.append(tempo)
    tempo = timeit.timeit("insertionsort({})".format(lista),setup="from __main__ import insertionsort", number=1)
    tempos3.append(tempo)
    tempo = timeit.timeit("quicksort({},{},{})".format(lista,0,len(lista)-1),setup="from __main__ import quicksort", number=1)
    tempos4.append(tempo)
    tempo = timeit.timeit("mergesort({},{},{})".format(lista,0,len(lista)-1),setup="from __main__ import mergesort", number=1)
    tempos5.append(tempo)
    tempo = timeit.timeit("shellsort({})".format(lista),setup="from __main__ import shellsort", number=1)
    tempos6.append(tempo)
    unicos = [i for i in lista if lista.count(i) < 2]
    max_value = max(unicos)
    tempo = timeit.timeit("countingsort({},{})".format(lista,max_value),setup="from __main__ import countingsort", number=1)
    tempos7.append(tempo)
    tempo = timeit.timeit("radixsort({})".format(lista),setup="from __main__ import radixsort", number=1)
    tempos8.append(tempo)
    tempo = timeit.timeit("bucketsort({})".format(lista),setup="from __main__ import bucketsort", number=1)
    tempos9.append(tempo)
     
 
p.plot(tamanho, tempos1,color="red", label="BubbleSort")
p.plot(tamanho, tempos2,color="green", label="SelectionSort")
p.plot(tamanho, tempos3,color="blue", label="InsertionSort")
p.plot(tamanho, tempos4,color="gray", label="QuickSort")
p.plot(tamanho, tempos5,color="brown", label="MergeSort")
p.plot(tamanho, tempos6,color="purple", label="ShellSort")
p.plot(tamanho, tempos7,color="black", label="CountingSort")
p.plot(tamanho, tempos8,color="yellow", label="RadixSort")
p.plot(tamanho, tempos9,color="orange", label="BucketSort")
p.show()
