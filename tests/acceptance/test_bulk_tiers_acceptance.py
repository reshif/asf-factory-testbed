"""Acceptance: tiered bulk discount at 9, 10, 49, 50."""
import pytest

from shop.pricing import bulk_price


@pytest.mark.parametrize(
    "quantity,percent",
    [(9, 0), (10, 10), (49, 10), (50, 20), (51, 20), (100, 20)],
)
def test_bulk_tier_boundaries(quantity, percent):
    assert bulk_price(100, quantity) == 100 * quantity * (100 - percent) // 100


def test_fifty_item_total_is_base_minus_twenty_percent():
    base = 250 * 50
    assert bulk_price(250, 50) == base - base * 20 // 100
