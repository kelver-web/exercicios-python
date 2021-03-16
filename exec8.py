# 8. Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês.

ganho_hora = float(input('Digite quanto você ganha por hora:  '))
horas_mes = float(input('Quantas horas você trabalha por mês?:   '))
total = ganho_hora * horas_mes
print(f'O total do seu salário é -> {total}')

# Meu exercício
print('Demostrativo nac')
salario = int(input('Digite o seu salário:  '))
horas_trabalhadas = int(input('Digite quantas horas você trabalha:  '))
total = (salario / horas_trabalhadas)
print(f'Sua hora aula é -> {total}')
