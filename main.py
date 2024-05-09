import random

numeroSecreto = random.randint(1, 50)

print("Bem vindo ao jogo", "\n" "Digite um número de 1 a 50 para adivinhar: ")

tentativas = 0 

while tentativas <5: 
     palpite = int(input("Digite seu palpite"))
    
     if palpite == numeroSecreto: 
        print("Você acertou!")
     elif palpite < numeroSecreto:
        print("Muito baixo")
     else: 
        print("Muito alto")
        
     tentativas += 1
    
if tentativas == 5: 
    print("Acabaram as tentativas. O número secreto era:" , numeroSecreto)