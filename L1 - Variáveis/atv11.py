import math

catetoa = float(input("Digite o valor do cateto a: "))
catetob = float(input("Digite o valor do cateto b: "))

hipotenusa = math.sqrt(catetoa**2 + catetob**2)

print("Hipotenusa:", round(hipotenusa, 1))
