#Exercicio 2 
#Escreva um programa em Python que solicite ao usuárioo salário atual e mostre o salário acrescido de 5% de comissão.

salario = float(input('Por gentileza informe seu salario atual R$:'))
comissao =  (salario * 5 / 100)

print('O salario atuaizado com a comissão de 5% é de R$:', salario + comissao)
