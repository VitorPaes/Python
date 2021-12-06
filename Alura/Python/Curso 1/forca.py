
def jogar():
    print("*********************************")
    print("    Bem vindo ao jogo da forc    ")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False


    #enquanto True and True
    while(not enforcou and not acertou ):
        chute = input("Qual letra?  ")
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Econtrei a letra {} na posicao {}".format(letra,index))
            index = index + 1
        print("jogando")
    	
    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()