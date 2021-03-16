# 13. Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando
#  as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite a sua altura:  '))
p_homem = (72.7 * altura) - 58
p_mulher = (62.1 * altura) - 44.7
if p_homem >= 63.97:
    print(f'Peso homem {p_homem:.2f}')
else:
    print(f'Peso Mulher {p_mulher:.2f}')
