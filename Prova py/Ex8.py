pc1 = float(input("Digite o preço do primeiro produto: "))
pc2 = float(input("Digite o preço do segundo produto: "))
pc3 = float(input("Digite o preço do terceiro produto: "))

if (pc1 < pc2) and (pc1 < pc3):
    print("O {} é o primeiro listado e mais barato".format(pc1))
elif (pc2 < pc1) and (pc2 < pc3):
    print("O {} é o segundo listado e mais barato".format(pc2))
elif (pc3 < pc1) and (pc3 < pc1):
    print("O {} é o terceiro listado e mais barato".format(pc3))