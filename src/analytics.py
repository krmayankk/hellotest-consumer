"""Analytics module — also uses compute_total for revenue calculations."""


def revenue_by_category(orders):
    """Calculate revenue per category using compute_total logic.

    Expects compute_total(price, quantity, tax_rate, discount) signature.
    """
    categories = {}
    for order in orders:
        for item in order["items"]:
            cat = item.get("category", "other")
            # Uses same signature: compute_total(price, quantity, tax_rate, discount)
            subtotal = item["price"] * item["quantity"]
            after_discount = subtotal - (subtotal * item.get("discount", 0))
            amount = after_discount + (after_discount * item.get("tax_rate", 0))
            categories[cat] = categories.get(cat, 0) + amount
    return categories
