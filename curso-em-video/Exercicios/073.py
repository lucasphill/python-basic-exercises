times = ('Fortaleza','Grêmio','Fluminense','São Paulo','Palmeiras','Bahia','Vasco','Botafogo','Juventude','Criciúma','Vitória','Flamengo','Atlético-GO',
         'Internacional','Cruzeiro','Atlético-MG','Athletico-PR','Corinthians','Bragantino','Cuiabá')

#Os 5 primeiros
pos = 1
print(f'Primeiros 5: ')
for t in times[0:5]:
    print(f'{pos} - {t}')
    pos += 1
print('#'*20)

#Os 4 ultimos
pos = 16
print(f'Ultimos 4')
for t in times[-4:]:
    print(f'{pos} - {t}')
    pos += 1
print('#'*20)

#Ordem Alfabética
pos = 1
print(f'Ordem Alfabética')
for t in sorted(times):
    print(f'{pos} - {t}')
    pos += 1
print('#'*20)

#Em que posição está o time Internacional
print(f'O Inter está na posição: {times.index('Internacional')+1}')