n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))

if (n1 > n2) and (n1 > n3) and (n2 > n3):
    print("{}, {}, {}".format(n1,n2,n3))
elif (n1 > n2) and (n1 > n3) and (n3 > n2):
    print("{}, {}, {}".format(n1,n3,n2))
elif (n2 > n1) and (n2 > n3) and (n1 > n3):
    print("{}, {}, {}".format(n2,n1,n3))
elif (n2 > n1) and (n2 > n3) and (n3 > n1):
    print("{}, {}, {}".format(n2,n3,n1))
elif (n3 > n1) and (n3 > n2) and (n2 > n1):
    print("{}, {}, {}".format(n3,n2,n1))
elif (n3 > n1) and (n3 > n2) and (n1 > n2):
    print("{}, {}, {}".format(n3,n1,n2))
