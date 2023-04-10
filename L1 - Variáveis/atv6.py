salariominimo = float(input("Digite o valor do salário mínimo: "))
quilowatts = int(input("Digite a quantidade de quilowatts gasta pela residência: "))

valorquilowatt = salariominimo / 700
valortotal = valorquilowatt * quilowatts
valorcomdesconto = valortotal * 0.9

print(f"Valor do quilowatt: R${valorquilowatt:.2f}")
print(f"Valor a ser pago: R${valortotal:.2f}")
print(f"Valor com desconto: R${valorcomdesconto:.2f}")

