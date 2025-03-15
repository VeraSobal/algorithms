import pytest
from ..lucky_ticket.lucky_ticket import count_lucky_ticket

from .extract_results import get_lucky_ticket_results

lucky_ticket_results=get_lucky_ticket_results()

@pytest.mark.timeout(timeout=60)
@pytest.mark.lucky_ticket
@pytest.mark.parametrize("value,expected",
                         lucky_ticket_results)
def test_count_lucky_ticket(value, expected):
    result = count_lucky_ticket(value)
    assert result == expected
