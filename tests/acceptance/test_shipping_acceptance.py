import pytest

import shop.pricing as pricing


def _ship(n):
    return pricing.shipping_cents(n)


@pytest.mark.parametrize(
    "total,expected",
    [(0, 499), (1, 499), (4999, 499), (5000, 0), (5001, 0), (1_000_000, 0)],
)
def test_shipping_fee_rule(total, expected):
    result = _ship(total)
    assert result == expected
    assert type(result) is int


@pytest.mark.parametrize("total", [-1, -5000])
def test_negative_total_raises(total):
    with pytest.raises(ValueError):
        _ship(total)


def test_pure_repeatable():
    assert _ship(100) == _ship(100) == 499
