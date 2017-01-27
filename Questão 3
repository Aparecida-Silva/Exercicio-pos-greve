'''
Escreva um programa que receba dois valores inteiros declarados por base e
expoente, e realize a operação de exponenciação da seguinte forma baseexponente.
a) Exemplo: Base = 2; Expoente = 3  2
3 = 2 x 2 x 2 = 8.
'''

base = int(input("Digite um número para a base da potenciação: "))
expoente = int(input("Digite um número para o expoente da potenciação: "))
potencia = 1
contador = 1
if (expoente >= 0):
    while(contador <= expoente):
        potencia = potencia * base
        contador = contador + 1

elif(expoente < 0):
    expoente = expoente * -1
    while(contador <= expoente):
        potencia = potencia * 1 / base
        contador = contador + 1
        
print("\n")
print(base, "elevado a", expoente, "é igual a: ", potencia)
