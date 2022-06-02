def negativo(pixels, intensidade):
    for item in pixels:
        negativo = [ intensidade - item ]
    return negativo



imagem = open("image.pgm", "r")
tipo = imagem.readline()
lixo = imagem.readline()
tamanho = imagem.readline().split()
#tamanho[0] = linhas  /// tamanho[1] = colunas
intensidade = imagem.readline()
intensidade = int(intensidade)

i=0
pixels=[]
for line in imagem:
    for num in line.split():
        pixels.append(int(num))



saida = open("saida.pgm", "w")
saida.write(tipo)
saida.write("#SPIGA\n")
saida.write(tamanho[0] + " " + tamanho[1]+"\n")
saida.write(str(intensidade))


aux = negativo(pixels, intensidade)

#escrita dos valores
for item in pixels:
    saida.write(str(item) + " ")