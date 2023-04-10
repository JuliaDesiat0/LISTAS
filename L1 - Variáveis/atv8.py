import math

pi = math.pi

raio = float(input("Digite o raio do círculo: "))

circunferencia = 2 * pi * raio
area = pi * raio**2

print("Circunferência:", round(circunferencia, 2))
print("Área:", round(area, 2))
