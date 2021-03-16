# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

ganho_hora = float(input('Digite quanto você ganha por hora:  '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas:  '))
salario = ganho_hora * horas_trabalhadas
inposto_renda = salario * (11 / 100)
inss = salario * (8 / 100)
sindicato = salario * (5 / 100)
salario_liquido = salario - inposto_renda - inss - sindicato
print(f'+ Salário bruto: {salario:.2f}')
print(f'- IR (11%) : R${inposto_renda:.2f}')
print(f'- INSS (8%) : R${inss:.2f}')
print(f'- Sindicato : R${sindicato:.2f}')
print(f'= Salário Lóquido : R${salario_liquido:.2f}')
