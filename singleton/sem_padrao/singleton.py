class ConexaoBancoDados:
    def __init__(self):
        self.status = "Conectado ao Banco da Concessionária"
        print("[Alerta: Uma NOVA conexão física com o banco foi aberta!]")


modulo_estoque = ConexaoBancoDados()
modulo_vendas = ConexaoBancoDados()

print(modulo_estoque is modulo_vendas)
