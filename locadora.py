class Carro:
    def __init__(self, categoria, transmissao, combustivel, marca, modelo, ano, placa):
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def exibir_informacoes(self):
        print("Categoria:", self.categoria)
        print("Transmissão:", self.transmissao)
        print("Combustível:", self.combustivel)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Placa:", self.placa)


class Cliente:
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg


class Locadora:
    def __init__(self):
        self.carros_disponiveis = []
        self.clientes = []
        self.locacoes = []

    def cadastrar_carro(self):
        print("Cadastro de Carro")
        categoria = input("Informe a categoria: ")
        transmissao = input("Informe a transmissão: ")
        combustivel = input("Informe o tipo de combustível: ")
        marca = input("Informe a marca: ")
        modelo = input("Informe o modelo: ")
        ano = input("Informe o ano: ")
        placa = input("Informe a placa: ")

        carro = Carro(categoria, transmissao, combustivel, marca, modelo, ano, placa)
        self.carros_disponiveis.append(carro)

        print("Carro cadastrado com sucesso!")
        carro.exibir_informacoes()

    def cadastrar_cliente(self):
        print("Cadastro de Cliente")
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        rg = input("Informe o RG: ")

        cliente = Cliente(nome, cpf, rg)
        self.clientes.append(cliente)

        print("Cliente cadastrado com sucesso!")
        print("Nome:", cliente.nome)
        print("CPF:", cliente.cpf)
        print("RG:", cliente.rg)

    def realizar_locacao(self):
        if not self.carros_disponiveis:
            print("Não há carros disponíveis para locação.")
            return

        print("Locação de Carro")
        self.listar_carros_disponiveis()
        carro_numero = int(input("Escolha o número do carro a ser alugado: "))

        if carro_numero <= 0 or carro_numero > len(self.carros_disponiveis):
            print("Opção inválida.")
            return

        cliente_cpf = input("Informe o CPF do cliente: ")

        cliente = self.encontrar_cliente(cliente_cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return

        data_inicio = input("Informe a data de início da locação: ")
        data_fim = input("Informe a data de fim da locação: ")

        carro = self.carros_disponiveis[carro_numero - 1]
        self.carros_disponiveis.remove(carro)

        locacao = {
            "carro": carro,
            "cliente": cliente,
            "data_inicio": data_inicio,
            "data_fim": data_fim
        }
        self.locacoes.append(locacao)

        print("Locação realizada com sucesso!")
        print("Carro Alugado")
        carro.exibir_informacoes()
        print("Cliente")
        print("Nome:", cliente.nome)
        print("CPF:", cliente.cpf)
        print("RG:", cliente.rg)

    def listar_carros_disponiveis(self):
        print("Carros Disponíveis:")
        for i, carro in enumerate(self.carros_disponiveis, 1):
            print("Número:", i)
            carro.exibir_informacoes()

    def encontrar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def exibir_relatorio_locacoes(self):
        print("Relatório de Locações:")
        for locacao in self.locacoes:
            print("Carro Alugado")
            locacao["carro"].exibir_informacoes()
            print("Cliente")
            cliente = locacao["cliente"]
            print("Nome:", cliente.nome)
            print("CPF:", cliente.cpf)
            print("RG:", cliente.rg)
            print("Data de Início:", locacao["data_inicio"])
            print("Data de Fim:", locacao["data_fim"])

    def exibir_menu(self):
        while True:
            print("Bem-vindo a Locadora Boa Viagem, escolha uma das opções abaixo:")
            print("1) Cadastrar um Novo Veículo")
            print("2) Cadastrar um Novo Cliente")
            print("3) Realizar a locação de um Veículo")
            print("4) Relatório de locações")
            print("5) Sair")

            opcao = input("Escolha uma das opções: ")

            if opcao == "1":
                self.cadastrar_carro()
            elif opcao == "2":
                self.cadastrar_cliente()
            elif opcao == "3":
                self.realizar_locacao()
            elif opcao == "4":
                self.exibir_relatorio_locacoes()
            elif opcao == "5":
                print("Obrigado por utilizar a Locadora Boa Viagem!")
                break
            else:
                print("Opção inválida.")


locadora = Locadora()
locadora.exibir_menu()
