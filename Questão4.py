'''
 Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N,
e mostre o resultado obtido.
'''

Num = int(input("Digite um número inteiro: "))
print("\n")
X = 0

for soma in range(1, Num + 1):
   X = X + soma
    
print("A soma de todos os números inteiros de 1 a", Num, "é igual a: ", X)
