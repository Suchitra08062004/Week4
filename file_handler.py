import json
import os
import csv


def load_data(file_path):
    if not os.path.exists(file_path):
        return {"expenses": [], "budget": 0}

    with open(file_path, "r") as f:
        return json.load(f)


def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)



import csv
import os


def export_csv(file_path, expenses):
    # 👉 create folder automatically
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Date", "Amount", "Category", "Description"])

        for e in expenses:
            writer.writerow([
                e["date"],
                e["amount"],
                e["category"],
                e["description"]
            ])