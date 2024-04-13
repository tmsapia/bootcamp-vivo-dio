# Sistema bancario
# Funções de deposito, saque e extrato

LIMITE_POR_SAQUE = 500
LIMITE_QTD_SAQUE_DIARIO = 3
saldo = 0.0
qtd_saques_realizados_dia = 0
extrato_saques = []
extrato_depositos = []



def deposita_valor(saldo, extrato_depositos):
    """Função para realizar o depósito no valor que o cliente deseja. O saldo é atualizado
    com o valor digitado e o valor do depósito é armazenado na lista de extrato de depósitos"""

    while True:

        valor_deposito = float(input ("Digite o valor que deseja depositar em sua conta: "))

        if valor_deposito <= 0:
            print("Digite um valor valido")
            continue

        else:
            saldo += valor_deposito
            extrato_depositos.insert(0,valor_deposito)
            print(f"Depósito de R$ {valor_deposito: .2f} realizado com sucesso")
            print(f"O seu saldo atual é de R$ {saldo: .2f}")
            return saldo
                       
def saca_valor(LIMITE_POR_SAQUE, LIMITE_QTD_SAQUE_DIARIO, saldo, qtd_saques_realizados_dia, extrato_saques):
    """Função para realizar o saque no valor que o cliente deseja. O saldo é atualizado
    após a retirada do valor da conta e o valor do saque é armazenado na lista de extrato de saques.
    São realizadas algumas verificações para garantir que o cliente pode realizar o saque antes da 
    operação ser executada"""

    while True:

        valor_saque = float(input("Digite o valor que deseja sacar de sua conta: "))
        
        if qtd_saques_realizados_dia >= LIMITE_QTD_SAQUE_DIARIO:
            print("Você ultrapassou a quantidade de saques diário")
            return saldo, qtd_saques_realizados_dia
            break

        elif valor_saque > LIMITE_POR_SAQUE:
            print (f"O limite máximo de saque é de R$ {LIMITE_POR_SAQUE}")
            continue
       
        elif valor_saque > saldo:
            print("Saldo insuficiente")
            continue
    
        elif valor_saque <= 0:
            print ("Digite um valor valido")
            continue
        
        else:
            saldo -= valor_saque
            extrato_saques.insert(0, valor_saque)
            qtd_saques_realizados_dia += 1
            print(f"Saque de R$ {valor_saque: .2f} realizado com sucesso")
            print(f"Seu saldo atual é de R$ {saldo: .2f}")
            return saldo, qtd_saques_realizados_dia

def exibir_extratos(extrato_depositos, extrato_saques, saldo):
    """Função para exibir os extratos de saques e depósitos realizados pelo cliente. Também é
    informado o saldo atual."""

    print ("\n ============= EXTRATO ============= \n")
    print("\n Saques: ")

    for saques in extrato_saques:
        print(f"R$ {saques: .2f}")


    print("\n Depósitos: ")

    for depositos in extrato_depositos:
        print(f"R$ {depositos: .2f}")

    print (f"\n Seu saldo atual é de R$ {saldo: .2f}\n")

    print("============================= \n")


while True:
    
    acao_usuario = input("""    
                                               
################# MENU #########################
                                              
                [d] Deposito  
                [s] Saque  
                [e] Extrato 
                [x] Sair
                         
 ###############################################       
                              
 Digite a ação desejada:  \n""")

    if acao_usuario == "d":
        saldo = deposita_valor(saldo, extrato_depositos)
        
        
    elif acao_usuario == "s":
        saldo, qtd_saques_realizados_dia = saca_valor(LIMITE_POR_SAQUE, LIMITE_QTD_SAQUE_DIARIO, saldo, qtd_saques_realizados_dia, extrato_saques)
        

    elif acao_usuario == "e":
        exibir_extratos(extrato_depositos, extrato_saques, saldo)
        

    elif acao_usuario == "x":
        print("Até breve!")
        break

    else: 
        print("Opção inválida. Por favor, escolha uma opção válida.")

