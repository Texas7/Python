n1 = float(input("Digite a sua primeira nota de uma dada disciplina no semestre: "))
n2 = float(input("Digite a segunda nota da mesma: "))

nf = ((n1 + n2)/2)

if (nf >= 9.00) and (nf <= 10.00):
    print("A - Aprovado, sua média é de {}".format(nf))
elif (nf >= 7.50) and (nf < 9.00):
    print("B - Aprovado, sua média é de {}".format(nf))
elif (nf >= 6.00) and (nf < 7.50):
    print("C - Aprovado, sua média é de {}".format(nf))
elif (nf >= 4.00) and (nf < 6.00):
    print("D - Reprovado, sua média é de {}".format(nf))
elif (nf < 4.00) and (nf >= 0):
    print("E - Reprovado, sua média é de {}".format(nf))
