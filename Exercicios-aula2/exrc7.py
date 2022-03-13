#Exercicio 7 
#Escreva um programa em Python que obtenha uma temperatura em graus Celsius, calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin. Utilize as cfórmulas abaixo:

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Kelvin')
    print('2. Converter de Celsius para Fahrenheit')

def kel_cel():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    K = C + 273
    print('Valor em Kelvin: {0}°K'.format(K))

def fahr_cel():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = 1.8 * C + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        kel_cel()

    if escolha == '2':
        fahr_cel()

        