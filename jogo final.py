import time
print('''                                 John Shayny é um homem que trabalha em uma empresa de TI.
                     Sua mulher morreu a 5 anos atrás e sua filha desapareceu há 5 meses enquanto estava indo para a escola.
                     Depois de quatro meses de busca ele se convence de que nunca mais irá encontra-lá e se afoga no álcool.
                           Porém, depois de um mês de depressão, ele recebe uma ligação de sua filha pedindo socorro.
                                                 Ela diz que está na redondeza na cidade.
                                         Ele pede ajuda para a polícia e eles retomam as buscas.
      Porém, depois de um mês procurando, a polícia conclui que a história era uma invenção de John por conta da bebida e da depressão.
                            Depois da polícia abandonar o caso de novo, John não desiste de encontrar sua filha.
        ''')
time.sleep(10)
print("")

print('''
                                                                     INSTRUÇÕES
                                             Você irá ajudar John nessa busca. Controle suas ações e o ajude
                                                          a superar os obstáculos em frente. 
                                                                     Boa sorte
                                                                                                                              ''')
time.sleep(5)

print("")
print("")
print("")
print ("Agora John terá que escolher diferentes caminhos para encontrar sua filha")
saL1 = 1
saL2 = 1
saL3 = 1
saL4 = 1
saL5 = 1
com = 1
while com == 1:
    escolha1 = str(input('''\nEscolha aonde John irá procurar sua filha [outros armazéns da cidade][sua vizinhança][delegacia]
[desistir dessa merda e voltar pra casa]: '''))
    if escolha1=="sua vizinhança":
        print ("\nJohn continua a busca por sua filha pela vizinhança, escolha sua ação: ")
        escolha2 = str (input ("\n[conversar com vizinhos] [apenas observar se a casa de John está sendo vigiada]: "))  

        if escolha2=="conversar com vizinhos":   
            
            print ("\nJohn questiona seus vizinhos antigos sobre sua filha, alguns falam que não lembravam dela.")
            escolha1 = str(input('''\nEscolha o próximo lugar que John irá procurar sua filha [outros armazéns da cidade][sua vizinhança][delegacia]
            [desistir dessa merda e voltar pra casa]: '''))
        if escolha2=="apenas observar se a casa de John está sendo vigiada":
            print('''











                                           ' ---------------------------------- '
                                          '                                      '                                       
                                         '                                        '                                                                      
                                        '              |----------|                '                                          
                                       '               |    ||    |                 '                                           
                                      '                |    ||    |                  '                                             
                                     '                 |    ||    |                   '                         
                                    '                  |----------|                    '
                                   '                                                    '                                                    
                                  '                                                      ' 
                                  |------------------------------------------------------| 
                                  |                                                      |
                                  |                                                      |
                                  |                                                      |
                                  |                                                      |  
                                  |     |-------------|                                  |
                                  |     |             |                                  |
                                  |     |             |         |-----------------|      |
                                  |     |             |         |        |        |      |
                                  |     |             |         |        |        |      |
                                  |     |             |         |--------|--------|      |
                                  |     |           O |         |        |        |      | 
                                  |     |             |         |        |        |      |
                                  |     |             |         |-----------------|      |
                                  |     |             |                                  |
                                  |     |             |                                  | 
                                  |     |             |                                  |
------------------------------------------------------------------------------------------------------------------













                                                                                                                  ''')
                         

            time.sleep(7)
            print("Não tem nada suspeito")
            escolha1 = str(input('''\nEscolha o próximo lugar que John irá procurar sua filha [outros armazéns da cidade][sua vizinhança][delegacia]
            [desistir dessa merda e voltar pra casa]: '''))          
                           
    elif escolha1=="delegacia":
        print ("\nJohn vai até a delegacia perguntar sobre os lugares que eles procuraram.")
        print ("\nPorém, a polícia se recusa a dar qualquer informação. ")
        time.sleep(3)
        print ("\nEscolha outro caminho")
        escolha1 = str(input('''\nEscolha o próximo lugar que John irá procurar sua filha [outros armazéns da cidade][sua vizinhança][delegacia]
        [desistir dessa merda e voltar pra casa]: '''))

    elif escolha1 == "desistir dessa merda e voltar pra casa":
        
        print('''\nDepois de se convencer de que era só uma ilusão John decide voltar pra casa e volta a ser um alcoolatra depressivo,
                                            até morrer de ataque cardíaco aos 60 anos
                                                             FIM
                                                                                                        ''')
        com = com + 1
        saL1 = 2
        saL2 = 2
        saL3 = 2
        saL4 = 2
        saL5 = 2
    
    
    elif escolha1=="outros armazéns da cidade":
        
        print ("\nJohn procura por outros armazéns, porém em um dos armazéns que a policia procurou ele encontra uma abertura secreta ")
        escolha3 = str (input ("[entrar na abertura no chão] --> parece nao ter volta [sair do armazém]: "))  

        if escolha3=="sair do armazém":
            escolha1 = str(input('''\nEscolha o próximo lugar que John irá procurar sua filha [outros armazéns da cidade][sua vizinhança][delegacia]
[desistir dessa merda e voltar pra casa]: '''))

        if escolha3=="entrar na abertura no chão":
            print ("\nParece um lugar escondido que a policia não havia achado, e tem uma porta a frente. E por não haver uma escada nao tem como voltar.")
            com = com + 1


while saL1 != 2:
    print('''


SALA 01




                /-------------------------------\                                                    |
                |               |               |                                                    |
                |               |               |                                                    |
                |               |               |                                                    | 
                |               |               |         /-----\                                    | 
                |               |               |         | [ ] |                                    | 
                |            O  |  O            |         | *** |                                    |
                |               |               |         | *** |                                    |
                |               |               |         | *** |                                    | 
                |               |               |         \-----/                                    |
                |               |               |                                                    |
                |               |               |                                                    |       
                |               |               |                                                    |
    -------------------------------------------------------------------------------------------------
                                                                     ''')
    por = str(input("Digite aparelho se quiser ir colocar a senha: "))
    print("")
    print("")
    if por != "aparelho":
        print("Digite aparelho como foi solicitado. ")
    print("")    
    time.sleep(4)   
    while por == "aparelho":
            
        print('''

                                       
                                                             Tabela para você converter a letra encontrada em número:



          ---------------------                                       A = 1  | H = 8  | O = 15 | V = 22
         |                     |                                      B = 2  | I = 9  | P = 16 | W = 23
         |  [               ]  |                                      C = 3  | J = 10 | Q = 17 | X = 24
         |                     |                                      D = 4  | K = 11 | R = 18 | Y = 25 
         |  [ 1 ] [ 2 ] [ 3 ]  |                                      E = 5  | L = 12 | S = 19 | Z = 26
         |                     |                                      F = 6  | M = 13 | T = 20 |  
         |  [ 4 ] [ 5 ] [ 6 ]  |                                      G = 7  | N = 14 | U = 21 |
         |                     |
         |  [ 7 ] [ 8 ] [ 9 ]  |
         |                     |
         |  [ * ] [ 0 ] [ # ]  |
         |                     | 
         |  [ENTER]  [DELETE]  |
          ---------------------


''')
        print("Dica:É um tipo de computador que tem como função controlar as demais estações de trabalho quando ligados em uma rede de computadores")
        print("")
        print("Não esqueça de transformar a palavra obtida em número usando a tabela acima.")
        senha = int(input("Digite a senha: "))
        if senha != 1951822941518:
            print("Senha incorreta!")
        elif senha == 1951822941518:
            print("Senha correta!")
            por = "nada"
        print("")    
        time.sleep(3)    
        while senha == 1951822941518:
            print('''
  ------------------------------------------------------------------------
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                               O | O                               | 
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |  
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 | 
   |                                 |                                 |
   |                                 |                                 |
 -------------------------------------------------------------------------                          
                                                                             ''')
            gam = str(input("Digite girar para tentar abrir a porta: "))
            if gam == "girar":
                saL1 = saL1 + 1
                senha = senha + 1
                print("")                
                print("Proxima sala")
                print("")
                print("")
                time.sleep(5)
            else:
                print("Digite girar como foi solicitado!")
            


while saL2 != 2:
    print('''


SALA 02




                /-------------------------------\                                                    |
                |               |               |                                                    |
                |               |               |                                                    |
                |               |               |                                                    | 
                |               |               |         /-----\                                    | 
                |               |               |         | [ ] |                                    | 
                |            O  |  O            |         | *** |                                    |
                |               |               |         | *** |                                    |
                |               |               |         | *** |                                    | 
                |               |               |         \-----/                                    |
                |               |               |                                                    |
                |               |               |                                                    |       
                |               |               |                                                    |
    -------------------------------------------------------------------------------------------------
                                                                     ''')
    por = str(input("Digite aparelho se quiser ir colocar a senha: "))
    print("")
    print("")
    if por != "aparelho":
        print("Digite aparelho como foi solicitado. ")
    print("")    
    time.sleep(4)   
    while por == "aparelho":
            
        print('''

                                       
                                                             Tabela para você converter a letra encontrada em número:



          ---------------------                                       A = 1  | H = 8  | O = 15 | V = 22
         |                     |                                      B = 2  | I = 9  | P = 16 | W = 23
         |  [               ]  |                                      C = 3  | J = 10 | Q = 17 | X = 24
         |                     |                                      D = 4  | K = 11 | R = 18 | Y = 25 
         |  [ 1 ] [ 2 ] [ 3 ]  |                                      E = 5  | L = 12 | S = 19 | Z = 26
         |                     |                                      F = 6  | M = 13 | T = 20 |  
         |  [ 4 ] [ 5 ] [ 6 ]  |                                      G = 7  | N = 14 | U = 21 |
         |                     |
         |  [ 7 ] [ 8 ] [ 9 ]  |
         |                     |
         |  [ * ] [ 0 ] [ # ]  |
         |                     | 
         |  [ENTER]  [DELETE]  |
          ---------------------


''')
        print('''
            Dica:As partes físicas do microcomputador só funcionam de maneira lógica quando executam ordens contidas em um programa ou em um conjunto de programas.
              A parte composta pelos programas – que transforma as partes físicas do microcomputador em uma unidade lógica de processamento – é chamada de:
                                                                                    ''')
        print("")
        print("Não esqueça de transformar a palavra obtida em número usando a tabela acima.")
        senha = int(input("Digite a senha: "))
        if senha != 1915620231185:
            print("Senha incorreta!")
        elif senha == 1915620231185:
            print("Senha correta!")
            por = "nada"
        time.sleep(3)    
        while senha == 1915620231185:
            print('''
  ------------------------------------------------------------------------
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                               O | O                               | 
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |  
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 | 
   |                                 |                                 |
   |                                 |                                 |
 ---------------------------------------------------------------------------                          
                                                                             ''')
            gam = str(input("Digite girar para tentar abrir a porta: "))
            if gam == "girar":
                saL2 = saL2 + 1
                senha = senha + 1
                print("")                
                print("Proxima sala")
                print("")
                print("")
                time.sleep(5)
            else:
                print("Digite girar como foi solicitado!")



while saL3 != 2:
    print('''


SALA 03




                /-------------------------------\                                                    |
                |               |               |                                                    |
                |               |               |                                                    |
                |               |               |                                                    | 
                |               |               |         /-----\                                    | 
                |               |               |         | [ ] |                                    | 
                |            O  |  O            |         | *** |                                    |
                |               |               |         | *** |                                    |
                |               |               |         | *** |                                    | 
                |               |               |         \-----/                                    |
                |               |               |                                                    |
                |               |               |                                                    |       
                |               |               |                                                    |
    -------------------------------------------------------------------------------------------------
                                                                     ''')
    por = str(input("Digite aparelho se quiser ir colocar a senha: "))
    print("")
    print("")
    if por != "aparelho":
        print("Digite aparelho como foi solicitado. ")
    print("")
    time.sleep(4)   
    while por == "aparelho":
            
        print('''

                                       
                                                             Tabela para você converter a letra encontrada em número:



          ---------------------                                       A = 1  | H = 8  | O = 15 | V = 22
         |                     |                                      B = 2  | I = 9  | P = 16 | W = 23
         |  [               ]  |                                      C = 3  | J = 10 | Q = 17 | X = 24
         |                     |                                      D = 4  | K = 11 | R = 18 | Y = 25 
         |  [ 1 ] [ 2 ] [ 3 ]  |                                      E = 5  | L = 12 | S = 19 | Z = 26
         |                     |                                      F = 6  | M = 13 | T = 20 |  
         |  [ 4 ] [ 5 ] [ 6 ]  |                                      G = 7  | N = 14 | U = 21 |
         |                     |
         |  [ 7 ] [ 8 ] [ 9 ]  |
         |                     |
         |  [ * ] [ 0 ] [ # ]  |
         |                     | 
         |  [ENTER]  [DELETE]  |
          ---------------------


''')
        print('''
                Dica:São computadores usados em ambiente de rede para aumentar a produtividade dos usuários em uma empresa,
                              normalmente disponibilizados a esses funcionários dentro de um departamento.
                           Uma das características é o não uso de disco rígido. Refere-se a qual tecnologia?
            
                                                                                    ''')
        print("")
        print("Não esqueça de transformar a palavra obtida em número usando a tabela acima.")
        senha = int(input("Digite a senha: "))
        if senha != 208914312951420:
            print("Senha incorreta!")
        elif senha == 208914312951420:
            print("Senha correta!")
            por = "nada"
        print("")    
        time.sleep(3)    
        while senha == 208914312951420:
            print('''
  ------------------------------------------------------------------------
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                               O | O                               | 
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |  
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 | 
   |                                 |                                 |
   |                                 |                                 |
 --------------------------------------------------------------------------                          
                                                                             ''')
            gam = str(input("Digite girar para tentar abrir a porta: "))
            if gam == "girar":
                saL3 = saL3 + 1
                senha = senha + 1
                print("")                
                print("Proxima sala")
                print("")
                print("")
                time.sleep(5)
            else:
                print("Digite girar como foi solicitado!")


while saL4 != 2:
    print('''


SALA 04




                /-------------------------------\                                                    |
                |               |               |                                                    |
                |               |               |                                                    |
                |               |               |                                                    | 
                |               |               |         /-----\                                    | 
                |               |               |         | [ ] |                                    | 
                |            O  |  O            |         | *** |                                    |
                |               |               |         | *** |                                    |
                |               |               |         | *** |                                    | 
                |               |               |         \-----/                                    |
                |               |               |                                                    |
                |               |               |                                                    |       
                |               |               |                                                    |
    -------------------------------------------------------------------------------------------------
                                                                     ''')
    por = str(input("Digite aparelho se quiser ir colocar a senha: "))
    print("")
    print("")
    if por != "aparelho":
        print("Digite aparelho como foi solicitado. ")
    print("")    
    time.sleep(4)   
    while por == "aparelho":
            
        print('''

                                       
                                                             Tabela para você converter a letra encontrada em número:



          ---------------------                                       A = 1  | H = 8  | O = 15 | V = 22
         |                     |                                      B = 2  | I = 9  | P = 16 | W = 23
         |  [               ]  |                                      C = 3  | J = 10 | Q = 17 | X = 24
         |                     |                                      D = 4  | K = 11 | R = 18 | Y = 25 
         |  [ 1 ] [ 2 ] [ 3 ]  |                                      E = 5  | L = 12 | S = 19 | Z = 26
         |                     |                                      F = 6  | M = 13 | T = 20 |  
         |  [ 4 ] [ 5 ] [ 6 ]  |                                      G = 7  | N = 14 | U = 21 |
         |                     |
         |  [ 7 ] [ 8 ] [ 9 ]  |
         |                     |
         |  [ * ] [ 0 ] [ # ]  |
         |                     | 
         |  [ENTER]  [DELETE]  |
          ---------------------


''')
        print("Dica:Componentes físicos do seu computador são conhecidos como:")
            
        print("")
        print("Não esqueça de transformar a palavra obtida em número usando a tabela acima.")
        senha = int(input("Digite a senha: "))
        if senha != 81184231185:
            print("Senha incorreta!")
        elif senha == 81184231185:
            print("Senha correta!")
            por = "nada"
        print("")    
        time.sleep(3)
        while senha == 81184231185:
            print('''
  ------------------------------------------------------------------------
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                               O | O                               | 
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |  
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 | 
   |                                 |                                 |
   |                                 |                                 |
  ------------------------------------------------------------------------                         
                                                                             ''')
            gam = str(input("Digite girar para tentar abrir a porta: "))
            if gam == "girar":
                saL4 = saL4 + 1
                senha = senha + 1
                print("")                
                print("Proxima sala")
                print("")
                print("")
                time.sleep(5)
            else:
                print("Digite girar como foi solicitado!")
                


while saL5 != 2:
    print('''


SALA 05




                /-------------------------------\                                                    |
                |               |               |                                                    |
                |               |               |                                                    |
                |               |               |                                                    | 
                |               |               |         /-----\                                    | 
                |               |               |         | [ ] |                                    | 
                |            O  |  O            |         | *** |                                    |
                |               |               |         | *** |                                    |
                |               |               |         | *** |                                    | 
                |               |               |         \-----/                                    |
                |               |               |                                                    |
                |               |               |                                                    |       
                |               |               |                                                    |
    -------------------------------------------------------------------------------------------------
                                                                     ''')
    por = str(input("Digite aparelho se quiser ir colocar a senha: "))
    print("")
    print("")
    if por != "aparelho":
        print("Digite aparelho como foi solicitado. ")
    print("")
    time.sleep(4)   
    while por == "aparelho":
            
        print('''

                                       
                                                             Tabela para você converter a letra encontrada em número:



          ---------------------                                       A = 1  | H = 8  | O = 15 | V = 22
         |                     |                                      B = 2  | I = 9  | P = 16 | W = 23
         |  [               ]  |                                      C = 3  | J = 10 | Q = 17 | X = 24
         |                     |                                      D = 4  | K = 11 | R = 18 | Y = 25 
         |  [ 1 ] [ 2 ] [ 3 ]  |                                      E = 5  | L = 12 | S = 19 | Z = 26
         |                     |                                      F = 6  | M = 13 | T = 20 |  
         |  [ 4 ] [ 5 ] [ 6 ]  |                                      G = 7  | N = 14 | U = 21 |
         |                     |
         |  [ 7 ] [ 8 ] [ 9 ]  |
         |                     |
         |  [ * ] [ 0 ] [ # ]  |
         |                     | 
         |  [ENTER]  [DELETE]  |
          ---------------------


''')
        print("Dica: Qual a linguagem mais utilizada hoje em dia?")
            
                                                                                    
        print("")
        print("Não esqueça de transformar a palavra obtida em número usando a tabela acima.")
        senha = int(input("Digite a senha: "))
        if senha != 101221:
            print("Senha incorreta!")
        elif senha == 101221:
            print("Senha correta!")
            por = "nada"
        time.sleep(3)    
        while senha == 101221:
            print('''
  ------------------------------------------------------------------------
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                               O | O                               | 
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |  
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 |
   |                                 |                                 | 
   |                                 |                                 |
   |                                 |                                 |
 -------------------------------------------------------------------------                          
                                                                             ''')
            gam = str(input("Digite girar para tentar abrir a porta: "))
            if gam == "girar":
                saL5 = saL5 + 1
                senha = senha + 1
                print("Você saiu desta sala!")
                print("")
                print("")
                time.sleep(5)
                print('''
          Depois de ter passado por estas portas John acha uma garotinha, porém logo ele percebe que não é sua filha.
     Mesmo assim ele a pega e sai pela passagem que ele havia entrado. Depois ele vai imediatamente para a policia e eles vão
    ao local. Logo a policia conclui que se trata de uma organização criminosa que sequestra crianças para serem suas escravas.
Um policia que investiga o caso diz a John que provavelmente foram eles que levaram sua filha. E então John parte em busca de sua filha.

                                                         CONTINUA...
                                                                                               ''')


            else:
                print("Não foi solicitado essa palavra!")

                
            
