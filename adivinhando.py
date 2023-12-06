import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = (random.randrange(1, 101))
total_de_tentativas = 0
pontos = 1000

print("Qual nivel de dificuldade você quer?")
print("(1) facil (2) medio (3) dificil")

nivel = int(input("Defina um nivel:"))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print("tentativa  {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu numero entre 1 e 100:"))
    print("Você digitou:", chute)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos".format(pontos))
        break
    else:
        if (maior):
            print("Você errou o seu chute foi maior que o numero secreto")
        elif (menor):
            print("Você errou e seu chute foi menor que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        print(pontos_perdidos)
    # ********************************************************************

print("***********")
print("Fim de jogo")
print("***********")
