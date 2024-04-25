
mensagem = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

SAQUE_DIARIO = 0
SALDO_CONTA = 0 



while True: 

    opcao = input(mensagem)
    
    if opcao == "d":
        deposito = int(input("Digite o valor de deposito: "))
        SALDO_CONTA = deposito + SALDO_CONTA
    
    if opcao == "s": 
        if SAQUE_DIARIO <= 3 and SALDO_CONTA > 0:
            
            saque = int(int(input("Dite o valor a ser sacado: ")))
            
            if SALDO_CONTA > saque:
                print("Vo")
            
            
        
