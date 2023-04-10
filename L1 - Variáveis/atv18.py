quantidade = int(input("Digite a quantidade de fitas da locadora: "))
valoraluguel = float(input("Digite o valor cobrado por aluguel: "))

#Faturamento anual
faturamento = quantidade * valoraluguel * 12 / 3
print("Faturamento anual: R${:.2f}".format(faturamento))

#Valor das multas por mês
multas = quantidade / 10 * valoraluguel * 0.1
print("Valor das multas por mês: R${:.2f}".format(multas))

#Total de fitas ao final do ano
totalfitas = quantidade + quantidade / 10 - quantidade * 0.02
print("Total de fitas ao final do ano: {:.2f}".format(totalfitas))
