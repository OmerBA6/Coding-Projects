__author__ = "Omer"


def main():
    i = 0
    for date_and_time in gen_date_and_time():
        if(i % 100000000 == 0):
            print (date_and_time)
        i += 1





def gen_date_and_time():
    for date in gen_date():
        for time in gen_time():
            yield (date + " " + time)
    
def gen_time():

    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield ("{:02d}:{:02d}:{:02d}".format(hour, minute, second))

def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, check_if_leap_year(year)):
                yield ("{:02d}/{:02d}/{:04d}".format(day, month, year))

def gen_secs():
    return (sec for sec in range(0, 60))

def gen_minutes():
    return (minute for minute in range(0, 60))

def gen_hours():
    return (hour for hour in range(0, 24))


def gen_years(start = 2022):
    return (year for year in range(start, 10000))


def gen_months():
    return (month for month in range(1,13))

def gen_days(month, leap_year = True):

    if (leap_year and month == 2):
        return (day for day in range(1,30))
    elif((not leap_year) and (month == 2)):
        return (day for day in range(1,29))
    elif(check_if_long_month(month)):
        return (day for day in range(1,32))
    else:
        return (day for day in range(1,31))


def check_if_long_month(month):
    return (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12)


def check_if_leap_year(year):
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))





if __name__ == "__main__":
    main()

