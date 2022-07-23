A,B,C,D = input().split()

A = float(A)
B = float(B)
C = float(C)
D = float(D)

peso_A = A * 2
peso_B = B * 3
peso_C = C * 4
peso_D = D * 1

media = float(peso_A + peso_B + peso_C + peso_D)/ 10

if (media >= 7):
    print(f"Media: {media:.1f}\nAluno aprovado.")
elif (media < 5):
    print(f"Media: {media:.1f}\nAluno reprovado.")
elif (media >= 5) and (media <= 6.9):
    E = float(input())
    media_final = (E + media)/2
    print(f"Media: {media:.1f}\nAluno em exame.\nNota do exame: {E:.1f}\nAluno aprovado.\nMedia final: {media_final:.1f}")

