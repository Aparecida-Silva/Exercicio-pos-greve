'''
Crie um programa para descobrir o custo total de um pedido de pizza, incluindo os
impostos sobre. Suponha que estamos pedindo uma ou mais pizzas do mesmo preço, e
que estamos fazendo o pedido da cidade de Campina Grande. Há um imposto sobre as
vendas que não está incluído no preço do cardápio, mas que será adicionado ao preço
final da compra. A taxa é de 8%, isso significa que é necessário adicionar esse percentual
ao valor final do pedido. Modele o programa da seguinte maneira:
a) Pergunte ao cliente quantas pizza ele irá pedir;
b) Pergunte o preço da pizza que está no cardápio;
c) Calcule o custo total das pizzas sem o imposto;
d) Calcule o valor do imposto;
e) Calcule o total cobrado da venda incluindo o imposto;
f) Mostre ao cliente o valor que será cobrado.
'''

print("*** Compra de Pizza ***")
print("\n")

QuantPizza = int(input("Quantas pizzas você deseja? "))
PreçoPizza = eval(input("Qual preço da pizza que está no cardápio? R$")) 
print("\n")

#custo total das pizzas sem o imposto
TSI = QuantPizza * PreçoPizza

#total cobrado da venda incluindo o imposto
imposto = 8/100 * TSI
TCI = TSI + imposto

print("O total é: R$", TCI)
