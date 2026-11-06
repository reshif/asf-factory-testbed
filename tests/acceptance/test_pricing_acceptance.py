"""Acceptance tests: the pricing behaviour the business relies on (synthetic testbed).

These are the oracle the factory locks (.factory/oracle-lock.json): agents may not edit them.
Change them only through a human-approved Test Change Request (E6).
Deliberately NOT locked: discounts for 50+ items, so new tiers can be added by features.
"""
import pytest

from shop.pricing import apply_discount, bulk_price, is_free


@pytest.mark.parametrize(
    "price,percent,expected",
    [(1000, 0, 1000), (1000, 10, 900), (1000, 100, 0), (999, 10, 900), (1, 50, 1)],
)
def test_discount_amount_is_rounded_down(price, percent, expected):
    assert apply_discount(price, percent) == expected


@pytest.mark.parametrize("percent", [-1, 101])
def test_discount_outside_0_to_100_is_rejected(percent):
    with pytest.raises(ValueError):
        apply_discount(1000, percent)


def test_zero_or_negative_price_is_free():
    assert is_free(0) and is_free(-5)
    assert not is_free(1)


@pytest.mark.parametrize("quantity", [1, 2, 9])
def test_under_ten_items_pay_full_price(quantity):
    assert bulk_price(100, quantity) == 100 * quantity


@pytest.mark.parametrize("quantity", [10, 25, 49])
def test_ten_to_forty_nine_items_get_exactly_ten_percent_off(quantity):
    assert bulk_price(100, quantity) == 100 * quantity * 90 // 100
