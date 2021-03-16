# 11. Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('digite um número:  '))
n2 = int(input('Digite outro:  '))
n3 = float(input('Digiete outro:  '))
result1 = (n1 * 2) * (n2 / 2)
result2 = (n1 * 3) + n3
result3 = n3 ** 3
print(f'O produto do dobro do primeiro com metade do segundo é -> {result1}')
print(f'A soma do triplo do primeiro com o terceiro -> {result2}')
print(f'O terceiro elevado ao cubo -> {result3}')
