#każdy element z listy musi zostać przetworzony. w pętli while element \n
#musiał zostać przetworzony określoną ilość razy, i poprzez warunek decydujemy
# czy element ma zostać przetworzony czy nie.

#zad.1
#pętla for i konwertowanie napisów do duzych liter
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for a in data:
    print(a.upper())

#zad.2
for a in data:
    elements=a.split(":")
    print(elements[0].upper())
    print(elements[1])

#zad.3
for a in data:
    elements = a.split(":")
    if elements[0]=='Error':
        print(elements[0], elements[1].upper())
    else:
        print(elements[0], elements[1])

