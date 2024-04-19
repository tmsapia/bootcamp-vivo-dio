# Sistema bancario otimizado
# Criação de duas novas features para cadastrar usuário e cadastrar conta bancária e realização de melhorias nas funções já existentes

def depositar_valor(saldo, extrato, valor_deposito):
    """Função para realizar o depósito no valor que o cliente deseja. O saldo é atualizado
    com o valor digitado e o valor do depósito é armazenado na lista de extrato"""

    if valor_deposito <= 0:
        return saldo, False, "Valor do depósito inválido"

    saldo += valor_deposito
    nova_entrada_extrato = f"Depósito: R$ {valor_deposito: .2f}"
    extrato_atualizado = [nova_entrada_extrato] + extrato
    mensagem = f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso. Saldo atual: R$ {saldo:.2f}"
    return saldo, extrato_atualizado, True, mensagem
                       
def sacar_valor(*, valor_saque, LIMITE_POR_SAQUE, LIMITE_QTD_SAQUE_DIARIO, saldo, qtd_saques_realizados_dia, extrato):
    """Função para realizar o saque no valor que o cliente deseja. O saldo é atualizado
    após a retirada do valor da conta e o valor do saque é armazenado na lista de extrato de saques.
    São realizadas algumas verificações para garantir que o cliente pode realizar o saque antes da 
    operação ser executada"""

    if qtd_saques_realizados_dia >= LIMITE_QTD_SAQUE_DIARIO:
        mensagem = "Você ultrapassou a quantidade de saques diário"
        return saldo, qtd_saques_realizados_dia, extrato, False, mensagem
        
    elif valor_saque > LIMITE_POR_SAQUE:
        mensagem = f"O limite máximo de saque é de R$ {LIMITE_POR_SAQUE}"
        return saldo, qtd_saques_realizados_dia, extrato, False, mensagem
    
    elif valor_saque > saldo:
        mensagem = "Saldo insuficiente"
        return saldo, qtd_saques_realizados_dia, extrato, False, mensagem        

    elif valor_saque <= 0:
        mensagem = "Digite um valor valido"
        return saldo, qtd_saques_realizados_dia, extrato, False, mensagem        
          
    else:
        saldo -= valor_saque
        nova_entrada_extrato = f"Saque: R$ {valor_saque: .2f}"
        extrato_atualizado = [nova_entrada_extrato] + extrato
        qtd_saques_realizados_dia += 1
        mensagem = f"Saque de R$ {valor_saque: .2f} realizado com sucesso. Seu saldo atual é de R$ {saldo: .2f}"
        return saldo, qtd_saques_realizados_dia, extrato_atualizado, True, mensagem

def exibir_extratos(saldo,*,extrato):
    """Função para exibir os extratos de saques e depósitos realizados pelo cliente. Também é
    informado o saldo atual."""

    extrato_str = "\n============= EXTRATO ===============\n"
    for operacao in extrato:
        extrato_str += operacao + "\n"
    extrato_str += f"\nSeu saldo atual é de R$ {saldo:.2f}\n"
    extrato_str += "======================================== \n"
    return extrato_str

def cadastrar_usuario(usuarios, cpf, nome, data_nascimento, endereco):
    """Realiza cadastro do usuário recebendo as informações de CPF, nome, data de nascimento e endereço"""
    
    if validar_cpf(cpf) == False or verificar_se_cpf_existe_na_lista_de_cliente(usuarios, cpf) == True:
        return usuarios, False, "CPF inválido ou já existente."
        
    novo_usuario = dict(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco) 
    lista_atualizada_usuarios = [novo_usuario] + usuarios
    return lista_atualizada_usuarios, True, "Cadastro realizado com sucesso!"  
        
def validar_cpf(cpf):
    """ Valida se o CPF tem 11 digitos e se tem somente números"""
    if len(cpf) == 11 and cpf.isdigit():
        return True
    return False

def verificar_se_cpf_existe_na_lista_de_cliente(usuarios, cpf):
    """Verifica se o CPF já existe na lista de clientes cadastrados."""
    return any(usuario["cpf"] == cpf for usuario in usuarios)

def criar_conta(AGENCIA, usuarios, numero_conta, cpf, contas_corrente):
    """Realiza a criação de uma conta recebendo como entrada o CPF do usuário"""

    if verificar_se_cpf_existe_na_lista_de_cliente(usuarios, cpf) == True:
        usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
        numero_conta += 1
        nova_conta_corrente = dict(cpf=usuario["cpf"], nome=usuario["nome"], agencia=AGENCIA, numero_conta=numero_conta)
        lista_atualizada_conta_corrente = [nova_conta_corrente] + contas_corrente
        mensagem = f"Conta criada com sucesso\n CPF: {usuario['cpf']}, Nome: {usuario['nome']}, Agência: {AGENCIA}, Conta Corrente: {numero_conta}\n"
        return numero_conta, lista_atualizada_conta_corrente, True, mensagem 
    
    return numero_conta, contas_corrente, False, "Esse cliente não existe."
   

def listar_usuarios(usuarios):
    usuarios_str = "\n============= USUÁRIOS ===============\n"
    for usuario in usuarios:
        usuarios_str += str(usuario) + "\n"
    usuarios_str += "======================================== \n"
    return usuarios_str

def listar_contas(contas_corrente):
    contas_str = "\n============= CONTAS ===============\n"
    for conta in contas_corrente:
        contas_str += f"""
        Agência: {conta["agencia"]}
        C/C: {conta["numero_conta"]}
        Nome: {conta["nome"]}
        CPF: {conta["cpf"]}
        =================================\n"""
    return contas_str


def menu():
    acao_usuario = input("""                                                   
===================== MENU ======================
                                              
                [d] Deposito  
                [s] Saque  
                [e] Extrato 
                [nu] Novo usuário 
                [nc] Nova conta 
                [lu] Lista usuarios
                [lc] Lista contas
                [x] Sair                    
 ================================================       
                              
 Digite a ação desejada:  """)
    return acao_usuario

def main():

    #constantes
    LIMITE_POR_SAQUE = 500
    LIMITE_QTD_SAQUE_DIARIO = 3
    AGENCIA = "0001"

    saldo = 0
    qtd_saques_realizados_dia = 0
    extrato = []
    usuarios =[]
    contas_corrente = []
    numero_conta = 0

    #Executa funções
    while True:

        acao_usuario = menu()
        
        #Deposito
        if acao_usuario == "d":
            valor_deposito = float(input("Digite o valor que deseja depositar em sua conta: "))
            saldo, extrato, retorno, mensagem = depositar_valor(saldo, extrato, valor_deposito)
            print(mensagem)

        #Saque  
        elif acao_usuario == "s":
            valor_saque = float(input("Digite o valor que deseja sacar de sua conta: "))
            saldo, qtd_saques_realizados_dia, extrato, retorno, mensagem = sacar_valor(valor_saque=valor_saque, LIMITE_POR_SAQUE=LIMITE_POR_SAQUE, LIMITE_QTD_SAQUE_DIARIO=LIMITE_QTD_SAQUE_DIARIO, saldo=saldo, qtd_saques_realizados_dia=qtd_saques_realizados_dia, extrato=extrato)
            print(mensagem)

        #Extrato
        elif acao_usuario == "e":
            extrato_str = exibir_extratos(saldo, extrato=extrato)
            print (extrato_str)
        
        #Cadastra usuário
        elif acao_usuario == "nu":
            cpf = input("CPF: ")
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento [dd/mm/aaaa]: ")
            endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ")
            usuarios, retorno, mensagem = cadastrar_usuario(usuarios, cpf, nome, data_nascimento, endereco)
            print(mensagem)

        #Cria conta
        elif acao_usuario == "nc":
            cpf = input("Digite seu CPF: ")
            numero_conta, contas_corrente, retorno, mensagem  = criar_conta(AGENCIA, usuarios, numero_conta, cpf, contas_corrente)
            print(mensagem)

        #Lista conta
        elif acao_usuario == "lc":
            contas_str = listar_contas(contas_corrente)
            print(contas_str)

        #Lista usuário
        elif acao_usuario == "lu":
            usuarios_str = listar_usuarios(usuarios)
            print(usuarios_str)  

        #Sair do sistema
        elif acao_usuario == "x":
            print("Até breve!")
            break

        else: 
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()