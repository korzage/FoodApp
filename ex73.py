times = ('Flamengo', 'Internacional', 'Atlético - MG', 'São Paulo', 'Fluminense', 'Grêmio','Palmeiras','Santos',
         'Athletico-PR','Red Bull Bragantino','Ceará','Corinthians','Atlético-GO','Bahia','Sport','Fortaleza',
         'Vasco da Gama','Góias','Coritiba','Botafogo')
print(f'Os cinco primeiros colocados são : {times[:5]}')
print(f'Os quatro últimos colocados são : {times[16:]}')
print(f'Os times em ordem alfabética {sorted(times)}')
print(f'O último colocado é o {times[19]}')
print('O Bragantino ta na posição {}'.format(times.index('Red Bull Bragantino')))