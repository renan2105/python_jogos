import adivinhacao
import forca

def escolher_jogo ():
    print("***************************")
    print("*****Escolha seu Jogo!*****")
    print("***************************")

    print("Jogos")
    print("(1)Adivinhação (2)Forca")

    jogo = int(input("Escolha o jogo:"))

    if jogo == 1:
        print("Jogando Advinhação")
        adivinhacao.jogar_advinhacao()
    elif jogo == 2:
        print("Jogando Forca")
        forca.jogar_forca()
    else:
        print("Jogo Invalido")
        exit()

    print("Fim de jogo o número secreto era ")


if __name__ == "__main__":
    escolher_jogo()