import forca
import carta

def escolhe_jogo():
    print("*********************************")
    print("    Escolha seu jogo             ")
    print("*********************************")

    print("(1) Forca (2) carta")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando jogo d adivinhacao")
        carta.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()