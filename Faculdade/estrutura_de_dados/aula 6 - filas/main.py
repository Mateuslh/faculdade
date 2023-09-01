from numpy import size


class fila():
    def __init__(self, arrayElementos, capacidade):
        if (capacidade < size(arrayElementos)):
            raise Exception("Capacidade não suporta fila instanciada.")
        self.__elements = arrayElementos
        self.__inicio = 0
        self.__isChanged = True
        self.capacidade = capacidade

    def isFull(self):
        if not self.__isChanged and size(self.__elements) < self.capacidade:
            return False
        elementosValidos = 0
        for elemento in self.__elements:
            if elemento is not None:
                elementosValidos += 1
        if self.__isChanged and elementosValidos < self.capacidade:
            return False
        return True

    def inserir(self, elementToInserted):
        if self.isFull():
            raise Exception("Fila possui todas as posições preenchidas.")
        if not self.__isChanged:
            for index,elementOfFor in enumerate(self.__elements):
                if elementOfFor is None:
                    self.__elements[index] = elementToInserted
                    return self.__elements
            self.__elements[size(self.__elements)] = elementToInserted
            return self.__elements

filaObj = fila([1,4,2,None,5],5)

print(filaObj.inserir(1))



