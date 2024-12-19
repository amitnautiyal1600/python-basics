def is_leap_year(year):
    is_leap = False
    if year % 4 == 0 :
        is_leap = True
        if year % 100 == 0 :
            is_leap = False
            if year % 400  == 0:
                is_leap = True
    print(is_leap)


is_leap_year(2000)
is_leap_year(2400)
is_leap_year(1989)
is_leap_year(2100)