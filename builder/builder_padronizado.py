# Com padrão/builder

class Carro:
    def __init__(self):
        self.motor: str = "1.0"
        self.cor: str = "Prata"
        self.tetoSolar: bool = False
        self.bancoCouro: bool = False

    def exibir_detalhes(self) -> None:
        print("--- Detalhes do Carro ---")
        print(f"Motor: {self.motor}")
        print(f"Cor: {self.cor}")
        print(f"Teto Solar: {'Sim' if self.tetoSolar else 'Não'}")
        print(f"Banco de Couro: {'Sim' if self.bancoCouro else 'Não'}")
        print("-------------------------\n")


class CarroBuilder:
    def __init__(self):
        self.carro = Carro()

    def set_motor(self, motor: str) -> 'CarroBuilder':
        self.carro.motor = motor
        return self 

    def set_cor(self, cor: str) -> 'CarroBuilder':
        self.carro.cor = cor
        return self

    def tetoSolar(self) -> 'CarroBuilder':
        self.carro.tetoSolar = True
        return self

    def bancoCouro(self) -> 'CarroBuilder':
        self.carro.bancoCouro = True
        return self

    def build(self) -> Carro:
        carroPronto = self.carro
        return carroPronto

carroEsportivo = (
    CarroBuilder()
    .set_motor("V8 Turbo")
    .set_cor("Vermelho")
    .tetoSolar()
    .bancoCouro()
    .build()
)
carroEsportivo.exibir_detalhes()

carroEconomico = (
    CarroBuilder()
    .set_motor("1.0 Flex")
    .set_cor("Preto")
    .build()
)
carroEconomico.exibir_detalhes()