import pytest

from ..power_fibo_prime.power_fibo_prime import (
    iter_power,
    recurs_power,
    recurs_fibo,
    iter_fibo,
    matrix_fibo,
    golden_fibo,
    count_primes1,
    count_primes2,
    count_primes,
)
from .extract_results import (
    get_power_results,
    get_prime_results,
    get_fibo_results,
)

TIMEOUT=120
power_results = get_power_results()
prime_results = get_prime_results()
fibo_results = get_fibo_results()


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.power
@pytest.mark.parametrize("value,expected",
                         power_results)
def test_iter_power(value, expected):
    number, power = value
    result = iter_power(number, power)
    assert round(result, 11) == expected


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.power
@pytest.mark.parametrize("value,expected",
                         power_results)
def test_recurs_power(value, expected):
    number, power = value
    result = recurs_power(number, power)
    assert round(result, 11) == expected


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.fibo
@pytest.mark.parametrize("value,expected",
                         fibo_results)
def test_recurs_fibo(value, expected):
    result = recurs_fibo(value)
    assert result == expected


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.fibo
@pytest.mark.parametrize("value,expected",
                         fibo_results)
def test_iter_fibo(value, expected):
    result = iter_fibo(value)
    assert result == expected


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.fibo
@pytest.mark.parametrize("value,expected",
                         fibo_results)
def test_matrix_fibo(value, expected):
    result = matrix_fibo(value)
    assert result == expected


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.fibo
@pytest.mark.parametrize("value,expected",
                         fibo_results)
def test_golden_fibo(value, expected):
    result = golden_fibo(value)
    assert result == expected


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.prime
@pytest.mark.parametrize("value,expected",
                         prime_results)
def test_count_primes1(value, expected):
    result = count_primes1(value)
    assert result == expected


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.prime
@pytest.mark.parametrize("value,expected",
                         prime_results)
def test_count_primes2(value, expected):
    result = count_primes2(value)
    assert result == expected


@pytest.mark.timeout(timeout=TIMEOUT)
@pytest.mark.prime
@pytest.mark.parametrize("value,expected",
                         prime_results)
def test_count_primes(value, expected):
    result = count_primes(value)
    assert result == expected
