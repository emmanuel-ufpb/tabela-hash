from lista_encadeada import ListaEncadeada

class TabelaHash:
    def __init__(self, n=100):
        self.tamanho = n
        self.baldes = [None] * 10

        for i in range(10):
            self.baldes[i] = [ListaEncadeada() for _ in range(n//10)]

    def funcao_hash1(self, chave):
        return chave % 10

    def funcao_hash2(self, chave):
        return chave // 10 % (self.tamanho // 10)

    def inserir(self, chave, valor):
        indice1 = self.funcao_hash1(chave)
        indice2 = self.funcao_hash2(chave)
        lista = self.baldes[indice1][indice2]
        lista.adicionar(chave, valor)

    def recuperar(self, chave):
        indice1 = self.funcao_hash1(chave)
        indice2 = self.funcao_hash2(chave)
        lista = self.baldes[indice1][indice2]
        return lista.obter(chave)
