n = 1
while n <= 100:
    for c in range(1, 11):
        print('{} x {} = {}'.format(n,c,n*c))
        if c == 10:
            n = n +1
            break
print('FIM')
