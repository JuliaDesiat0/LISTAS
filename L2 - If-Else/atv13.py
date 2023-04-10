idade = int(input("Digite a idade do trabalhador: "))
temposervico = int(input("Digite o tempo de serviço, em anos, do trabalhador: "))

if idade >= 65 or temposervico >= 30 or (idade >= 60 and temposervico >= 25):
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador não pode se aposentar ainda.")