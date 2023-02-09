

modelo_carro=[['camaro',10],['fusca',15],['gol',20],['palio',10],['uno',12],['civic',13],['corolla',14],['ferrari',12],['mustang',11]] #add a lista de nomes e km
print('numero  modelo_carro')
for i in range(len(modelo_carro)):
    print(i,'-',modelo_carro[i][0])#printa a lista de nomes

modelo = int(input('digite o numero do modelo do carro: '))#pega o numero do modelo do carro
litros = int(input('digite a quantidade de litros: '))#pega a quantidade de litros
km = modelo_carro[modelo][1]#pega o valor do km
resultado = km * litros#multiplica o km pelo litros
print('o carro percorreu',resultado,'km')#printa o resultado