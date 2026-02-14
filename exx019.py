import random
aluno = random.randint(1, 4)
if aluno == 1:
    aluno = 'Ana'
elif aluno == 2:
    aluno = 'Bruno'
elif aluno == 3:
    aluno = 'Carla'
else:
    aluno = 'Daniel'
print(f'O aluno(a) escolhido foi {aluno}')

