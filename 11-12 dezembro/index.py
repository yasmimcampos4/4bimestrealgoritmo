1
"""#criando um vetor
notas= []

#criando a variável média
media = 0

for i in range (5):
    notaUnitaria = float(input("digite a nota"))
    notas.append(notaUnitaria)
    #O append incrementa o valor 

#o item no vai ser quem irá passar por todos os itens do vetor, e vai colocar dentro da media que irá somando item por item até finalizar o valor do item
for nota in notas:
    media = media+nota

media = media/5

print(media)
"""
2
"""numeros =[]

for i in range(10):
    numUnitario = float(input("digite o numero"))
    numeros.append(numUnitario)

qtNeg = 0
somaPos = 0
for numUnitario in numeros:
    if numUnitario < 0:
        qtNeg += 1
    if numUnitario > 0:
        somaPos+= numUnitario

print(f'A soma dos positivos é: {somaPos} e a quantidade de negativos é: {qtNeg}')"""

3
"""
numeros =[]

for i in range(10):
    numUnitario = float(input("digite um número"))
    numeros.append(numUnitario)

posicao = 0

for i in range(10):
    if numeros[posicao]< numeros[i]:
        posicao=i


print(f"A posição do maior número no vetor é: {posicao}")
"""
