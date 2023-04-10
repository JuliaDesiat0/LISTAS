a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if b == 0:
    print("Impossível dividir", a, "por zero!")
else:
    if a % b == 0:
        print("A é divisível por B")
    else:
        print("A não é divisível por B")