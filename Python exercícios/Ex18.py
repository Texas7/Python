x = float(input("Informe o tamnho da área em metros quadrados: "))

y = x / 6 #y é a quantidade em litros necessária

#Quantidade em metros que cada latão de tinta cobre: 18 * 6 = 108
#Quantidade em metros que cada galão de tinta cobre: 3.6 * 6 = 21.6

if (x % 108 == 0):
    qt1 = x / 108
else:
    qt1 = int((x / 108)+1) #Se a divião não for exata então acrescentará mais 1 latão

pt1 = qt1 * 80 #Preço dos Latões de tinta

if(x % 21.6 == 0):
    qt2 = x / 21.6
else:
    qt2 = int((x / 21.6)+1) #Se a divião não for exata então acrescentará mais 1 galão

pt2 = qt2 * 25 #Preço dos Latões de tinta

#Situação 3:
ml = int(y / 18.0)
mg = int((y - (ml * 18)) / 3.6)

if (y - (ml * 18)% 3.6 != 0):
    mg += 1

vl1 = ml * 80
vl2 = mg * 25
total = vl1 + vl2

print("Compras em latão: {} latas e valor total de: {} reais".format(qt1,pt1))
print("Compras em galão: {} galões e valor total de: {} reais".format(qt2,pt2))
print("Compra misturando, {} galões e {} latões. Total de {} reais".format(mg,ml,total))
