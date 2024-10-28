'''
nome: Clarissa Cruz
data: 28/10/2024
versao: 2
'''

#Faça um programa que peça dois números e verifique (usando if e else) e imprima o maior deles

num1 = float (input ('Adicione um número: '))
num2 = float (input ('Adicione outro número: '))

if num1 > num2:
    print (f'O {num1} é maior que o {num2}')
elif num1 == num2:
    print (f'Os dois números são iguais')
else:
    print (f'O {num2} é maior que o {num1}')