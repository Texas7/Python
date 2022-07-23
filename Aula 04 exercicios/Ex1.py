x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))

z = 0

while x <= y :
    z += x
    x += 1

print("Resultado = {}".format(z))
