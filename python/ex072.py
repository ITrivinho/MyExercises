nums = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
user = ' '
while True:
    user = int(input('Digite um número de 0 a 20: '))
    if 0 <= user <= 20:
        break
print(f'Você digitou o número {nums[user].upper()}')
