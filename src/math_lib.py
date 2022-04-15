import math

pi = math.pi
e = math.e

def sinus(x):
    return round(math.sin(x), 9)

def kosinus(x):
    return round(math.cos(x), 9)

def tangens(x):
    return round(math.tan(x), 9)

def logaritmus(x):
    return round((math.log(x, 10)), 9)

def ln_logaritmus(x):
    return round((math.log(x, e)), 9)

def x_na_druhu(x):
    return round((x ** x), 9)

def jedna_deleno_x(x):
    return round((1 / x), 9)

def absolutna_hodnota(x):
    return round((math.fabs(x)), 9)

def x_na_tretiu(x):
    return round((x ** x ** x), 9)

def desat_na_x(x):
    return round((10 ** x), 9)

def odmocnina(x):
    return round(math.sqrt(x), 9)

def modulo(x, y):
    return round(x % y, 9)

def faktorial(x):
    return round(math.factorial(x), 9)

def nasobenie(x, y):
    return round(x * y, 9)

def delenie(x, y):
    return round(x / y, 9)

def scitanie(x, y):
    return round(x + y, 9)

def odcitanie(x, y):
    return round(x - y, 9)