print('Hello 11.fakt')

nevek = ["Hanga", "Boldi", "Abel", "Adam"]

nev=input('Mi a neved?')

for i in range(len(nevek)):
    if nev==nevek[i]:
        print('Faktos vagy!')
        break
    else:
        print('Nem vagy faktos!')
        break
