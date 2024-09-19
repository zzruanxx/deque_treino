class Deque:
    def __init__(self):
        self.deque = []

    def esta_vazio(self):
        return len(self.deque) == 0
    
    def adicionar_frontal(self, item):
        self.deque.insert(0, item)

    def adicionar_retaguarda(self,item):
        self.deque.append(item)
    
    def remover_frontal(self):
        if self.esta_vazio():
            raise IndexError("Underflow")
        return self.deque.pop()
    
    def remover_retaguarda(self):
        if self.esta_vazio():
            raise IndexError("Deque esta vazio")
        return self.deque.pop()
    
    def tamanho(self):
        return len(self.deque)
    
    def pegar_frontal(self):
        if self.esta_vazio():
            raise IndexError("Deque esta vazio")
        return self.deque[0]
    
    def pegar_retaguarda(self):
        if self.esta_vazio():
            raise IndexError("Deque esta vazio")
        return self.deque[-1]
    
    deque = Deque()
    deque.adicionar_frontal(12)
    deque.adicionar_retaguarda(20)
    print(deque.remover_frontal())
    print(deque.remover_retaguarda())