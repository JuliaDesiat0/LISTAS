quantidade = int(input("Digite a quantidade de fitas da locadora: "))
valordoaluguel = float(input("Digite o valor cobrado por aluguel: "))

faturamento = quantidade * valordoaluguel * 12 / 3
print("Faturamento anual: R${:.2f}".format(faturamento))

multas = quantidade / 10 * valordoaluguel * 0.1
print("Valor das multas por mês: R${:.2f}".format(multas))

totalfitas = quantidade + quantidade / 10 - quantidade * 0.02
print("Total de fitas ao final do ano: {:.2f}".format(totalfitas))
