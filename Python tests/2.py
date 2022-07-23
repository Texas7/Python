N = int(input("Digite um numero\n"))

c = 0
a = 0
b = 1

if (N <= -1):
    print("erro")
else:
  while N > 1:
      c = int(a + b)
      a = b
      b = c
      N -= 1
print(c)