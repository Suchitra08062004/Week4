from datetime import datetime


class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
        }

    @staticmethod
    def validate(date, amount, category):
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return False

        return amount > 0 and category.strip() != ""