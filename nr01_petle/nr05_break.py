#chcemy sprawdzić czy liczba jest liczbą pierwszą
#chcemy zastosować break jesli jest więcej dzielników danej liczby

for x in range (2, 31):
    isPrime=True #zakładamy, ze udało się nam znaleźć liczbą pierwszą
    for divider in range (2,x):
        if x%divider==0: #szukamy dzieolników
            isPrime=False #jeśli uda nam się znaleźć dzielnik to wtedy nie ma liczby pierwszej
            print ('%2d is not a prime number-divider is %2d' % (x, divider))
            break #break uruchamia się tylko przy znalezeniu kolejnego dzielnika

    if isPrime: #kiedy dana petla zakonczy sie wartość bedzie True albo false
        print('%2d is a prime' % (x))

#zad.1
text = 'Mechanical advantage is a measure of the force ' \
       'amplification achieved by using a tool, mechanical ' \
       'device or machine system. The device preserves the input ' \
       'power and simply trades off forces against movement to ' \
       'obtain a desired amplification in the output force. The' \
       ' model for this is the law of the lever. Machine ' \
       'components designed to manage forces and movement in' \
       ' this way are called mechanisms.[1] An ideal mechanism ' \
       'transmits power without adding to or subtracting from ' \
       'it. This means the ideal mechanism does not include a ' \
       'power source, is frictionless, and is constructed from ' \
       'rigid bodies that do not deflect or wear. The ' \
       'performance of a real system relative to this ideal.'

#trzeba zbudować streszczenie definicji poprzez wyswietlenie pirewszych 20 slow
words=text.split(' ')
short_text=''
counter=0

for i in words:
    short_text+=i+' '
    counter+=1
    if counter >=20:
        print (short_text)
        break

