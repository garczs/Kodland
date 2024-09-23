import random
x = int(input('Ile faktow podac?'))
fakts = []
for i in range(x):
    fakt = input('podaj fakt')
    fakts.append(fakt)
print('twoja prawda to', random.choice(fakts))
