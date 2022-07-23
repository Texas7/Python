m2 = float(input("Tamanho da area em metros quadrados: "))

if (m2 % 54 == 0):
    qt = m2/54
else:
        qt = int(m2/54)+ 1

pt = qt * 80
            
print("Você precisará de {} latas\n o preço total será de {} reais".format(qt,pt))
