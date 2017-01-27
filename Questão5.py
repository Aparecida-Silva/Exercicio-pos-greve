'''
 (Adaptado – Python Zumbi) Escreva um programa para calcular a redução de tempo
de vida de um fumante. Considere que para cada cigarro fumado por dia, durante o
tempo em anos que ele tem o hábito de fumar, ele perdeu 10 minutos de sua vida. Dessa
forma, exiba para o usuário o tempo de vida perdido com o hábito do fumo.
'''
#Perguntar a quantidade de cigarros fumados por dia
QuantCigarro = int(input("Digite quantos cigarros em média, você costuma fumar por dia: "))
#Perguntar há qaunto tempo (anos) fuma
anos = int(input("Digite há quanto tempo (anos), você tem o hábito de fumar: "))

Min = 0 

for x in range(1, QuantCigarro + 1):
  Min += 10 
TempoVidaPerdida = (anos * 365) * Min 
#Mostrar o tempo de vida perdido 
print("\n")
print("O seu tempo de vida perdido com o hábito do fumo, foi de", TempoVidaPerdida, "minutos!")
print("Que tal parar de fumar; e aumentar a sua expectativa de vida?")
