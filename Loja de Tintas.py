print('-' * 15)
print('Loja de Tintas:')
print('-' * 15)

import math
# Área total a ser pintada
altura = float(input('\033[34mInforme a altura a ser pintada:\033[0m '))
largura = float(input('\033[34mInforme a largura a ser pintada:\033[0m '))
print(f'\033[32mA área total para pintura é de {altura * largura:.2f} m²\033[0m ')


# Quantidade de tinta para pintura
area = altura * largura
litros = area / 3
print(f'\033[31mVocê vai precisar de {litros:.2f} litros de tinta\033[0m ')

# Quantidade de latas a serem compradas
litros_por_latas = 18
valor_da_lata = 80
latas = math.ceil(litros / litros_por_latas)
valor_total = latas * valor_da_lata
print(f'\033[44mVocê vai precisar comprar {litros_por_latas} que vai custar R${valor_total:.2f}\033[0m ')


