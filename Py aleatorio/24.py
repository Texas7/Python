A,B,C = input().split()

A = float(A)
B = float(B)
C = float(C)

Delta = (((B**2))- (4*A)*C)
raiz =  pow(Delta, 0.5)
negative = B * -1

resto1 = int(A)

if (resto1 == 0) or (Delta < 0):
    
    print("Impossivel calcular")  
else:
    X1 = ((negative + raiz)/ (2*A))

    X2 = ((negative - raiz)/ (2*A))
    
    print("R1 = {:.5f}\nR2 = {:.5f}".format(X1,X2))

  
