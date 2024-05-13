texto = input("digite um palavra: ")
VOGAIS = "AEIOU"


for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")    
else:
    print()
    print("executado")

print()

#range é uma sequencia de numero
for numero in range(0,11):
    print(numero, end="")

#tabuada do 5
for numero in range(0, 52, 5):
    print(numero, end="")

#estrutura while 
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)
