import json
import os
from Finance_tracker.file_handler import save_data, load_data


TEST_FILE = "test_data.json"


def test_save_and_load():
    data = {
        "expenses": [
            {
                "date": "2026-06-15",
                "amount": 500,
                "category": "Food",
                "description": "Lunch"
            }
        ],
        "budget": 1000
    }

    save_data(TEST_FILE, data)

    loaded = load_data(TEST_FILE)

    assert loaded["budget"] == 1000
    assert len(loaded["expenses"]) == 1

    os.remove(TEST_FILE)