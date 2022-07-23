X = int(input())

A1 = int(X/100)
A2 = X%100

B1 = int(A2/50)
B2 = A2%50

C1 = int(B2/20)
C2 = B2%20

D1 = int(C2/10)
D2 = C2%10

E1 = int(D2/5)
E2 = D2%5

F1 = int(E2/2)
F2 = int(E2%2)

print(f"{X}\n{A1} nota(s) de R$ 100,00\n{B1} nota(s) de R$ 50,00\n{C1} nota(s) de R$ 20,00\n{D1} nota(s) de R$ 10,00\n{E1} nota(s) de R$ 5,00\n{F1} nota(s) de R$ 2,00\n{F2} nota(s) de R$ 1,00")