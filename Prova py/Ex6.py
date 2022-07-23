n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))

if (n1 > n2) and (n1 > n3):
    print("O {} é o primeiro listado e maior número".format(n1))
elif (n2 > n1) and (n2 > n3):
    print("O {} é o segundo listado e maior número".format(n2))
elif (n3 > n1) and (n3 > n2):
    print("O {} é o terceiro listado e maior número".format(n3))
