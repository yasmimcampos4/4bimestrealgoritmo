#VAMOS SIMULAR COM FUNCIONA O ALGORITMO DE UMA 
#IMPRESSORA QUE PODE RECEBER IMPRESSAO DE DIVERSOS 
#COMPUTADORES, VAMOS PENSAR EM UMA FILA.
class FilaDeImpressao:




    def configurar_inicial(self):
        self.fila=[]      
        
        
    def adicionar_trabalho(self,trabalho):
            self.fila.append(trabalho)
            print(f"Trabalho'{trabalho}' adicionado a fila de impressao")
            
    #remover o trabalh da lista
    def processar_trabalho(self):
        if not self.esta_vazia(): #verifica se a lista nao esta vazia
            trabalho = self.fila.pop(0) #remove o primeiro da fila
            print(f"o trabalho '{trabalho}'esta sendo processado") 
        else:
            print("a fila esta vazia!")
            
    #mostrar a fila de impressao
    def mostrar_fila(self):
        if self.esta_vazia():
            print("A fila esta vazia!") 
        else:
            print("Fila atual de impressao:")
            for trabalho in self.fila:
                print(f"-{trabalho}") #imprimir cada trabalho da lista       
            
    def esta_vazia(self):
        return len(self.fila) == 0
    #len verifica se o tamanho do vetor esta zerado       
                                                                                                                                                                
    #funçoes de interação com o usuario 
def menu():
    fila_impressao=FilaDeImpressao()
    #criando uma instancia para a classe
    fila_impressao.configurar_inicial()
        #configurar os atributos de entrada/inicial 
    while True:
    #opção para o nosso usuario
        print("Opções:")
        print("1 Adiciona um trabalho na fila da impressao")
        print("2. imprimir o proximo trabalho da fila")
        print("3. mostrar a fila de impressao")
        print("4. sair")
        escolha = input("escolha uma opcao 1-4")
        if escolha == "1":
            trabalho = input("Digite o nome do trabalho a ser impresso")
            fila_impressao.adicionar_trabalho(trabalho)
        elif escolha == "2":
            fila_impressao.processar_trabalho()
        elif escolha =="3":
            fila_impressao.mostrar_fila()
        elif escolha == "4":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida")  
            
menu() 
                                                                      