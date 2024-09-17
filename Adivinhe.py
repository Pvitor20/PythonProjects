import random

print("Adivinhe o número!!!")

def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input("Digite um número"))
        if guess_number > random_number:
            print("Errou!!! Muito alto")

        elif guess_number < random_number: 
            print("Errou!!! Muito baixo")    

    print("Parabén, você acertou!!!")

guess(10)