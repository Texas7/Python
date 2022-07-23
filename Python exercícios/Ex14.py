x1 = int(input("Digite o peso da quantidade de peixes adquirida: "))
multa = 0
excesso = 0

if (x1 > 50):
    x = x1 * 4
    z = 50 * 4
    multa = x - z
    excesso = x1 - 50

print("Peso total: {}kg\nExcesso: {}kg\nMulta: {} reais".format(x1, excesso, multa))
