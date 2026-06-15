from Finance_tracker.reports import (
    monthly_report,
    category_report,
    stats
)


def sample_data():
    return [
        {
            "date": "2026-06-01",
            "amount": 100,
            "category": "Food",
            "description": "A"
        },
        {
            "date": "2026-06-02",
            "amount": 300,
            "category": "Travel",
            "description": "B"
        },
        {
            "date": "2026-07-01",
            "amount": 200,
            "category": "Food",
            "description": "C"
        }
    ]


def test_monthly_report():
    data = sample_data()
    assert monthly_report(data, "2026-06") == 400


def test_category_report():
    data = sample_data()
    result = category_report(data)

    assert result["Food"] == 300
    assert result["Travel"] == 300


def test_stats():
    data = sample_data()
    result = stats(data)

    assert result["total"] == 600
    assert result["avg"] == 200
    assert result["max"] == 300