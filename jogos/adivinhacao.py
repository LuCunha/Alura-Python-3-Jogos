import random

def jogar():

    print("***************")
    print("Bem vindo ao jogo de adivinhação")
    print("Você começara o jogo com 1000 pontos e a cada rodada que errar o numero, seus pontos vão caindo dependendo do nível que escolher.")
    print("Boa Sorte!!")
    print("***************")

    numero_secreto = 0
    total_de_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    print("Qual nível de dificuldade você gostaria de jogar?")
    print("(1) Fácil - Numero Secreto será de 0 à 10 e você terá 8 tentativas")
    print("(2) Médio - Numero Secreto será de 0 à 50 e você terá 5 tentativas ")
    print("(3) Difícil - Numero Secreto será de 0 à 100 e você terá 3 tentativas")

    nivel = int(input("Defina o Nível: "))

    if(nivel == 1):
        numero_secreto = random.randrange(0,11)
        total_de_tentativas = 8
        pontos_perdidos = 125
    elif(nivel == 2):
        numero_secreto = random.randrange(0,51)
        total_de_tentativas = 5
        pontos_perdidos = 200
    else:
        numero_secreto = random.randrange(0,101)
        total_de_tentativas = 3
        pontos_perdidos = 333

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}". format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu numero: "))
        print("Você digitou ", chute)

        if(numero_secreto == chute):
            print("Você acertou, seu total de pontos foi {}!!".format(pontos))
            break
        else:
            if(chute > numero_secreto):
                print("Você errou o numero que vc chutou é maior que o numero secreto")

            else:
                print("Você errou o  numero que você chutou é menor que o numero secreto")
            pontos = pontos - pontos_perdidos

if(__name__ =="__main__"):
    jogar()
