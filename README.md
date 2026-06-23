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
│   ├── sem_padrao/prototype.py
│   └── com_padrao/prototype.py
└── builder/
    ├── sem_padrao/builder.py
    └── com_padrao/builder.py
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
# singleton/sem_padrao/singleton.py

class ConexaoBancoDados:
    def __init__(self):
        self.status = "Conectado ao Banco da Concessionária"
        print("[Alerta: Uma NOVA conexão física com o banco foi aberta!]")

# Problema: cada operação abre uma conexão nova desnecessariamente
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

1. A classe do produto final (CarroCustomizado) possui os atributos, mas não os define de uma vez.
2. A classe CarroBuilder cria os métodos modulares para adicionar cada opcional individualmente.
3. O processo retorna o próprio construtor (return self) permitindo chamadas encadeadas.
4. O método final build() entrega o veículo configurado para a produção.


### Sem o padrão

```python
# builder/sem_padrao/builder.py

class CarroCustomizado:
    def __init__(self, modelo, motor, cor, banco_couro=False, teto_solar=False,
                 multimidia=False, blindado=False):
        self.modelo = modelo
        self.motor = motor
        self.cor = cor
        self.banco_couro = banco_couro
        self.teto_solar = teto_solar
        self.multimidia = multimidia
        self.blindado = blindado

# Problema: parâmetros booleanos posicionais confusos — o que cada True/False significa?
encomenda_cliente_a = CarroCustomizado("SUV Premium", "2.0 T", "Cinza", True, False, True, False)
encomenda_cliente_b = CarroCustomizado("Hatch Pop", "1.0", "Preto", False, False, False, False)
```

### Com o padrão

```python
# builder/com_padrao/builder.py

class CarroCustomizado:
    def __init__(self):
        self.modelo = None
        self.motor = None
        self.cor = None
        self.banco_couro = False
        self.teto_solar = False
        self.multimidia = False
        self.blindado = False

    def __str__(self):
        opcionais = [
            "Banco de Couro" if self.banco_couro else None,
            "Teto Solar" if self.teto_solar else None,
            "Kit Multimídia" if self.multimidia else None,
            "Blindagem" if self.blindado else None,
        ]
        itens = [i for i in opcionais if i]
        return (f"{self.modelo} {self.motor} ({self.cor}) -> "
                f"Opcionais: {', '.join(itens) if itens else 'Nenhum'}")


class CarroBuilder:
    def __init__(self):
        self._carro = CarroCustomizado()

    def definir_base(self, modelo, motor, cor):
        self._carro.modelo = modelo
        self._carro.motor = motor
        self._carro.cor = cor
        return self

    def adicionar_banco_couro(self):
        self._carro.banco_couro = True
        return self

    def adicionar_teto_solar(self):
        self._carro.teto_solar = True
        return self

    def adicionar_multimidia(self):
        self._carro.multimidia = True
        return self

    def adicionar_blindagem(self):
        self._carro.blindado = True
        return self

    def build(self):
        return self._carro


# Montagem passo a passo: legível, fluente e sem ambiguidades
pedido_premium = (CarroBuilder()
                  .definir_base("SUV Premium", "2.0 T", "Cinza")
                  .adicionar_banco_couro()
                  .adicionar_multimidia()
                  .build())

pedido_executivo = (CarroBuilder()
                    .definir_base("Sedan Executivo", "2.5", "Preto")
                    .adicionar_banco_couro()
                    .adicionar_teto_solar()
                    .adicionar_blindagem()
                    .build())

print(pedido_premium)    # SUV Premium 2.0 T (Cinza) -> Opcionais: Banco de Couro, Kit Multimídia
print(pedido_executivo)  # Sedan Executivo 2.5 (Preto) -> Opcionais: Banco de Couro, Teto Solar, Blindagem
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