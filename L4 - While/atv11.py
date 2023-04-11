somadosalunosterceira = 0
maiorquantidadelivros = 0
totalalunos = 0
alunosnaogostamredacaoterceira = 0

while True:
    serie = int(input("Digite a série do aluno (1 a 4) ou 0 para sair: "))
    
    if serie == 0:
        break
    
    livros = int(input("Digite a quantidade de livros lidos por mês: "))
    redacao = int(input("Gosta de fazer redação? Digite 1 para sim ou 0 para não: "))
    
    if serie == 3:
        somadosalunosterceira += 1
        if redacao == 0:
            alunosnaogostamredacaoterceira += 1
        
    if serie == 4 and livros > maiorquantidadelivros:
        maiorquantidadelivros = livros
        
    total_alunos += 1

percentualnaogostamredacaoterceira = (alunosnaogostamredacaoterceira / somadosalunosterceira) * 100 if somadosalunosterceira != 0 else 0

print("a) Quantidade de alunos na terceira série: ", somadosalunosterceira)
print("b) Maior quantidade de livros lidos por um aluno na quarta série: ", maiorquantidadelivros)
print("c) Porcentagem de alunos que não gostam de fazer redação e estão na terceira série: ", percentualnaogostamredacaoterceira, "%")
