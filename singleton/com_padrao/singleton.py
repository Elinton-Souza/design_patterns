# com_padrao/singleton.py


class ConexaoBancoDados:
    _instancia = None  # guarda a única instância criada

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            print("[Criando a conexão com o banco de dados...]")
            cls._instancia = ConexaoBancoDados()
        return cls._instancia

    def __init__(self):
        self.status = "Conectado ao Banco da Concessionária"


# Sempre usamos get_instancia() para garantir que só existe uma conexão
modulo_estoque = ConexaoBancoDados.get_instancia()
modulo_vendas = ConexaoBancoDados.get_instancia()

print(modulo_estoque is modulo_vendas)  # True — é a mesma instância!
print(modulo_estoque.status)
