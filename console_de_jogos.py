print("**********************")
print("Bem vindo à Xico Station!")
print("************************")

usuario = input("Qual o seu nome, nobre jogador?")
print("Seja muito bem vindo à Xico Station, {}!".format(usuario))

tipo_jogo = int(input("Qual jogo você quer jogar? (1) Forca (2) Adivinhação: "))
if(tipo_jogo ==1):
    print("Você escolheu o jogo de Forca!")
    import forca
else:
    print("Você escolheu o jogo de Adivinhação!")
    import jogo

