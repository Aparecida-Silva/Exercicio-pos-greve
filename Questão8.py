#Variaveis 
ListaB = ""
verificador = 1

#Lista A só de enfeite
ListaA = []

#Progama
while(verificador == 1):
   
#Pedir nome do usuario
   nome=str(input("Digite o nome:"))
# Adicionando o nome na lista A(ListaA)    
   ListaA.append(nome)
   
#COntador de palavras no nome
   palavras = len(nome.split())
   
#Organização do nome
   for n in range(0,palavras):
       #Adicionando o nome iinvertido na lista(ListaB)
       ListaB = ListaB + nome.split()[palavras -1]
       palavras = palavras - 1
       if (palavras == 0):
           ListaB = ListaB + ";"
       else:
           ListaB = ListaB + ","
   verificador = int(input("Digite 1 se quiser adicionar mais algum nome, ou 2 para sair e ver o resultado:"))
print("(b)",ListaB)
