# sem_padrao/singleton.py


class ConexaoBancoDados:
    def __init__(self):
        self.status = "Conectado ao Banco da Concessionária"
        print("[Alerta: Uma NOVA conexão física com o banco foi aberta!]")


# Problema: cada operação abre uma conexão nova desnecessariamente
modulo_estoque = ConexaoBancoDados()
modulo_vendas = ConexaoBancoDados()

print(modulo_estoque is modulo_vendas)  # False — conexões duplicadas gastando recursos!
