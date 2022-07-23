X,Y = input().split()

X = float(X)
Y = float(Y)

if (X == 0) and (Y == 0):
    print("Origem")
elif (X > 0) and (Y == 0) or (X < 0) and (Y == 0):
    print("Eixo X")
elif (Y > 0) and (X == 0) or (Y < 0) and (X == 0):
    print("Eixo Y")
elif (X > 0) and (Y > 0):
    print("Q1")
elif (X < 0) and (Y < 0):
    print("Q3")
elif (X > 0) and (Y < 0):
    print("Q4")
elif (Y > 0) and (X < 0):
    print("Q2")
