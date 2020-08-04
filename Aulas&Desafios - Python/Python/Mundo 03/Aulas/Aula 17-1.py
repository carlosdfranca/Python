num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print (num)
num.sort(reverse=True)
num.insert(2, 2)
print (num)
num.pop(4)
print (num)
num.remove(2) #elimina só o primeiro elemento
print (num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(f'Essa lista tem {len(num)} elementos')