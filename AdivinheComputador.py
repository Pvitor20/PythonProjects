import random

print("Vou tentar adivinhar o seu número!!! \n Pense em um numero de 1 a 100")

def computer_guess(max):
    min = 1
    feedback = ""
    computer_number = 0
    while feedback != "c":
        if min != max:
            computer_number = random.randint(min, max)
        else: 
            computer_number = min 
        feedback = input(f"{computer_number} é muito alto (A), muito baixo (B) ou está correto (C)?").lower()
        
        if feedback == "a":
            max = computer_number -1
        
        elif feedback == "b":
            min = computer_number + 1
        
    print("Acertei!!!")

computer_guess(100)