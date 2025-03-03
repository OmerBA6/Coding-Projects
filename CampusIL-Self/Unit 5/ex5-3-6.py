

def filter_teens(a = 13, b = 13 ,c = 13):
    sum_of_ages = 0

    if(a not in range(13,19) or a == 15 or a == 16):
        sum_of_ages += a
    else:
        sum_of_ages += fix_age(a)

    if(b not in range(13,19) or b == 15 or b == 16):
        sum_of_ages += b
    else:
        sum_of_ages += fix_age(b)

    if(c not in range(13,19) or c == 15 or c == 16):
        sum_of_ages += c
    else:
        sum_of_ages += fix_age(c)
    

    return sum_of_ages


def fix_age(age):
    return(0)

print (filter_teens(2 , 1, 15))