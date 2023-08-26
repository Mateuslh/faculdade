import numpy as np

class Pilha():
        def __init__(self,pValores,pCapacidade=None):
            if pCapacidade == None:
                self.capacidade = np.size(pValores)
            else:
                self.capacidade = pCapacidade
            self.topo = np.size(pValores)-1
            self.valores = pValores+([None]*(np.size(pValores)-self.capacidade))

        def pilhaCheia(self):
            return self.valores[self.capacidade-1] != None

        def pilhaVazia(self):
            return self.valores[0] == None

        def empilhar(self,valor):
            if valor == self.capacidade:
                print("[Erro]\nCapacidade da pilha ultrapassada.")
            else:
                index = self.topo+1
                self.valores[index] = valor
                self.topo = index

        def desempilhar(self):
            if not self.pilhaVazia():
                self.valores[self.topo] = None
                self.topo -= 1
            else:
                print("[Erro]\nNão é possivel retirar elementos de uma pilha vazia.")
        def verTopo(self):
            print(self.valores[self.topo])

        def valoresAnterioresIndex(self,index):
            valoresAnteriores = []
            for indexAcessado in range(index,-1,-1):
                valoresAnteriores.append(self.valores[indexAcessado])
            return valoresAnteriores


# Exercicio 1

exercicio1 = Pilha(list("mateus"),8)

for item in exercicio1.valores:
    if item is not None:
        exercicio1.desempilhar()

exercicio1.verTopo()

# Exercicio 5
# . Considere que temos três tipos de “abre parênteses”: “(”, “{” e “[”, e três tipos de “fecha parênteses”: “) ”, “}” e “] ”. Utilizando o conceito de pilhas, desenvolva um algoritmo que permita verificar se expressões com vários “abre” e “fecha parênteses” bem formadas. Considere que uma  expressão com parênteses é bem formada se um mesmo tipo de parênteses aberto é fechado corretamente após a sua ocorrência, mas sem que haja um outro parênteses aberto que não foi fechado entre eles.
# Por exemplo, as três expressões seguintes estão bem formadas:
# 	• ({[]})[(){}]
# 	• ({}([]))
# 	• {{}}(()()[[]])
# Por outro lado, as seguintes não estão:
# 	• ({)
# 	• }{
# 	• {{}())[[]])

exercicio5 = Pilha(list("({[]})[(){}]"))

print(exercicio5.valoresAnterioresIndex(2))

# Exercicio 1
# reposta
# t,4(desempilhar a posicao 5,4,3 e ler o valor do topo)


# Exercicio 2


