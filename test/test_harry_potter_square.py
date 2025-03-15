import pytest
from ..harry_potter_square.harry_potter_square import spell_data, harry_potter_square
from .extract_results import get_harry_potter_results

harry_potter_results = get_harry_potter_results()


@pytest.mark.harry
@pytest.mark.parametrize("value,expected", harry_potter_results)
def test_harry_potter_square(value, expected):
    result = harry_potter_square(spell_data()[value])
    assert result == expected
