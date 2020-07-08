lista = [1, 3, 7, 11, 13, 17, 23]
cel = 17


def szukaj(lista, cel, pozycja):
    if lista[pozycja] == cel: #Funkcja, sprawdza czy element w liście, znajdujący się na tej pozycji, jest tym, którego szukamy
        print("Znalazłem na pozycji", pozycja)
        return
    elif pozycja == len(lista) - 1: #Jeżeli nie znalazł, to sprawdzamy czy to był ostatni element na liście
        print("Nie znalazłam celu") #jeżeli tak, to drukujemy komunikat, że liczby którą szukamy nie ma na liście
        return
    szukaj(lista, cel, pozycja + 1) #Jeżeli nie, to funkcja, wywołuje sama, siebie, lecz z ‚pozycja+1


szukaj(lista, cel, 0) #Wywołujemy nasza funkcję, a jako pozycja, podajemy liczbę 0, będącą odpowiednikiem pierwszej pozycji w liście, do sprawdzenia

  #zad.2 chcemy sprawdzić tekst pod kątem wielkości liter, duże litery zaminieć na małe a małe na duże
tekst = "Dawno, dawno, temu. Na odległej stronie, o analizie danych i AI..."


def zamień(tekst, pozycja):
    if tekst[pozycja].isupper():
        tekst = tekst[0:pozycja] + tekst[pozycja].lower() + tekst[pozycja + 1:] #funkcji ‚isupper()’, sprawdzamy czy litera w łańcuchu na tej pozycji jest wielka. Jak jest to tworzymy
        # łańcuch na nowo. Łańcuchy nie wspierają podmiany pojedynczej litery, tak jak lista wspiera podmianę jednego elementu, dlatego musimy łańcuch utworzyć na nowo:
        # najpierw część do tej pozycji, potem zamieniamy literę na pozycji na małą, a na końcu dodajemy resztę łańcucha.

    else:
        tekst = tekst[0:pozycja] + tekst[pozycja].upper() + tekst[pozycja + 1:]

    if pozycja == len(tekst) - 1: return tekst;  #sprawdzamy czy parametr ‚pozycja’, wskazuje na koniec łańcucha, jeżeli tak, to zwracamy łańcuch, za pomocą ‚ return tekst ‚

    return zamień(tekst, pozycja + 1) #ponownie wywołujemy funckję i przesuwamy element do przodu


print(zamień(tekst, 0))