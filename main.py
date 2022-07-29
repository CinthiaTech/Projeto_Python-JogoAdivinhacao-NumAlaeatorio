import random
print("********************************")
print("BEM VINOD AO JOGO DE ADIVINHAÇÃO")
print("********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 5
rodada = 1

print(numero_secreto)

while (rodada <= total_de_tentativas):
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou!")
        break



    else:
        if (maior):
            print("O seu chute foi maior do que o número secreto!")
        elif (menor):
            print("O seu chute foi menor do que o número secreto!")

    rodada = rodada + 1

print("FIM DO JOGO")



