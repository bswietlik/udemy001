# przykład rozwiązania zadania
lista = [1, 3, 7, 11, 2, -6, 0]
# zmienna przechowująca najmniejsza wartość
# na początku przypisujemy wartość None, aby w pętli for
# wiedzieć że jest to pierwsza interakcja
# później zmienna, zaczyna zawierać liczby z listy
najmniejsza = None
for i in lista:

    # przy każdej iteracji, sprawdzamy czy zmienna i
    # jest mniejsza przechowywane przez nas zmienna
    # Jeżeli tak, to ją zapisujemy

    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i

print("najmniejsza liczba to:", najmniejsza)

# liczymy sumę danej liczby i poprzedniej definiujemy zmienną, która przechowuje poprzednią wartość
poprzednia = 0
# uruchamiamy pętle, przechodzącą od 0 do 10
for i in range(0, 11):
    # wypisujemy sumę obecnej liczby, przechowywanej w zmiennej i
    # oraz liczby poprzedniej
    print(i + poprzednia)

    # zapisujemy obecną zmienną i do zmiennej poprzednia
    # zanim pętla sie powtórzy, a i przyjmie nową wartość
    poprzednia = i
