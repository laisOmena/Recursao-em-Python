def hipotenusa(cateto1, cateto2):
   hip2 = (cateto1**2) + (cateto2**2)
   hip = hip2**(1/2)
   return hip
cateto1 = float(input("Digite um número: "))
cateto2 = float(input("Digite outro número: "))
a = hipotenusa(cateto1, cateto2)
print("A hipotenusa é {0:.2f}.".format(a))