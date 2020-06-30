#zad.1 wyznacz wartość silni i=10

i=10

result = 1

for j in range(1, i + 1):
    result *= j

print(i, result)

#zad.2 policz silnie dla liczb od 1 do 10
result=1
for i in range(0,10):
    i+=1
    result*=i
    print(i, result)

#zad.3
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for x in list_noun:
    for y in list_adj:
        print (x, y)
