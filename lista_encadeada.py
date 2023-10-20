class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, chave, valor):
        novo_no = No(chave, valor)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def obter(self, chave):
        atual = self.cabeca
        while atual:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None