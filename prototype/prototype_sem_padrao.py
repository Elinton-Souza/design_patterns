# sem_padrao/prototype.py


class CarroEstoque:
    def __init__(self, modelo, motor, cor, freio_abs, teto_solar):
        self.modelo = modelo
        self.motor = motor
        self.cor = cor
        self.freio_abs = freio_abs
        self.teto_solar = teto_solar
        print(f"[Processamento pesado: Validando engenharia do {modelo} nas diretrizes da fábrica...]")


# Problema: para criar 3 carros iguais no pátio, reprocessa toda a validação do zero
carro_1 = CarroEstoque("Sedan Conforto", "1.6", "Branco", True, False)
carro_2 = CarroEstoque("Sedan Conforto", "1.6", "Branco", True, False)
carro_3 = CarroEstoque("Sedan Conforto", "1.6", "Branco", True, False)
# "[Processamento pesado...]" é impresso 3 vezes — processo repetido desnecessariamente
