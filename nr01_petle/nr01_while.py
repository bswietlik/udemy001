#wyznaczam sumy kolejnych dwóch liczb od 0 do 50
number=1
previousNumber=0
while number <= 50:
    print(number, previousNumber+number)
    previousNumber=number
    number+=1