vogais = 'aeiouáéíóú'
contador = 0
texto = input('Digite uma palavra ou frase: ')

for letra in texto:
    if letra in vogais:
        contador += 1
print('O número de vogais que existem nessa palavra/frase é: {}'.format(contador))

