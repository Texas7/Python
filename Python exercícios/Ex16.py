x = int(input("Digite o valor do tamanho do arquivo em MB: "))
mbps = int(input("Digite o valor da velocidade do link da internet em Mbps: "))

valor1 = mbps / 8
valor2 = x / valor1
tempo = valor2 / 60
print("O tempo gasto será de aproximadamente: {:.2f} minutos ou {} segundos".format(tempo,valor2))
