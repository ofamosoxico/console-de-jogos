import random

from console_de_jogos import usuario
print("************************")
print("Bem vindo ao jogo de Forca, {}!".format(usuario))
print("************************")

with open("lista_frutas.txt") as file:
    nomes = file.readlines()

palavra_secreta = random.choice(nomes)
palavra_secreta_mi= palavra_secreta.lower().strip()
letras_acertadas = ["_" for letrinha in palavra_secreta_mi]
enforcou = False
acertou = False
erro = int("0")

while (not enforcou and not acertou):

    chute1 = input("Digite uma letra abaixo: ")
    chute = chute1.strip()

    if (chute in palavra_secreta_mi):
        index = int("0")
        for letrinha in palavra_secreta_mi:
            if (chute == letrinha):
                letras_acertadas[index] = letrinha
                print("Parabéns, seu chute é uma das letras dessa palavra!")
            index += 1
    else:
        erro += 1
        print("Você errou, e ainda possui {} tentativas!".format(10-erro))

    enforcou = erro == 10
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

if(enforcou):
    print("Você perdeu o jogo. A palavra correta era {}!".format(palavra_secreta_mi))
elif(acertou):
    print("Parabéns, você venceu!A palavra correta era {}!".format(palavra_secreta_mi))

print("Fim do jogo")



