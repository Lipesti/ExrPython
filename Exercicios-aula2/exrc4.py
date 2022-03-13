#Exercicio 4 
#Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c.
#Conhecendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais. 
# Lembre-se que para calcular as duas raízes:

def raizes (a, b, c):
        D= (b**2 - 4*a*c)
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)

        print('\nValor de x1: {0: .2f}'.format(x1))
        print('Valor de x2: {0: .2f}'.format(x2))

#if name == 'main':
while True:
      print('Calculando as raízes de uma equação de 2º grau \n')
      a = float(input('Informe o valor de a: '))
      b = float(input('Informe o valor de b: '))
      c = float(input('Informe o valor de c: '))
      raizes(a,b,c)
      continua = input('Deseja sair? Digite s: ')
      if(continua == 's'):
                         break
