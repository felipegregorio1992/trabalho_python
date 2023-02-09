


lista=['pera','laranja','manga','pitanga','melao','melancia','pera','uva','jamelao','caqui','cacau'] #add nomes a lista de nomes

for corredois in range(len(lista)-1,0,-1):#corre a lista
    for a in range(corredois):#corre a lista
        if lista[a]>lista[a+1]:#ordena a lista teste se o valor da lista for maior que o proximo
            pegadois = lista[a]#pegar o valor da lista se for maior que o proximo
            lista[a] = lista[a+1]#troca o valor da lista se for maior que o proximo
            lista[a+1] = pegadois#joa ovalor maior na lista para direita

print(lista)