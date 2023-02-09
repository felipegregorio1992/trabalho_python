import random


lista=[]
for i in range(0,100):
    lista.append(i)#adiciona 100 numeros na lista

lista = random.sample(lista, 100)#embaralha a lista
print(lista)
for corre in range(len(lista)-1,0,-1):#corre a lista
    for a in range(corre):#corr a lista
        if lista[a]<lista[a+1]:#ordena a lista teste se o valor da lista for menor que o proximo
            pega = lista[a]#pegar o valor da lista se for menor que o proximo
            lista[a] = lista[a+1]#troca o valor da lista se for menor que o proximo
            lista[a+1] = pega#joa ovalor menor na lista para direita

print(lista)

