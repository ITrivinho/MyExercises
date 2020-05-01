n = c = 0
msg = 'TABUADA'
print('=' * 40)
print(f'{msg:^40}')
print('=' * 40)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
    print('-' * 30)
print('\nPrograma finalizado'.upper())
