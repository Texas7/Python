x = int(input("Quanto você ganha por hora ?: "))
y = int(input("Quantas horas você trabalha no mês?: "))

v1 = x * y #v1 Quantia ganha no mês (salário bruto)
v2 = v1 * 0.08 #v2 Imposto do INSS
v3 = v1 * 0.05 #v3 Imposto do Sindicato
v4 = v1 * 0.11 #v4 Imposto de Renda
vt = v2 + v3 + v4 #vt Total de imposto
v5 = (v1 -(v2 + v3 + v4)) #v5 Salário líquido
 
print("Salário bruto: {} reais\n Imposto do INSS: {} reais\n Imposto do sindicato: {} reais\n Imposto de renda: {} reais".format(v1,v2,v3,v4))
print("Total de impostos: {:.2f} reais\n Salário líquido: {} reais".format(vt,v5))
