import pytest

from shop.pricing import apply_discount, bulk_price, is_free


def test_discount_basic():
    assert apply_discount(1000, 10) == 900


def test_discount_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(1000, 101)


def test_is_free():
    assert is_free(0) is True
    assert is_free(5) is False


def test_bulk_price():
    assert bulk_price(100, 10) == 900
    assert bulk_price(100, 2) == 200


def test_bulk_price_no_discount_below_10():
    assert bulk_price(100, 9) == 900


def test_bulk_price_ten_percent_tier():
    assert bulk_price(100, 10) == 900
    assert bulk_price(100, 49) == 4410


def test_bulk_price_twenty_percent_tier():
    assert bulk_price(100, 50) == 4000
    assert bulk_price(100, 100) == 8000


@pytest.mark.django_db
def test_product_str():
    from shop.models import Product

    assert str(Product.objects.create(name="pen", price_cents=3)) == "pen"
