'''
A Bate Ponto LTDA bonifica seus funcionários de acordo o tempo de serviço na empresa Escreva um programa que leia o tempo de serviço de um funcionário e o valor do bônus por ano trabalhado. Mostre na tela quanto será a bonificação do funcionário.

'''

tempo = int(input())
bonus = float(input())
bonus *= tempo
print('%.2f'%bonus)