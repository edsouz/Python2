l = [1,2,3,4,5,6,7,8,9,10]

for num in l:
    print(num)

print()
for num in l:
    if num%2 == 0:
        print(num, 'é par')
    else:
        print(num, 'é ímpar')

print()

soma = 0
for num in l:
    soma += num
print('A soma dos ítens de l é',soma)
