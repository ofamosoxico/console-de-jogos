import random

print("**********************")
print("Bem vindo jogador")
print("************************")
usuario = input("Qual o seu nome? ")
print("Seja bem vindo", usuario, "!")

resposta = int(random.randint(1, 100))
tentativa = int("1")
chances = int("3")

while (tentativa <= chances):
    print("Tentativa {} de {}".format(tentativa, chances))
    palpite = input("Digite um numero aleatorio entre 1 e 100: ")
    chute = int(palpite)

    if (chute < 1 or chute > 100):
        print("Você chutou um numero não válido")
        tentativa = tentativa + 1
        continue

    if (chute == resposta):
        print("Você acertou, {}, meus parabéns! O número secreto era {}!".format(usuario, resposta))
        break
    elif (chute > resposta):
        print("Poxa", usuario, "você chutou um valor acima do valor correto!")
    elif (chute < resposta):
        print("Poxa", usuario, "você chutou um valor abaixo do valor correto!")
    tentativa = tentativa + 1

print("Fim do jogo! Obrigado pro jogar, {}! O número secreto era {} !".format(usuario, resposta))
