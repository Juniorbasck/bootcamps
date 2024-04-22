MAIOR_IDADE = 18 
IDADE_ESPECIAL = 16

idade = int(input("informa a idade: "))

if idade >= MAIOR_IDADE:
    print("pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("pode tirar a CNH")
else:
    print("não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("pode fazer aulas praticas")
else :
    print("não pode tirar a CNH")


# if ternario:
# Exemplo: 
# status = "Sucesso" if saldo >= saque else "Falha"