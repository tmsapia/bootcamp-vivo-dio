# sistema bancario
# deposito, saque e extrato

LIMITE_POR_SAQUE = 500
LIMITE_QTD_SAQUE_DIARIO = 3
saldo = 0.0
qtd_saques_realizados_dia = 0
extrato_saques = []
extrato_depositos = []



def deposita_valor(saldo, extrato_depositos):
    while True:
        valor_deposito = float(input ("Digite o valor que deseja depositar em sua conta: "))

        if valor_deposito <= 0:
            print("Digite um valor valido")
            continue

        else:
            saldo += valor_deposito
            extrato_depositos.append(valor_deposito)
            print(f"Depósito de R$ {valor_deposito: .2f} realizado com sucesso")
            print(f"O seu saldo atual é de R$ {saldo: .2f}")
            return saldo
            
                
def saca_valor(LIMITE_POR_SAQUE, LIMITE_QTD_SAQUE_DIARIO, saldo, qtd_saques_realizados_dia, extrato_saques):

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
            extrato_saques.append(valor_saque)
            qtd_saques_realizados_dia += 1
            print(f"Saque de R$ {valor_saque: .2f} realizado com sucesso")
            print(f"Seu saldo atual é de R$ {saldo: .2f}")
            return saldo, qtd_saques_realizados_dia

def exibir_extratos(extrato_depositos, extrato_saques):
    print("Extrato de Saques:", extrato_saques)
    print("Extrato de Depósitos:", extrato_depositos)


while True:
    
    acao_usuario = input(""" 
            Menu 
            [d] Deposito  
            [s] Saque  
            [e] Extrato 
            [x] Sair
            """)

    if acao_usuario == "d":
        saldo = deposita_valor(saldo, extrato_depositos)
        
        
    elif acao_usuario == "s":
        saldo, qtd_saques_realizados_dia = saca_valor(LIMITE_POR_SAQUE, LIMITE_QTD_SAQUE_DIARIO, saldo, qtd_saques_realizados_dia, extrato_saques)
        

    elif acao_usuario == "e":
        exibir_extratos(extrato_depositos, extrato_saques)
        

    elif acao_usuario == "x":
        break

    else: 
        print("Opção inválida. Por favor, escolha uma opção válida.")

