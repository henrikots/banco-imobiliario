import random

jogador1, jogador2, jogador3 = 300, 300, 300
dado_extra, dado_extra2,dado = 0,0,0
cont_casa_jog1, cont_casa_jog2, cont_casa_jog3 = 0,0,0
continuar = "s"
cont_vez = 0
nome_casa = " "
casa2, casa3, casa4, casa6, casa7, casa8, casa10, casa11, casa12, casa14, casa15, casa16 = 0,0,0,0,0,0,0,0,0,0,0,0
compra = 0
sorte_revez = 0
tot1, tot2, tot3 = 0,0,0
lugar = 0
soma = 0
proprietario, pagar = 0, 0
cash = 0

print("\n==================================================================\n")
# Escolha de modo de jogo, 2 ou 3 jogadores
escolha = int(input("Você deseja jogar com 2 ou 3 jogadores: [2] ou [3] "))
while escolha != 2 and escolha != 3:
    escolha = int(input("Dígito inválido, você deseja jogar com 2 ou 3 jogadores: [2] ou [3] "))

print(" ")
print("\n==================================================================\n")

# Ver ordem de ínicio da jogada
dado_extra = random.randint(1,6)
print("Jogador 1 rolou o dado:", dado_extra)
dado = random.randint(1,6)
while dado == dado_extra:
    dado = random.randint(1,6)
print("Jogador 2 rolou o dado: ", dado)
if escolha == 3:
    dado_extra2 = random.randint(1,6)
    while dado_extra2 == dado or dado_extra2 == dado_extra:
        dado_extra2 = random.randint(1,6)
    print("Jogador 3 rolou o dado: ", dado_extra2)
if dado_extra > dado and dado_extra > dado_extra2:
    print("Jogador 1 começa!!\n")
    cont_vez = 1
elif dado > dado_extra and dado > dado_extra2:
    print("Jogador 2 começa!!\n")
    cont_vez = 2
elif dado_extra2 > dado and dado_extra2 > dado_extra:
    print("Jogador 3 começa!!\n")
    cont_vez = 3


print("==================================================================\n")

#Laço de continuidade do Jogo
while jogador1 > 0 and jogador2 > 0 and jogador3 > 0 and continuar == "s":    

    #Verifica que casa o Jogador irá ficar após rolar o dado e adiciona na variável lugar
    dado = random.randint(1,6)
    print("Jogador", cont_vez,"rolou o dado: ", dado)
    if cont_vez == 1:
        cont_casa_jog1 += dado
        lugar = cont_casa_jog1
        cash = jogador1
    elif cont_vez == 2:
        cont_casa_jog2 += dado
        lugar = cont_casa_jog2
        cash = jogador2
    else:
        cont_casa_jog3 += dado
        lugar = cont_casa_jog3
        cash = jogador3

    #Verifica se o jogador atravessou todo o tabuleiro para receber seu bonus
    if cont_casa_jog1 > 16 or cont_casa_jog2 > 16 or cont_casa_jog3 > 16:
        print("\n-----------------------------------------------------------------\n")
        print("Você atravessou São Paulo, assim você ganhou 50 créditos.")
        if cont_vez == 1:
            jogador1 += 50
            cont_casa_jog1 -= 16
            lugar = cont_casa_jog1
        elif cont_vez == 2:
            jogador2 += 50
            cont_casa_jog2 -= 16
            lugar = cont_casa_jog2
        else:
            jogador3 += 50
            cont_casa_jog3 -= 16
            lugar = cont_casa_jog3
        #Quando o tabuleiro é atravessado o jogador tem a opção de continuar ou não o jogo   
        continuar = input("Deseja continuar o jogo: [S] ou [N]: ").lower()
        while continuar != "s" and continuar != "n":
            continuar = input("Comando invalido, deseja continuar o jogo: [S] ou [N]: ").lower()
        print("\n-----------------------------------------------------------------\n")
    #Apresenta a quantidade de créditos do Jogador da Rodada
    if cont_vez == 1:
        print("Você tem ", jogador1, " créditos")
    elif cont_vez == 2:
        print("Você tem ", jogador2, " créditos")
    else:
        print("Você tem ", jogador3, " créditos")

    print("\n-----------------------------------------------------------------\n")
    #Se o jogador decidir não continuar esse 'if' fara q o restante do código não não seja rodado
    if continuar == "n":
        print(" ")
    
    #Casa 1
    elif lugar == 1:
        nome_casa = "Início"
        print("Você está na Casa 1")

    #Casa 2 -----
    #Verifica se o jogador esta nessa casa
    elif lugar == 2:
        nome_casa = "Masp"
        print("Você está na Casa 2 - Masp")
        #Verifica se a casa possui dono, se não possuir o Jogador tem a opção de adquirir se seus créditos forem maior ou igual ao valor da casa
        if casa2 == 0:
            if cash >= 30:
                compra = input("Deseja comprar Masp por 30 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                   compra = input("Digito inválido, deseja comprar Masp por 30 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    #Se a propriedade for adquirida o valor dela é armazenada ao acumulador 'comprada' e registrado na casa o digito do seu dono
                    comprada = 30
                    casa2 = cont_vez
            else:
                #Se não possuir créditos suficientes essa mensagem aparecerá
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa2 != cont_vez:
            #Caso a casa possua dono a variavel 'soma' armazenará o valor da taxa que deverá ser pago ao proprietário e a variável 'proprietario' armazenara o digito do dono
            pagar = 1
            print("Você terá que pagar 9 créditos ao Jogador ", cont_vez)
            soma = 9
            proprietario = casa2
    #Todas as casas que não sejam Sorte ou Revéz(5, 9, 13) e de Início(1) seguirá o mesmo esquema descrito nos comentarios da #Casa 2

    #Casa 3
    elif lugar == 3:
        nome_casa = "Ibirapuera"
        print("Você está na Casa 3 - Ibirapuera")
        if casa3 == 0:
            if cash >= 30:
                compra = input("Deseja comprar Ibirapuera por 30 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Ibirapuera por 30 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 30
                    casa3 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa3 != cont_vez:
            pagar = 1
            print("Você terá que pagar 9 créditos ao Jogador ", casa3)
            soma = 9
            proprietario = casa3

    #Casa 4
    elif lugar == 4:
        nome_casa = "Villa Lobos"
        print("Você está na Casa 4 - Villa Lobos")
        if casa4 == 0:
            if cash >= 35:
                compra = input("Deseja comprar Villa Lobos por 35 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Villa Lobos por 35 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 35
                    casa4 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa4 != cont_vez:
            pagar = 1
            print("Você terá que pagar 11 créditos ao Jogador ", casa4)
            soma = 11
            proprietario = casa4

    #Casa 5 -----
    #Quando o Jogador está na casa Sorte ou Revéz a variável 'sorte_revez' armazenará um número aleatório servirá para mostrar qual será a ação que o Jogador receberá
    elif lugar == 5:
        nome_casa = "Sorte ou Revéz"
        print("Você está na Casa 5 - Sorte ou Revéz")
        sorte_revez = random.randint(1,10)
    #Todas as casas de Sorte ou Revéz(5, 9, 13) seguirá o mesmo esquema descrito nos comentários da #Casa 5
        

    #Casa 6
    elif lugar == 6:
        nome_casa = "Ponte Estaiada"
        print("Você está na Casa 6")
        if casa6 == 0:
            if cash >= 20:
                compra = input("Deseja comprar Ponte Estaiada por 20 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Ponte Estaiada por 20 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 20
                    casa6 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa6 != cont_vez:
            pagar = 1
            print("Você terá que pagar 6 créditos ao Jogador ", casa6)
            soma = 6
            proprietario = casa6
            

    #Casa 7
    elif lugar == 7:
        nome_casa = "Morumbi"
        print("Você está na Casa 7")
        if casa7 == 0:
            if cash >= 60:
                compra = input("Deseja comprar Morumbi por 60 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Morumbi por 60 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 60
                    casa7 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa7 != cont_vez:
            pagar = 1
            print("Você terá que pagar 18 créditos ao jogador ", casa7)
            soma = 18
            proprietario = casa7

    #Casa 8
    elif lugar == 8:
        nome_casa = "Mackenzie"
        print("Você está na Casa 8")
        if casa8 == 0:
            if cash >= 90:
                compra = input("Deseja comprar Mackenzie por 90 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Mackenzie por 90 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 90
                    casa8 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa8 != cont_vez:
            pagar = 1
            print("Você terá que pagar 27 créditos ao Jogador ", casa8)
            soma = 27
            proprietario = casa8

    #Casa 9
    elif cont_casa_jog3 == 9:
        nome_casa = "Sorte ou Revéz"
        print("Você está na Casa 9")
        sorte_revez = random.randint(1,10)

    #Casa 10
    elif lugar == 10:
        nome_casa = "Pacaembu"
        print("Você está na Casa 10")
        if casa10 == 0:
            if cash >= 40:
                compra = input("Deseja comprar Pacaembu por 40 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Pacaembu por 40 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 40
                    casa10 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa10 != cont_vez:
            pagar = 1
            print("Você terá que pagar 12 créditos ao Jogador ", cont_vez)
            soma = 12
            proprietario = casa10


    #Casa 11  
    elif lugar == 11:
        nome_casa = "Paulista"
        print("Você está na Casa 11")
        if casa11 == 0:
            if cash >= 70:
                compra = input("Deseja comprar Paulista por 70 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Paulista por 70 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 70
                    casa11 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa11 != cont_vez:
            pagar = 1
            print("Você terá que pagar 21 créditos ao Jogador ", casa11)
            soma = 21
            proprietario = casa11


    #Casa 12
    elif lugar == 12:
        nome_casa = "Augusta"
        print("Você está na Casa 12")
        if casa12 == 0:
            if cash >= 30:
                compra = input("Deseja comprar Augusta por 30 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Augusta por 30 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 30
                    casa12 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa12 != cont_vez:
            pagar = 1
            print("Você terá que pagar 9 créditos ao Jogador ", casa12)
            soma = 9
            proprietario = casa12

    #Casa 13
    elif lugar == 13:
        nome_casa = "Sorte ou Revéz"
        print("Você está na Casa 13")
        sorte_revez = random.randint(1,10)

    #Casa 14
    elif lugar == 14:
        nome_casa = "Vila Madalena"
        print("Você está na Casa 14")
        if casa14 == 0:
            if cash >= 60:
                compra = input("Deseja comprar Vila Madalena por 60 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Vila Madalena por 60 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 60
                    casa14 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa14 != cont_vez:
            pagar = 1
            print("Você terá que pagar 18 créditos ao Jogador ", casa14)
            soma = 18
            proprietario = casa14


    #Casa 15  
    elif lugar == 15:
        nome_casa = "Galeria do Rock"
        print("Você está na Casa 15")
        if casa15 == 0:
            if cash >= 20:
                compra = input("Deseja comprar Galeria do Rock por 20 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                   compra = input("Digito inválido, deseja comprar Galeria do Rock por 20 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 20
                    casa15 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa15 != cont_vez:
            pagar = 1
            print("Você terá que pagar 6 créditos ao Jogador ", casa15)
            soma = 6
            proprietario = casa15
        


    #Casa 16  
    elif lugar == 16:
        nome_casa = "Praça da Sé"
        print("Você está na Casa 16")
        if casa16 == 0:
            if cash >= 10:
                compra = input("Deseja comprar Praça da Sé por 10 créditos: [S] ou [N] ").lower()
                while compra != "s" and compra != "n":
                    compra = input("Digito inválido, deseja comprar Praça da Sé por 10 créditos: [S] ou [N] ").lower()
                if compra == "s":
                    comprada = 10
                    casa16 = cont_vez
            else:
                print("Você não tem créditos suficientes, trabalhe mais!")
        elif casa16 != cont_vez:
            pagar = 1
            print("Você terá que pagar 3 créditos ao jogador ", casa16)
            soma = 3
            proprietario = casa16

    #Se o Jogador durante a rodada cair na casa de Sorte ou Revéz aqui será verificado qual ação ele receberá e o valor do premio/multa será armazenado na variável 'soma'
    if lugar == 13 or lugar == 9 or lugar == 5:
        if sorte_revez==1:
            print("Você foi assaltado na Cracolandia, perca 15 créditos ")
            soma = -15
        elif sorte_revez==3:
            print("Ultrapassou o farol vermelho na consolação e foi multado, perca 20 créditos")
            soma = -20
        elif sorte_revez==5:
            print("Comeu um churrasco grelhado estragado na Republica e passou mal, vá ao hospital e perca 10 créditos")
            soma = -10
        elif sorte_revez==7:
            print("Perdeu a carteira em uma balada na Augusta, perca 25 créditos")
            soma = -25
        elif sorte_revez==9:
            print("Seu filho passou no Mackenzie,pague a faculdade!, perca 30 créditos")
            soma  = -30
        elif sorte_revez ==2:
            print("Foi no Roda Roda Jequiti! Receba 30 creditos")
            soma = 30
        elif sorte_revez ==4:
            print("Achou dolares na rua! Receba 25 creditos")
            soma = 25
        elif sorte_revez ==6:
            print("Ganhou na TeleSena! Receba 20 creditos")
            soma = 20
        elif sorte_revez ==8:
            print("Comprou um BigMac e recebeu troco errado! Receba 15 creditos")
            soma = 15
        elif sorte_revez ==10:
            print("Seu filho terminou a faculdade, não pagará mais a mensalidade! Receba 10 creditos")
            soma = 10
        #Pelo 'cont_vez' é identificado o jogador da rodada e o premio/multa adicionado ao seu total de créditos
        if cont_vez == 1:
            jogador1 += soma
        elif cont_vez == 2:
            jogador2 += soma
        else:
            jogador3 += soma

    print("\n-----------------------------------------------------------------\n")
    #Se na rodada o Jogador comprou uma propriedade, o valor a ser pago será descontado dos créditos do Jogador da rodada e o valor da propriedade armazenada em um contador individual
    if compra == "s":
        if cont_vez == 1:
            jogador1 -= comprada
            tot1 += comprada
        elif cont_vez == 2:
            jogador2 -= comprada
            tot2 += comprada
        else:
            jogador3 -= comprada
            tot3 += comprada
        print("Você comprou ", nome_casa)
    #Se na rodada o Jogador parou em uma casa que ja tenha dono, terá que pagar uma taxa e o Dono da propriedade recebera o valor da taxa
    elif pagar == 1:
        if cont_vez == 1:
            jogador1 -= soma
        elif cont_vez == 2:
            jogador2 -= soma
        else:
            jogador3 -= soma
            
        if proprietario == 1:
            jogador1 += soma
        elif proprietario == 2:
            jogador2 += soma
        else:
            jogador3 += soma

    somar = 0
    compra = " "
    pagar = 0
    print("Jogador ", cont_vez , "está na casa: ", nome_casa)

    print("")
    #São mostrados os valores de créditos de todos os jogadores
    print("Jogador1 tem", jogador1, "créditos")
    print("Jogador2 tem", jogador2, "créditos")
    if escolha == 3:
        print("Jogador3 tem", jogador3, "créditos")
    print("\n==================================================================\n")
    #Apos a finalização da rodada de um Jogador o 'cont_vez' passará para o numero do proximo Jogador a seguir a jogada
    cont_vez += 1
    if escolha == 3 and cont_vez > 3:
        cont_vez -= 3
    elif escolha == 2 and cont_vez > 2:
        cont_vez -= 2

print("\n Jogo Finalizado \n")
print("\n==================================================================\n")
#São somados o total de créditos e o valor total das propriedades compradas por cada jogador
jogador1 += tot1
jogador2 += tot2
jogador3 += tot3
#Aqui é mostrado o vencedor e, se houver, o empate
if escolha == 3:
    if jogador1 > jogador2 and jogador1 > jogador3:
        print("Parabéns, o jogador 1 conquistou a cidade de São Paulo com ", jogador1, " créditos.")
    elif jogador2 > jogador1 and jogador2 > jogador3:
        print("Parabéns, o jogador 2 conquistou a cidade de São Paulo com ", jogador2, " créditos.")
    elif jogador3 > jogador1 and jogador3 > jogador2:
        print("Parabéns, o jogador 3 conquistou a cidade de São Paulo com ", jogador3, " créditos.")
    else:
        print("O jogo terminou empatado, vão no Habbib's comemorar.")
else:
    if jogador1 > jogador2:
        print("Parabéns, o jogador 1 conquistou a cidade de São Paulo com ", jogador1, " créditos.")
    elif jogador2 > jogador1:
        print("Parabéns, o jogador 2 conquistou a cidade de São Paulo com ", jogador2, " créditos.")
    else:
        print("O jogo terminou empatado, vão no Habbib's comemorar.")
        
print("\n==================================================================\n")
