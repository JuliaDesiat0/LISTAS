idade = int(input("Digite sua idade: "))

if idade >= 1 and idade <= 13:
    print("Você é uma criança.")
elif idade > 13 and idade <= 20:
    print("Você é um(a) adolescente.")
elif idade > 20 and idade <= 50:
    print("Você é um(a) adulto(a).")
else:
    print("Você é uma pessoa idosa.")