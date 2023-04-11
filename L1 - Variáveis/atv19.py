numerodaconta = int(input("Digite o número da conta corrente (3 dígitos): "))

inverso = int(str(numerodaconta)[::-1])

soma = numerodaconta + inverso

digito_verificador = str(soma)[::-1][0]

print("Dígito verificador da conta:", digito_verificador)
