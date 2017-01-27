'''
 (Adaptado – Python Zumbi) Sabendo que a função str() transforma qualquer número
em string exiba quantos dígitos ele possui usando a função len().
'''

Num = int(input("Informe um número inteiro: "))
String = str(Num)
Len = len(String)

print("\n")
print("O número informado possui", Len, "dígito(s) ao todo!")
