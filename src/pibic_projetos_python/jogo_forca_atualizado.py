import random


# 1º: Declaração das funções principais para rodar o jogo:

def definir_palavra():
    palavras = ["python","computador","programa","comandos","codigo","algoritmo",
                "teclado","monitor","tecnologia","arquivo",]
    return random.choice(palavras)

def mostrar_estado(quantidade_tracinhos, tentativas, letras_usadas):
    print()
    print("Palavra:", " ".join(quantidade_tracinhos))
    print(f"Tentativas restantes: {tentativas}")
    print("Letras usadas:", sorted(letras_usadas))

def validacao_letra(letras_usadas):
    while True:
        letra = input("Digite uma letra: ").lower().strip()

        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra!")
        elif letra in letras_usadas:
            print("Você já tentou essa letra. Tente outra!")
        else:
            return letra

def atualizar_palavra(palavra_secreta, quantidade_tracinhos, letra):
    acertou = False

    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            quantidade_tracinhos[i] = letra
            acertou = True

    return acertou


# 2º: Chamar as funções já declaradas para o funcionamento da interação (o jogo em si):

def jogar():
    palavra_secreta = definir_palavra()
    quantidade_tracinhos = ["_"] * len(palavra_secreta)
    letras_usadas = set()
    tentativas = 6

    print("===== JOGO DA FORCA =====")
    print()
    print("TEMA: COMPUTAÇÃO")
    print(f"A palavra tem {len(palavra_secreta)} letras.")

    while tentativas > 0 and "_" in quantidade_tracinhos:
        mostrar_estado(quantidade_tracinhos, tentativas, letras_usadas)

        letra = validacao_letra(letras_usadas)
        letras_usadas.add(letra)

        if atualizar_palavra(palavra_secreta, quantidade_tracinhos, letra):
            print(f"Boa! A letra '{letra}' está na palavra!")
        else:
            tentativas -= 1
            print(f"A letra '{letra}' não está na palavra. Você perdeu uma vida!")

    print()

    if "_" not in quantidade_tracinhos:
        print(f"Parabéns! Você acertou a palavra: {palavra_secreta}")
    else:
        print("Você perdeu! Acabaram as suas tentativas.")
        print(f"A palavra secreta era: {palavra_secreta}")


def main():
    jogar()


if __name__ == "__main__":
    main()
