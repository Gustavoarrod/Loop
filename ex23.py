#Codigo e quantidade
print('''

      Código     Especificação     Preço
        1       Cachorro Quente    R$4.00
        2           X-Salada       R$4.50
        3           X-Bacon        R$5.00
        4       Torrada simples    R$2.00
        5         Refrigerante     R$1.50
        ''')

cod = int(input("Digite o código do item: "))

quant = int(input("Digite a quantidade do item: "))

tot = cod*quant

tot = round(tot,2)

print ("Total: R$ %.2f" % (tot)) 
