A,B,C = input().split()

A = float(A)
B = float(B)
C = float(C)

if (A < B + C) and (B < A + C) and (C < A + B):
    Perimetro = A + B + C
    print(f"Perimetro = {Perimetro:.1f}")
else:
    Area = ((A + B)*C)/2
    print(f"Area = {Area:.1f}")
