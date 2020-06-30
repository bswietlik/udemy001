#sprawdzamy czy liczba z zakresu jest parzysta`. Trzeba zastosować dzielenie modulo
for number in range(1,21):
    if number%2==0:
        print('number %2d is %s' % (number, 'even'))
    else:
        print('number %2d is %s' % (number, 'odd'))
    #print(number)

#zad.1 wyświetl

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range (1,11):
    print(i, string_A)

for i in range (1,11):
    if i%2==0:
        print(i, string_B)
    else:
        print (i, string_A)

napis='x'
napis2='o'
for i in range (1,10):
    print(napis*i)

for i in range(1,10):
    if i%2==0:
        print(napis*i)
    else:
        print(napis2*i)

