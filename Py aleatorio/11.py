A1,A2,A3 = input().split()
B1,B2,B3 = input().split()

A1 = int(A1)
A2 = int(A2)
A3 = float(A3)

B1 = int(B1)
B2 = int(B2)
B3 = float(B3)

Total = A2 * A3 + B2 * B3 

print("VALOR A PAGAR: R$ {:.2f}".format(Total))
