# 9. Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

f = float(input('Digite a temperatura para ver em graus C*:  '))
C = (f - 32) * (5 / 9)
print(f'A temperatura é -> {C:.1f}°C')
