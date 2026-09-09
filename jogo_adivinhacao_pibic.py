print()
print("=====JOGO DE ADIVINHAÇÃO=====")

# MINHA IDEIA: 

# Importar biblioteca de aleatoriedade
import random 

# Geração de um número aleatório no intervalo de 1 a 100:

numero_aleatorio = random.randint(1,100)

# Tentativas do jogador: loop

print("O número está entre 1 e 100.")
print()

tentativas = 0
while True:
    numero = int(input("Digite um número inteiro: "))
    tentativas += 1

# Definir proximidade entre o número digitado e o gerado aleatoriamente: 
    proximidade = abs(numero_aleatorio - numero)

# Classificação: 
    if numero_aleatorio == numero:
        print("Parabéns! Você acertou o número!")
        print(f"Você usou {tentativas} tentativas.")
        print(tentativas)
        break
    elif numero_aleatorio > numero:
        if proximidade <= 30:
            print("O seu número foi BAIXO (mas está perto)")
        else:
            print("O seu número foi MUITO BAIXO (está longe)")
    else:
        if proximidade <= 30:
            print("O seu número foi ALTO (mas está perto)")
        elif proximidade > 30:
            print("O seu número foi MUITO ALTO (está longe)")
 
            




          

