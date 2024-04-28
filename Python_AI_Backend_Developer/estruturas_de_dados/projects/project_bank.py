
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
        deposito = float(input("Digite o valor de deposito: "))

        if deposito > 0:
            SALDO_CONTA += deposito     
            ULTIMOS_DEPOSITOS.append(deposito)
        else:
            print("Voce só pode depositar valores positivos")

    elif opcao == "s": 
        if SAQUE_DIARIO <= 3 and SALDO_CONTA > 0:
            
            saque = float(int(input("Dite o valor a ser sacado: ")))
            
            if SALDO_CONTA > saque:
                SALDO_CONTA = SALDO_CONTA - saque
                SAQUE_DIARIO = SAQUE_DIARIO + 1
                ULTIMOS_SAQUES.append(saque)
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
        for x in ULTIMOS_DEPOSITOS:
            print(f"ultimo saques foram: {x}")
        print()
        print("-----------------------------")
        print()
        for x in ULTIMOS_SAQUES:
            print(f"ultimo saques foram: {x}")
            
    elif opcao == "q":
        break;     

    else:
        print("digite a operaçãao desejada")
            
        
print("programa finalizado!!")