def wypiszWszystkie(*slowa):
    wynik =" "
    for x in slowa:

        wynik += x
        wynik += " "
        print("ze spacja: ", wynik)
    return
wypiszWszystkie('Witaj', 'Cześć', 'Andrzeju')