A,B,C,D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

SOMACD = C + D
SOMAAB = A + B
parimpar = A % 2


if (B > C) and (D > A) and (SOMACD > SOMAAB) and (C > 0) and (D > 0) and (parimpar == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")