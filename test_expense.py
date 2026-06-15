from Finance_tracker.expense import Expense


def test_valid_expense():
    assert Expense.validate("2026-06-15", 500, "Food") is True


def test_invalid_date():
    assert Expense.validate("2026-99-99", 500, "Food") is False


def test_invalid_amount():
    assert Expense.validate("2026-06-15", -100, "Food") is False


def test_empty_category():
    assert Expense.validate("2026-06-15", 100, "") is False