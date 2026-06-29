class Carro:
    def __init__(
        self,
        motor: str = "1.0",
        cor: str = "Prata",
        tetoSolar: bool = False,
        bancoCouro: bool = False
    ):
        self.motor = motor
        self.cor = cor
        self.tetoSolar = tetoSolar
        self.bancoCouro = bancoCouro

    def exibir_detalhes(self) -> None:
        print("--- Detalhes do Carro ---")
        print(f"Motor: {self.motor}")
        print(f"Cor: {self.cor}")
        print(f"Teto Solar: {'Sim' if self.tetoSolar else 'Não'}")
        print(f"Banco de Couro: {'Sim' if self.bancoCouro else 'Não'}")
        print("-------------------------\n")


carroEsportivo = Carro(
    motor="V8 Turbo",
    cor="Vermelho",
    tetoSolar=True,
    bancoCouro=True
)
carroEsportivo.exibir_detalhes()

carroEconomico = Carro(
    motor="1.0 Flex",
    cor="Preto"
)
carroEconomico.exibir_detalhes()
