Vamos FAZER UM PROGRAMA QUE LEIA 10 NUMEROS REAIS E OS ARMAZENAR EM UMA LISTA.
CALCULE E MOSTRE: 
A QUANTIDADE DE NUMEROS NEGATIVOS 
A SOMA DOS NUMEROS POSITIVOS
"""

#criando vetor
numero = []
#crianado uma estrutura do tipo para que vai receber 5 elementos , se quisesse  recebesse mais elementos é so trocar dentro dos parentese  
for i in range(10):
    #estamos  chamando aqui o float antes de input pois nossos dados são tipo real 
    numerounitaria = float(input("Digite a nota do aluno: "))
    # o append esta incrementando o vetor atras  do final da lista, o que define a estrutura de dados do tipo lisa é isso aqui
    numero.append(numerounitaria)

quantidade_negativos = 0
soma_positivos = 0 
# para passar dentro de todos os itens do vetor usamos:

for numerounitaria in numero:
    if numerounitaria <0 :#verificando se é negativo
        quantidade_negativos += 1 # é a mesma coisa que quantidade_negativo = quantidade_negativos + 1 
    if numerounitaria > 0 : #verifique se é positivo 
        soma_positivos += numerounitaria# é a mesma coisa que soma_positivos = somapositivos + numerounitario



print(f"quantidade de numeros negativos: {quantidade_negativos}, e a soma dos positivos é :{soma_positivos}")



"""
UMA LISTA COM 10 VALORES E MOSTRA A POSIÇÃO  ONDE SE  ENCONTRA O MAIOR VALOR (SEM UTILIZAR FUNÇÕES PRONTAS)
numerosunitario
"""

numero =[]

for i in range(10):
   numerosunitario = float(input("digite um número"))
   numero.append(numerosunitario)

posicao = 0

for i in range(10):
    if numero[posicao]< numero[i]:
        posicao=i


print(f"A posição do maior número no vetor é: {posicao}")





"""
FAÇA UM PROGRAMA QUE VAI LER 5 NOTAS E ARMAZENAR EM UMA LISTA 
Imprimir media geral da turma
"""
#criando vetor
nota = []
#crianado uma estrutura do tipo para que vai receber 5 elementos , se quisesse  recebesse mais elementos é so trocar dentro dos parentese  
for i in range(5):
    #estamos  chamando aqui o float antes de input pois nossos dados são tipo real 
    notaunitaria = float(input("Digite a nota do aluno: "))
    # o append esta incrementando o vetor atras  do final da lista, o que define a estrutura de dados do tipo lisa é isso aqui
    nota.append(notaunitaria)
    
# criando a variavel media
media = 0 

#o item no vai ser quem vai passar em todos os itens do vetor, e vai colocalos dentro da media, que ira somando item por item ate finalizar  valor 
for no in nota: 
    media = media + no

media = media/5

print (f"media geral: {media}")

