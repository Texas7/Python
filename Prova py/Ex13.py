l1 = int(input("Digite o valor do primeiro lado: "))
l2 = int(input("Digite o valor do segundo lado: "))
l3 = int(input("Digite o valor do terceiro lado: "))

if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1):
    print("Não forma um triângulo")
elif (l1 == l2) and (l1 == l3):
    print("Equilátero")
elif (l1 == l2) or (l1 == l3) or (l2 == l3):
    print("Isósceles")
else:
    print("Escaleno")