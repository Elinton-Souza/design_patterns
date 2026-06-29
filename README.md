# Padrões de Projeto — Padrões Criacionais (GoF)

> Trabalho da disciplina **Engenharia de Software II** — UniSenac   

---

## Grupo 1 — Turma Manhã

| Integrante      | Padrão responsável |
| --------------- | ------------------ |
| Elinton Souza   | Singleton          |
| Mateus Mariani  | Prototype          |
| Guilherme Dias  | Builder            |

---

## O que são Padrões de Projeto?

Padrões de projeto (design patterns) são **soluções reutilizáveis para problemas recorrentes** no design de software orientado a objetos. Eles não são trechos de código prontos, mas sim modelos — descrições ou templates — de como resolver um problema que pode ser aplicado em muitos contextos diferentes.

O catálogo mais famoso foi documentado por Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides no livro *Design Patterns: Elements of Reusable Object-Oriented Software* (1994), popularmente chamado de livro do **GoF (Gang of Four)**.

Os 23 padrões do GoF são divididos em três grandes categorias:

| Categoria           | Foco                                                  | Exemplos                                                        |
| ------------------- | ----------------------------------------------------- | --------------------------------------------------------------- |
| **Criacionais**     | Como os objetos são criados                           | Singleton, Factory Method, Abstract Factory, Builder, Prototype |
| **Estruturais**     | Como objetos e classes se compõem                     | Adapter, Decorator, Facade, Proxy, Composite                    |
| **Comportamentais** | Como objetos se comunicam e dividem responsabilidades | Observer, Strategy, Command, Iterator, State                    |

---

## Estrutura do Repositório

```
design_patterns/
├── .gitignore
├── README.md
├── singleton/
│   ├── sem_padrao/singleton.py
│   └── com_padrao/singleton.py
├── prototype/
│   ├── prototype_sem_padrao.py
│   └── prototype_padronizado.py
└── builder/
    ├── builder_sem_padrao.py
    └── builder_padronizado.py
```

---

## Padrões Criacionais

Os **padrões criacionais** abstraem o processo de instanciação de objetos. Eles ajudam a tornar o sistema independente de como seus objetos são criados, compostos e representados. Em vez de instanciar objetos diretamente com `new`, esses padrões fornecem mecanismos que aumentam a **flexibilidade** e o **reuso** do código existente.

### 🚗 O Cenário de Negócio: Sistema de Concessionária
    Para tornar este trabalho prático e integrado, o grupo aplicou os três padrões criacionais dentro do mesmo ecossistema: o sistema de gerenciamento de uma fábrica/concessionária de automóveis.
     
- O **Builder** será usado para montar veículos customizados passo a passo.
- O **Prototype** será usado para clonar em massa veículos de estoque que compartilham da mesma configuração de fábrica.
- O **Singleton** será usado para centralizar e garantir uma única conexão com a base de dados onde todos esses veículos são persistidos.

---

## 1. Singleton

> **Responsável:** Elinton Souza

### O que é?

O **Singleton** é um padrão de projeto criacional que garante que uma classe tenha **apenas uma instância** em toda a aplicação, fornecendo um ponto de acesso global a ela.

### Problema que resolve

No sistema da nossa concessionária, múltiplos módulos (vendas, estoque, customização) precisam salvar ou consultar dados no banco de dados central. Se cada classe ou consulta abrir uma nova conexão com o banco de dados separadamente, o sistema rapidamente sofrerá com lentidão, estouro do limite de conexões disponíveis e inconsistência de dados. O Singleton resolve isso garantindo que a classe gerenciadora de banco de dados possua uma única conexão ativa compartilhada por todo o software.

### Como funciona

1. A classe possui um atributo `_instancia` que começa como `None`.
2. O método `get_instancia()` verifica se já existe uma instância criada.
3. Se não existir, cria uma nova e a armazena. Se já existir, retorna a mesma.
4. Todo o código usa `get_instancia()` em vez de chamar `ConexaoBancoDados()` diretamente.

### Sem o padrão

```python

class ConexaoBancoDados:
    def __init__(self):
        self.status = "Conectado ao Banco da Concessionária"
        print("[Alerta: Uma NOVA conexão física com o banco foi aberta!]")

modulo_estoque = ConexaoBancoDados()
modulo_vendas = ConexaoBancoDados()

print(modulo_estoque is modulo_vendas)  # False — conexões duplicadas gastando recursos!
```

### Com o padrão

```python
# singleton/com_padrao/singleton.py

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
```

---

## 2. Prototype

> **Responsável:** Mateus Mariani

### O que é?

O **Prototype** é um padrão de projeto criacional que permite **copiar objetos existentes** sem tornar o código dependente de suas classes. Em vez de recriar um objeto complexo do zero, clonamos um molde pré-existente (o protótipo).

### Problema que resolve

A fábrica da concessionária produz lotes com centenas de carros idênticos (mesmo motor, mesma cor de fábrica, mesmo pacote de opcionais). Instanciar cada carro do zero, redefinindo manualmente todos os seus 50 atributos estruturais e carregando as configurações padrão repetidas vezes, gera desperdício de processamento e linhas de código repetitivas. O Prototype resolve isso definindo um "Carro Padrão de Linha" e clonando-o instantaneamente para gerar as unidades do estoque.

### Como funciona

1. A classe que representa o veículo fornece um método de clonagem (clone()).
2. O método cria uma cópia profunda de todos os atributos atuais do objeto
3. O sistema cria os novos registros do pátio a partir do clone do modelo base

### Sem o padrão

```python
# prototype/sem_padrao/prototype.py

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
```

### Com o padrão

```python
# prototype/com_padrao/prototype.py
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
```

---

## 3. Builder

> **Responsável:** Guilherme Dias

### O que é?

O **Builder** é um padrão de projeto criacional que permite **construir objetos complexos passo a passo**. Ele separa a lógica de montagem do objeto da sua representação final.

### Problema que resolve

Quando um cliente vai comprar um carro customizado sob encomenda, ele se depara com uma infinidade de opcionais: tipo de roda (liga leve, calota), tipo de banco (couro, tecido), presença de teto solar, kit multimídia, sensores de ré, etc. Se tentarmos criar uma classe Carro cujo construtor receba todos esses parâmetros opcionais de uma vez, teremos um método monstruoso ("construtor telescópico"), confuso, difícil de ler e altamente propenso a erros de posicionamento de variáveis. O Builder resolve isso criando o carro de forma fluida, peça por peça.

### Como funciona

1. A classe `Carro` possui os atributos com valores padrão, mas não recebe tudo no construtor.
2. A classe `CarroBuilder` tem métodos separados para definir motor, cor e adicionar cada opcional.
3. Cada método retorna o próprio builder (`return self`), permitindo chamadas encadeadas.
4. O método `build()` entrega o objeto `Carro` finalizado.

### Sem o padrão

```python
# builder/builder_sem_padrao.py

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

# Problema: é difícil saber o que cada True/False representa sem olhar a assinatura
carroEsportivo = Carro(motor="V8 Turbo", cor="Vermelho", tetoSolar=True, bancoCouro=True)
carroEsportivo.exibir_detalhes()

carroEconomico = Carro(motor="1.0 Flex", cor="Preto")
carroEconomico.exibir_detalhes()
```

### Com o padrão

```python
# builder/builder_padronizado.py

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
        return self.carro


# Montagem passo a passo: cada etapa é clara e legível
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
```

---

## ⚖️ Pontos Fortes e Fracos

### Singleton *(Elinton)*

| Pontos Fortes | Pontos Fracos |
| --- | --- |
| Garante um único ponto de acesso para um recurso compartilhado (ex: banco de dados) | Viola o Princípio da Responsabilidade Única |
| Economiza memória ao evitar instâncias duplicadas | Dificulta testes unitários (estado global) |
| Inicialização *lazy* (objeto criado só quando necessário) | Pode mascarar dependências ocultas no código |

### Prototype *(Mateus)*

| Pontos Fortes | Pontos Fracos |
| --- | --- |
| Clona objetos complexos sem acoplar o código às classes concretas | Referências circulares tornam a clonagem difícil |
| Elimina inicializações repetidas e configurações pesadas | Exige atenção na escolha entre *shallow copy* e *deep copy* |
| Facilita a criação de variações a partir de modelos pré-configurados | Subclasses precisam implementar obrigatoriamente o método `clone()` |

### Builder *(Guilherme)*

| Pontos Fortes | Pontos Fracos |
| --- | --- |
| Constrói objetos complexos passo a passo, em etapas bem definidas | Aumenta a complexidade com múltiplas classes novas |
| Elimina construtores telescópicos com dezenas de parâmetros confusos | Pode ser *overengineering* para objetos simples |
| Interface fluente melhora drasticamente a legibilidade do código | O cliente precisa conhecer os métodos de construção corretos |

---

## 📝 Conclusões do Grupo

Ao longo deste trabalho, o grupo estudou três padrões criacionais do GoF dentro de um mesmo contexto — um sistema de concessionária. Isso ajudou a enxergar como cada padrão resolve um problema específico, e como eles se complementam.

O **Singleton** foi o mais direto: uma única instância compartilhada faz sentido imediato em situações como conexões com banco de dados. A questão em Python é que não existe construtor privado como em Java — a solução é usar convenções como (`get_instancia()`) para garantir o uso correto.

O **Prototype** trouxe uma perspectiva diferente: em vez de construir do zero, você reutiliza um modelo já validado. O ponto crítico é entender a diferença entre shallow copy e deep copy. Usar a errada gera objetos que compartilham referências sem querer — e o erro aparece tarde.

O **Builder** foi o que mais impactou a legibilidade. Comparar um construtor com vários parâmetros booleanos com uma interface fluente deixa óbvio por que o padrão existe. A separação entre "o que construir" e "como construir" é uma das ideias mais úteis para projetos que crescem em complexidade.

A conclusão geral: padrões de projeto não são soluções universais. Cada um resolve um problema específico e pode ser desnecessário em contextos simples. O valor está em reconhecer quando o problema se encaixa no padrão — não em aplicá-lo por padrão em todo projeto.