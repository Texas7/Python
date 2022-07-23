X, Y = input().split()

X = int(X)
Y = int(Y)

item_p = [0, 4, 4.5, 5, 2, 1.5]

preco = float(item_p[X] * Y) 

print("Total: R$ {:.2f}".format(preco))
