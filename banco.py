import os

class ContaBancaria:
    def __init__(self, nome_titular):
        self.titular = nome_titular
        self.saldo = 0.0
        self.tipo = "Corrente"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Erro: O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente! Seu saldo atual é de: R$ {self.saldo:.2f}")
        elif valor <= 0:
            print("Valor inválido! O saque deve ser maior que R$ 0,00")
        else:
            self.saldo -= valor
            print(f"O saque de R$ {valor:.2f} foi realizado com sucesso!")

    def ver_saldo(self):
        print(f"=> Titular: {self.titular} | Tipo: {self.tipo} | Saldo: R$ {self.saldo:.2f}")

class ContaPoupanca(ContaBancaria):
    def __init__(self, nome_titular, taxa_rendimento=0.005):
        super().__init__(nome_titular)
        self.taxa_rendimento = taxa_rendimento
        self.tipo = "Poupança"

    def render_juros(self):
        if self.saldo > 0:
            rendimento = self.saldo * self.taxa_rendimento
            self.saldo += rendimento
            print(f"Sua conta rendeu R$ {rendimento:.2f} de juros (Taxa de {self.taxa_rendimento * 100}%)!")
        else:
            print("A conta não possui saldo para render juros.")

def salvar_contas(lista_contas):
    print("\nSalvando todas as contas no arquivo...")
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "contas.txt")
    
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("=== Banco Python - Cadastro de Contas ===\n")
        
        # Percorre a lista de objetos do banco
        for conta in lista_contas:
            # Note o uso do ponto (.) para acessar os atributos do objeto
            arquivo.write(f"Tipo: {conta.tipo} | Titular: {conta.titular} | Saldo: {conta.saldo:.2f}\n")
            
    print("Sucesso! O arquivo 'contas.txt' foi atualizado.")

def carregar_contas():
    lista_contas = []
    
    # Descobre o caminho correto do ficheiro na mesma pasta do código
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "contas.txt")
    
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            
            # Percorre as linhas pulando a primeira (que é o cabeçalho)
            for linha in linhas[1:]:
                linha = linha.strip()
                if linha == "":
                    continue
                
                # Exemplo da linha: Tipo: Corrente | Titular: João | Saldo: 150.50
                partes = linha.split(" | ")
                tipo = partes[0].replace("Tipo: ", "")
                titular = partes[1].replace("Titular: ", "")
                saldo = float(partes[2].replace("Saldo: ", ""))
                
                # AQUI ESTÁ A MÁGICA DA POO:
                # Decidimos qual molde usar para recriar o objeto com base no tipo guardado
                if tipo == "Poupança":
                    nova_conta = ContaPoupanca(titular)
                else:
                    nova_conta = ContaBancaria(titular)
                
                # Devolvemos o saldo que estava guardado para o novo objeto
                nova_conta.saldo = saldo
                
                # Adicionamos o objeto reconstruído à lista do banco
                lista_contas.append(nova_conta)
                
        print("✅ Contas carregadas com sucesso do ficheiro!")
        
    except FileNotFoundError:
        # Se for a primeira vez que o programa corre, o ficheiro não existe
        print("ℹ️ Nenhum ficheiro de contas encontrado. A iniciar um banco vazio.")
        
    return lista_contas

# ==========================================
#     SISTEMA DE GERENCIAMENTO DO BANCO
# ==========================================

banco = carregar_contas() # Nossa lista que guardará todos os objetos de contas

while True:
    print("\n=== 🏦 BANCO PYTHON - MENU PRINCIPAL ===")
    print("1. Criar Conta Corrente")
    print("2. Criar Conta Poupança")
    print("3. Acessar uma Conta Existente")
    print("4. Listar Todas as Contas")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        nome = input("Digite o nome do titular da Conta Corrente: ")
        nova_conta = ContaBancaria(nome)
        banco.append(nova_conta)
        print(f"Conta Corrente de {nome} criada com sucesso!")
        
    elif opcao == '2':
        nome = input("Digite o nome do titular da Conta Poupança: ")
        nova_conta = ContaPoupanca(nome) # Cria objeto Conta Poupança
        banco.append(nova_conta)
        print(f"Conta Poupança de {nome} criada com sucesso!")
        
    elif opcao == '3':
        nome_busca = input("Digite o nome do titular para acessar a conta: ")
        conta_encontrada = None
        
        # Pesquisa o objeto da conta dentro da lista pelo nome do titular
        for conta in banco:
            if conta.titular.lower() == nome_busca.lower():
                conta_encontrada = conta
                break
                
        if conta_encontrada:
            # SUBMENU: Entramos dentro da conta específica do usuário
            while True:
                print(f"\n--- 👤 Operando Conta de: {conta_encontrada.titular} ({conta_encontrada.tipo}) ---")
                print("1. Ver Saldo")
                print("2. Depositar")
                print("3. Sacar")
                
                # A mágica do Python: se for poupança, mostra a opção de render juros!
                if conta_encontrada.tipo == "Poupança":
                    print("4. Render Juros")
                    
                print("5. Voltar ao Menu Principal")
                
                sub_opcao = input("Escolha uma operação: ")
                
                if sub_opcao == '1':
                    conta_encontrada.ver_saldo()
                    
                elif sub_opcao == '2':
                    valor_txt = input("Valor do depósito: R$ ")
                    try:
                        conta_encontrada.depositar(float(valor_txt))
                    except ValueError:
                        print("Erro: Digite um número válido.")
                        
                elif sub_opcao == '3':
                    valor_txt = input("Valor do saque: R$ ")
                    try:
                        conta_encontrada.sacar(float(valor_txt))
                    except ValueError:
                        print("Erro: Digite um número válido.")
                        
                elif sub_opcao == '4' and conta_encontrada.tipo == "Poupança":
                    conta_encontrada.render_juros()
                    
                elif sub_opcao == '5':
                    break
                else:
                    print("Opção inválida!")
        else:
            print("Conta não encontrada no nosso sistema!")
            
    elif opcao == '4':
        if len(banco) == 0:
            print("Nenhuma conta cadastrada no banco ainda.")
        else:
            print("\n=== RELATÓRIO GERAL DE CONTAS ===")
            for conta in banco:
                conta.ver_saldo()
                
    elif opcao == '5':
        salvar_contas(banco)
        print("Encerrando o sistema do Banco Python. Até mais!")
        break
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")