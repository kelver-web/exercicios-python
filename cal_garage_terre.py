lar_garage = int(input('Digite a largura da garagem:  '))
prof_garage = int(input('Digite a profundidade da garagem:  '))
area_garage = lar_garage * prof_garage
print(f'{area_garage}mts')

lar_terreno = int(input('Digite a largura do terreno:  '))
prof_terreno = int(input('Digite a profundidade do terreno:  '))
area_terreno = lar_terreno * prof_terreno
print(f'{area_terreno}mts')

percent_ocupation = ((area_garage) * (area_terreno)) / 100
print(f'Percentual de ocupação: {percent_ocupation}mts')
