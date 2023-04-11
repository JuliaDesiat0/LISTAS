#ler o número da conta
numeroconta = int(input("Digite o número da conta corrente (3 dígitos): "))

#inverso do número
inverso = int(str(numeroconta)[::-1])

#somar o número com o inverso
soma = numeroconta + inverso

#calcular o dígito verificador
digito_verificador = str(soma)[::-1][0]

#resultado
print("Dígito verificador da conta:", digito_verificador)
