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


prototipo_sedan_branco = CarroEstoque("Sedan Conforto", "1.6", "Branco", True, False)

carro_patio_1 = prototipo_sedan_branco.clone()
carro_patio_2 = prototipo_sedan_branco.clone()
carro_patio_3 = prototipo_sedan_branco.clone()

carro_patio_3.cor = "Preto"

print(carro_patio_1.cor)
print(carro_patio_3.cor)
print(carro_patio_1 is carro_patio_2)
