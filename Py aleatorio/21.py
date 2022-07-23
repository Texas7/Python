X = int(input())

anos = X / 365
resto = X % 365

mes = resto / 30
dias = resto % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(int(anos),int(mes),int(dias)))

