#Exercicio 3 
#Escreva um programa em Python que solicite ao usuário a distância entre duas cidades e o tempo de viagem. 
#O programa deverá calcular e exibir a velocidade média de um carro que vai de uma cidade para outra.

distancia = float(input('Digite a distancia em km: '))
tempo = float(input('Informe o tempo de viagem: '))

vmedia = distancia /tempo;


print('A velocidade media entre as cidades é ', vmedia)