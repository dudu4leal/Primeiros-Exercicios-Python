#tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol de 2024, na ordem de colocação. 
# Depois mostra: a) Os 6 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time do Botafogo.

brasileirao2024 = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória',
                    'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 'RB Bragantino', 'Athletico Paranaense', 'Criciúma', 'Atlético Goianiense', 'Cuiabá')

print('-=' * 15)
print(f'Tabela final do Brasileirão 2024: {brasileirao2024}')
print('-=' * 15)
print(f'Classificados para a Libertadores da América: {brasileirao2024[:6]}')
print('-=' * 15)
print(f'Rebaixados para a Série B: {brasileirao2024[-4:]}')
print('-=' * 15)
print(f'Clubes participantes(em ordem alfabética): {sorted(brasileirao2024)}')
print('-=' * 15)
print(f'O Botafogo ficou na {brasileirao2024.index('Botafogo')+1}º posição!')
print('-=' * 15)

