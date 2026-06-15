def monthly_report(expenses, month):
    total = sum(
        e["amount"] for e in expenses
        if e["date"].startswith(month)
    )
    return total


def category_report(expenses):
    result = {}

    for e in expenses:
        result[e["category"]] = result.get(e["category"], 0) + e["amount"]

    return result


def stats(expenses):
    if not expenses:
        return {"total": 0, "avg": 0, "max": 0}

    total = sum(e["amount"] for e in expenses)

    return {
        "total": total,
        "avg": total / len(expenses),
        "max": max(e["amount"] for e in expenses),
    }