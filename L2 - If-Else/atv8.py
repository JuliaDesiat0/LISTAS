I = int(input("Digite sua idade: "))

if I >= 1 and I <= 13:
    print("Você é uma criança.")
elif I > 13 and I <= 20:
    print("Você é um(a) adolescente.")
elif I > 20 and I <= 50:
    print("Você é um(a) adulto(a).")
else:
    print("Você é uma pessoa idosa.")
