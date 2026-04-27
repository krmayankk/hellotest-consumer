"""Billing module — consumes compute_total from hellotest/src/utils.py.

This service calls compute_total(price, quantity, tax_rate, discount)
to calculate line items for invoices.
"""


def calculate_invoice_line(price, quantity, tax_rate, discount=0):
    """Calculate a single invoice line item.

    Uses the same compute_total(price, quantity, tax_rate, discount)
    signature from the shared utils library.
    """
    # In production this would import from the shared library
    # For now we replicate the call signature
    subtotal = price * quantity
    after_discount = subtotal - (subtotal * discount)
    return after_discount + (after_discount * tax_rate)


def generate_bill(items, tax_rate=0.08):
    """Generate a bill from a list of items."""
    total = 0
    lines = []
    for item in items:
        amount = calculate_invoice_line(
            item["price"], item["quantity"], tax_rate, item.get("discount", 0)
        )
        lines.append(f"{item['name']}: ${amount:.2f}")
        total += amount
    lines.append(f"Total: ${total:.2f}")
    return "\n".join(lines)
