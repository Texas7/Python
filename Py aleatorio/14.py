A,B,C = input().split()

A = int(A)
B = int(B)
C = int(C)

MaiorAB = (A + B + abs(A - B))/2

if (MaiorAB > C):
    Maior = MaiorAB
else:
    Maior = C

print("{:.0f} eh o maior".format(Maior))