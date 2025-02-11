
def argumente(**kwargs):
    print(kwargs)

argumente(kwargs1 = "Hund", kwargs2 = "Katze", kwargs3 = 2.0, kwargs4 = True, kwargs6 = 5)

#-------------------------------------------------------------------------------------------------------#

def multiplikation(*args):
    z = 5
    for zahl in args:
        z *= zahl # mit * sagen wir, wie er rechnen soll
    print(z)

multiplikation(5,2)

#-------------------------------------------------------------------------------------------------------#

def multiplikation(x, y):
    print (x + y)

multiplikation(3,6)


