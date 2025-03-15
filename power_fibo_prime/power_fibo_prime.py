from decimal import Decimal, getcontext
from math import floor
from .matrix import Matrix


"""Возведение в степень"""


def iter_power(number, power):
    """ итеративный O(N) """
    if number == 0:
        return 0
    if number == 1:
        return 1
    if power == 1:
        return number
    if power == 0:
        return 1
    result = 1
    for _ in range(power):
        result *= number
    return result


def recurs_power(number, power):
    """ через домножение O(N/2+LogN) = O(N) """
    if number == 0:
        return 0
    if number == 1:
        return 1
    if power == 1:
        return number
    if power == 0:
        return 1
    result = recurs_power(number, power//2)
    if power % 2 == 0:
        return result*result
    else:
        return number*result*result


"""Поиск чисел Фибоначчи"""


def recurs_fibo(number):
    """ рекурсивный O(2^N) """
    if number == 0:
        return 0
    if number == 1:
        return 1
    result = recurs_fibo(number-1)+recurs_fibo(number-2)
    return result


def iter_fibo(number):
    """ итеративный O(N) """
    if number == 0:
        return 0
    if number == 1:
        return 1
    result0 = 0
    result1 = 1
    for i in range(2, number+1):
        result2 = result1+result0
        result0, result1 = result1, result2
    return result2


def golden_fibo(number):
    """ по формуле золотого сечения """
    if number == 0:
        return 0
    getcontext().prec = 500000
    sqrt5 = Decimal('5').sqrt()
    f = (sqrt5+Decimal('1')) / Decimal('2')
    result = floor((f**number)/sqrt5+Decimal('0.5'))
    return round(result)


def matrix_fibo(number):
    """ через умножение матриц O(LogN) """
    if number == 0:
        return 0
    if number == 1:
        return 1
    fibo_matrix = Matrix(2, 2, [1, 1, 1, 0])
    return fibo_matrix.power(number-1)[0][0]


"""Поиск количества простых чисел"""


def is_prime1(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def count_primes1(number):
    """ через перебор делителей, O(N^2) """
    count = 0
    for num in range(2, number+1):
        if is_prime1(num):
            count += 1
    return count


def is_prime2(number):
    i = 2
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    number_sqrt = number**0.5
    while i <= number_sqrt:
        if number % i == 0:
            return False
        i += 1
    return True


def count_primes2(number):
    """ с оптимизациями поиска O(N * Sqrt(N)) """
    count = 0
    for num in range(2, number+1):
        if is_prime2(num):
            count += 1
    return count


def count_primes(number):
    """ с оптимизациями поиска и делением только на простые числа O(N * Sqrt(N) / Ln (N)) """
    def is_prime(number):
        i = 0
        number_sqrt = number**0.5
        while primes[i] <= number_sqrt:
            if number % primes[i] == 0:
                return False
            i += 1
        return True
    count = 0 if number == 1 else 1
    primes = [2]
    num = 3
    while num <= number:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1
    return count
