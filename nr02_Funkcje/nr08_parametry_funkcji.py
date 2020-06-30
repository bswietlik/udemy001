#okreslam zmienne funkcji
def GiveWorkingDay (year,month,day):
    from datetime import  date
    from datetime import  timedelta
    day = date(year,month,day)  # zwaraca dzień dzisiejszy

    if day.weekday() == 5:  # mamy sobote
        workingday = day + timedelta(days=2)  # dodajemy 2 dni żeby był poniedziałek
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    print('working day', day, 'is', workingday)
    return


GiveWorkingDay(2020,4,13)