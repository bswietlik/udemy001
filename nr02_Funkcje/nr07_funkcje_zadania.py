#chcę ustalić czy dany dzień jest dniem roboczym. Za sobotę lub niedzielę trzeba wyświetlic
#datę poniedziałku
#trzeba zrobić import modułu czasu
def GiveWorkingDay():
    from datetime import date
    from datetime import  timedelta

    day=date.today() #zwaraca dzień dzisiejszy

    if day.weekday()==5: #mamy sobote
        workingday=day+timedelta(days=2)#dodajemy 2 dni żeby był poniedziałek
    elif day.weekday()==6:
        workingday = day + timedelta(days=1)
    else:
        workingday=day
    print('working day', day,'is', workingday)
    return
GiveWorkingDay()
#zad.1 funkcja ile dni zostało do konca roku

def liczIleDoKoncaRoku():
    from datetime import  date
    current_day=date.today()
    current_year=current_day.year
    date_end_year=date(current_year,12,31)
    delta=date_end_year-current_day
    print(delta.days)
    return
liczIleDoKoncaRoku()

