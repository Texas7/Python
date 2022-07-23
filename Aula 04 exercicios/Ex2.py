x = []
cont = 1

while cont <= 10 :
    x.append(int(input("Informe 10 notas: ")))
    cont += 1

z = sum(x) / 10

print("Média: {}".format(z))