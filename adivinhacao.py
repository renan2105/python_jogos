import random


def jogar_advinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1)Facil (2)Médio (3)Dificil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    else:
        print("nivel invalido, deve ser 1, 2 ou 3")
        exit()

    # while total_de_tentativas >= rodada:
    for rodada in range(1, total_de_tentativas + 1):
        print("rodada {} de {}.".format(rodada, total_de_tentativas))

        chute = input("digite um numero entre 1 e 100: ")
        chute = int(chute)
        print("você digitou:", chute)

        if chute < 1 or chute > 100:
            print("você digitou um numero invalido!!!".upper())
            continue

        if chute == numero_secreto:
            print("Você Acertou, sua pontuação foi de {}".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if chute > numero_secreto:
                print("Você Errou: O seu chute foi maior que o número secreto")
            if chute < numero_secreto:
                print("Você Errou: O seu chute foi menor que o número secreto")
            # rodada = rodada + 1

    print("Fim de jogo o número secreto era {}".format(numero_secreto))


if __name__ == "__main__":
    jogar_advinhacao()