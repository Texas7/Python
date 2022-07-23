h = float(input("Digite sua altura para calcularmos seu peso ideal: "))

man = (72.7*h)- 58
woman = (62.1*h)- 44.7

print("O peso ideal com base no corpo masculino é de {:.1f}kg e com base no corpo feminino é {:.1f}kg".format(man, woman))
