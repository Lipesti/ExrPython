#Exercicio 5
#Escreva um programa em Python que leia a cotação do dólar (taxa de conversão), leia um valor em dólares e converta e mostre o valor equivalente em Reais.

dolar = float(input("Informe a quantidade de dólar para conversão: US$ "))
cotacao = float(input ("Informe o valor da cotação do dólar: R$ "))
conversao = dolar*cotacao
print('A quantidade de dólar convertido em real é: R$',conversao)