"""Pricing rules for the sample shop."""


def apply_discount(price_cents: int, percent: int) -> int:
    """Return the price after a percentage discount (0-100), rounded down."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return price_cents - (price_cents * percent) // 100


def is_free(price_cents: int) -> bool:
    return price_cents <= 0


def bulk_price(unit_cents: int, quantity: int) -> int:
    """Price for a quantity; 10-49 items get 10% off, 50+ get 20% off."""
    total = unit_cents * quantity
    if quantity >= 50:
        total = apply_discount(total, 20)
    elif quantity >= 10:
        total = apply_discount(total, 10)
    return total


def shipping_cents(order_total_cents: int) -> int:
    """Shipping fee: free for orders of 5000 cents or more, else flat 499."""
    if order_total_cents < 0:
        raise ValueError("order total must not be negative")
    if order_total_cents >= 5000:
        return 0
    return 499
