
mensagem = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

SAQUE_DIARIO = 0
SALDO_CONTA = 0 
ULTIMOS_SAQUES = []
ULTIMOS_DEPOSITOS = []

while True: 

    opcao = input(mensagem)
    
    if opcao == "d":
        deposito = int(input("Digite o valor de deposito: "))
        SALDO_CONTA = deposito + SALDO_CONTA    
        ULTIMOS_DEPOSITOS.append(deposito)

    elif opcao == "s": 
        if SAQUE_DIARIO <= 3 and SALDO_CONTA > 0:
            
            saque = int(int(input("Dite o valor a ser sacado: ")))
            
            if SALDO_CONTA > saque:
                SALDO_CONTA = SALDO_CONTA - saque
                SALDO_CONTA = SALDO_CONTA + 1
                ULTIMOS_DEPOSITOS.append(saque)
                print("Saque realizado")
            else:
                print("você não tem saldo")
        else:
            print("você n pode realizar saque")
    
    elif opcao == "e":
        print("--------EXTRATOO----------")
        print()
        print()
        print(f"Você tem em cconta nesse momento: {SALDO_CONTA}")
        print()
        print()
        print("Seus ultimos saques foram: ")
        print()
        for ultimo_saque in ULTIMOS_SAQUES:
            print(ultimo_saque)

    elif opcao == "q":
        break; 
            
        
print("programa finalizado!!")