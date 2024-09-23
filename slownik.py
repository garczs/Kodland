slownik = {}
for i in range(5):
    x = input("Podaj słowo: ")
    y = input('Podaj tłumaczenia:')
    slownik[x] = y
word = input("Wpisz słowo którego nie rozumiesz(używaj wielkich liter)")
if word in slownik.keys():
    print(word, ":", slownik[word])
else:
    print("nie rozumiem")
