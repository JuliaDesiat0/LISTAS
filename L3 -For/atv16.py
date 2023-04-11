while True:
    numero = int(input("Digite um número inteiro positivo menor que 16 para calcular o fatorial (ou digite um número negativo para sair): "))

    if numero < 0:
        break
    elif numero >= 16:
        print("Número muito grande. Tente novamente.")
        continue

    fat = 1
    for i in range(1, numero+1):
        fat *= i

    print(f"O fatorial de {numero} é {fat}.")
