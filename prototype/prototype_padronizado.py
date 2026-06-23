# com_padrao/prototype.py
import copy


class CarroEstoque:
    def __init__(self, modelo, motor, cor, freio_abs, teto_solar):
        self.modelo = modelo
        self.motor = motor
        self.cor = cor
        self.freio_abs = freio_abs
        self.teto_solar = teto_solar
        print(f"[Processamento pesado: Validando engenharia do {modelo} nas diretrizes da fábrica...]")

    def clone(self):
        return copy.deepcopy(self)


# Registra o protótipo padrão de fábrica apenas uma vez
prototipo_sedan_branco = CarroEstoque("Sedan Conforto", "1.6", "Branco", True, False)

# Clona os modelos para o estoque instantaneamente, sem reprocessar as validações pesadas
carro_patio_1 = prototipo_sedan_branco.clone()
carro_patio_2 = prototipo_sedan_branco.clone()
carro_patio_3 = prototipo_sedan_branco.clone()

# Permite customizar variações pontuais sem afetar o protótipo original
carro_patio_3.cor = "Preto"

print(carro_patio_1.cor)  # Branco
print(carro_patio_3.cor)  # Preto
print(carro_patio_1 is carro_patio_2)  # False — cópias independentes
