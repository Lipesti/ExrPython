#Exercicio 6 
#Escreva um programa em Python que leia um valor representando o gasto realizado por um cliente do restaurante ComaBem e visualize o valor total a ser pago, considerando os 10% do garçom.

gasto = float(input('Digite o gasto do cliente no restaurante ComaBem: '))
total = gasto + (gasto * 0.10)
print('A conta ficou de R$ {}'.format(total))