import math

catetoA = float(input("Digite o valor do cateto a: "))
catetoB = float(input("Digite o valor do cateto b: "))

hipotenusa = math.sqrt(catetoA**2 + catetoB**2)

print("Hipotenusa:", round(hipotenusa, 1))
