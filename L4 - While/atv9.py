votosbranco = 0
votosnulo = 0
votoskiko = 0
votoschaves = 0
votoschiquinha = 0

while True:
    voto = input("Digite o número do seu voto (ou 666 para encerrar a votação): ")
    
    if voto == "1":
        votosbranco += 1
    elif voto == "2":
        votosnulo += 1
    elif voto == "3":
        votoskiko += 1
    elif voto == "4":
        votoschaves += 1
    elif voto == "5":
        votoschiquinha += 1
    elif voto == "666":
        break
    else:
        print("Voto inválido. Digite novamente.")
        
print("Resultado da votação:")
print("Branco:", votosbranco)
print("Nulo:", votosnulo)
print("Kiko:", votoskiko)
print("Chaves:", votoschaves)
print("Chiquinha:", votoschiquinha)
