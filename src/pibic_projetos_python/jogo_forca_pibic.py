# JOGO DA FORCA:

# Definir palavra secreta (todas as letras minúsculas):
import random

palavras = ["python", "computador", "programa", "comandos", "codigo",
            "algoritmo", "teclado", "monitor", "tecnologia", "arquivo"]

palavra_secreta = random.choice(palavras)

# A quantidade de traços equivale ao tamanho da palavra secreta:
quantidade_tracinhos = ["_"] * len(palavra_secreta)

# Lista para guardar as letras usadas: elas devem ser usadas apenas uma vez
letras_usadas = set()   

tentativas = 6

print("=====JOGO DA FORCA=====")
print()
print("TEMA: COMPUTAÇÃO ")
print(f"A palavra tem {len(palavra_secreta)} letras. ")


# ___________________________________________________________________________________________________________________________________________________________________________
# Laço principal:
while tentativas > 0 and "_" in quantidade_tracinhos:
    print()
    print("Palavra: ", " ".join(quantidade_tracinhos)) # converter a lista com _ para strings sem aspas
    print(f"Tentativas restantes: {tentativas}") 
    print("Letras usadas:", sorted(letras_usadas)) # Ordenação por uso das letras usadas

    letra = input("Digite uma letra: ").lower().strip()

    # Validação da letra: aceitar SOMENTE uma letra

    if len(letra) != 1 or not letra.isalpha():  # isalpha valida se o que foi digitado é uma letra ou não
        print("Digite apenas uma letra!")
        continue # volta ao início do while sem consumir uma vida 

    if letra in letras_usadas: # estamos digitando uma letra já usada
        print("Você já tentou essa letra. Tente outra! ")
        continue 

    # Adicionar as letras usadas na lista: sem repetição de letras

    letras_usadas.add(letra)

    if letra in palavra_secreta:
        print(f"Boa! A letra {letra} está na palavra secreta! ")

    # Percorre a palavra secreta pela posição da letra: 
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                quantidade_tracinhos[i] = letra # letra na posição certa da palavra
    else: 
        tentativas -= 1
        print(f"A letra '{letra}' não está na palavra. Você perdeu uma vida")

# ___________________________________________________________________________________________________________________________________________________________________________


print()

if "_" not in quantidade_tracinhos:
    print(f"Parabéns! Você acertou a palavra: {palavra_secreta}")
else:
    print("Você perdeu! Acabaram as suas tentativas")
    print(f"A palavra secreta era {palavra_secreta}")


def main() -> None:
    print("Hello from pibic-projetos-python!")


if __name__ == "__main__":
    main()











    
    
