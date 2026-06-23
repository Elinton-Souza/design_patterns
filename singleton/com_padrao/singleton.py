# com_padrao/singleton.py


class ConexaoBancoDados:
    """
    Singleton implementado via __new__.

    Ao sobrescrever __new__, garantimos que Python nunca crie um segundo
    objeto em memória — qualquer chamada a ConexaoBancoDados() retorna
    sempre a mesma instância, sem precisar de um método get_instancia().
    """

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("[Criando a ÚNICA conexão física com o banco de dados...]")
            cls._instancia = super().__new__(cls)
            cls._instancia.status = "Conectado ao Banco da Concessionária"
        return cls._instancia


# Módulos diferentes reutilizam a mesmíssima conexão
modulo_estoque = ConexaoBancoDados()
modulo_vendas = ConexaoBancoDados()

print(modulo_estoque is modulo_vendas)  # True — conexão única e centralizada!
print(modulo_estoque.status)            # Conectado ao Banco da Concessionária
