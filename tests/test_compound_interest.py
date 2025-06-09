import pytest
from compound_interest import compound_interest


def test_compound_interest_basic():
    result = compound_interest(1000, 2, 5)
    assert result == pytest.approx(102.5)
