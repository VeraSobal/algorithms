from pathlib import Path
from decimal import Decimal, getcontext


def list_results(test_results_folder):
    folder = Path("test")/Path(test_results_folder)
    cur_dir = Path.cwd()
    test_path = cur_dir/folder
    dict_results = {}
    for item in test_path.iterdir():
        try:
            with item.open("r", encoding="UTF-8") as f:
                key = item.stem.split(".")[1]
                value = f.read()
                if dict_results.get(key):
                    dict_results[key][item.suffix[1:]] = value
                else:
                    dict_results[key] = {item.suffix[1:]: value}
        except:
            continue
    list_results = [(x["in"], x["out"]) for x in list(dict_results.values())]
    return list_results

def get_harry_potter_results():
    return list_results("harry_potter")

def get_lucky_ticket_results():
    result = []
    for item in list_results("lucky_ticket"):
        value_str, expected_str = item
        value = int(value_str)
        expected = int(expected_str)
        result.append((value, expected))
    return result


def get_power_results():
    result = []
    for item in list_results("power_fibo_prime/power"):
        value_str, expected_str = item
        str_number, str_power, *_ = value_str.split("\n")
        value = (Decimal(str_number), int(str_power))
        expected = Decimal(expected_str)
        result.append((value, expected))
    return result


def get_fibo_results():
    result = []
    getcontext().prec = 2500000
    for item in list_results("power_fibo_prime/fibo"):
        value_str, expected_str = item
        value = int(value_str)
        expected = Decimal(expected_str)
        result.append((value, expected))
    return result


def get_prime_results():
    result = []
    for item in list_results("power_fibo_prime/primes"):
        value_str, expected_str = item
        value = int(value_str)
        expected = int(expected_str)
        result.append((value, expected))
    return result