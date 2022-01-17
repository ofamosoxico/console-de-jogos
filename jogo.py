import random

from console_de_jogos import usuario
print("**********************")
print("Bem vindo, {}!".format(usuario))
print("************************")
pontos = int(100)

nivel= int(input("Escolha abaixo qual nível de jogo você quer, entre (1) Fácil (2) Médio (3) Difícil: "))
if (nivel ==1):
    print("Você escolheu o nível Fácil!")
    chances=int("50")
elif (nivel ==2):
    print("Você escolheu o nível Médio!")
    chances = int("25")
else:
    print("você escolheu o nível Difícil!")
    chances = int("10")

resposta = int(random.randint(1, 100))
tentativa = int("1")


while (tentativa <= chances):
    print("Tentativa {} de {}".format(tentativa, chances))
    palpite = input("Digite um numero aleatorio entre 1 e 100: ")
    chute = int(palpite)

    if (chute < 1 or chute > 100):
        print("Você chutou um numero não válido")
        tentativa = tentativa + 1
        continue

    if (chute == resposta):
        print("Você acertou, {}, meus parabéns! O número secreto era {} e com isso você fez {} pontos!".format(usuario, resposta, pontos))
        break
    elif (chute > resposta):
        print("Poxa", usuario, "você chutou um valor acima do valor correto!")
    elif (chute < resposta):
        print("Poxa", usuario, "você chutou um valor abaixo do valor correto!")
    tentativa = tentativa + 1
    pontos = pontos - 1
    print("Você tem {} pontos!".format(pontos))
break