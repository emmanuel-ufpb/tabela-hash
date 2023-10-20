from tabela_hash import TabelaHash

if __name__ == '__main__':
    tabela = TabelaHash()
    tabela.inserir(123, "valor123")
    print(tabela.recuperar(123))  # Deve imprimir "valor123"