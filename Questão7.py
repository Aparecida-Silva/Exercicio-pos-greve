'''
 Faça um programa que use a função valorPagamento para determinar o valor a ser
pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor
da prestação e o número de dias em atraso e passar estes valores para a função
valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa
que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a
execução o programa deverá voltar a pedir outro valor de prestação e assim continuar
até que seja informado um valor igual a zero para a prestação. Neste momento o
programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade
e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da
seguinte forma: Para pagamentos sem atraso, cobrar o valor da prestação. Quando
houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

#Variaveis 
TotalDIa = 0
contador = 0
verificação = 1
porcentagem1 = 0.1 / 100
porcentagem3 = 3 / 100

#Função para calcular a prestação
def ValorPagamento (ValorDaPrestação,atraso):
  #Com atraso
  if(ValorDaPrestação < 0):
    print("O Valor da prestação tem que ser positivo")
    
  else:
    #Com atraso
    if (atraso > 0):
      multa = ValorDaPrestação * porcentagem3
      JurosDia = atraso * (ValorDaPrestação * porcentagem1)
      Total = ValorDaPrestação + multa + JurosDia
    #Sem atraso
    
    else:
      Total = ValorDaPrestação
  return Total

#Progama
while (verificação > 0):
  ValorDaPrestação = eval(input("Digite o Valor da Prestação: "))
  atraso = eval(input("Digite quandos dias a prestação está de atraso: "))
  
  #Se o valor da prestação for negativa
  while (ValorDaPrestação < 0):
  
    print("O valor da prestação tem que ser positiva!")
    ValorDaPrestação = eval(input("Digite o Valor da Prestação: "))
    atraso = eval(input("Digite quandos dias a prestação está de atraso: "))
    
  print(ValorPagamento(ValorDaPrestação,atraso))
  
  #verificação e contador de prestações
  verificação = ValorPagamento(ValorDaPrestação,atraso)
  TotalDIa = TotalDIa + verificação
  contador = contador + 1
print("Relatório do dia\n Foram gastos R$",TotalDIa,"\n Foram pagas",contador - 1,"prestações")

