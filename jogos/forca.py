def jogar():
    print("***************")
    print("Bem vindo ao jogo da forca")
    print("***************")

    palavra_secreta = "banana"
    letras_acertadas= ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        print("Jogando...")
        chute = input("Digite uma letra:")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra

            posicao = posicao + 1

        print(letras_acertadas)

if (__name__ == "__main__"):
    jogar()
