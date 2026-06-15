# Personal Finance Tracker

A comprehensive **Python-based Personal Finance Tracker** that helps users manage expenses, categorize spending, track budgets, and generate financial reports.

---

#  Project Description

The Personal Finance Tracker is a command-line application that helps users manage daily expenses efficiently. It allows storing financial data, categorizing spending, analyzing trends, and exporting reports.

This project demonstrates:
- Object-Oriented Programming (OOP)
- File Handling (JSON, CSV)
- Modular Python design
- Data validation and error handling
- Reporting and analytics

---

#  Features

- Add new expenses with validation
- Edit and delete expenses
- Categorize expenses (Food, Transport, Bills, Entertainment, etc.)
- Save data in JSON format
- Automatic load on startup
- Monthly expense reports
- Category-wise breakdown
- Budget tracking system
- Export data to CSV
- Search and filter expenses
- Backup and restore system
- Simple CLI menu interface

---

#  Project Structure
week4-finance-tracker/
│
├── finance_tracker/
│ ├── init.py
│ ├── main.py
│ ├── expense.py
│ ├── expense_manager.py
│ ├── file_handler.py
│ ├── reports.py
│ └── utils.py
│
├── data/
│ ├── expenses.json
│ ├── backup/
│ └── exports/
│
├── tests/
│ ├── test_expense.py
│ ├── test_file_handler.py
│ └── test_reports.py
│
├── run.py
├── requirements.txt
├── README.md
├── .gitignore


---

# ⚙️ How to Run

```bash
cd week4-finance-tracker
python run.py

Setup Instructions
Install Python 3.8+
Clone or download project
Keep folder structure unchanged
Run run.py
Data files are auto-created inside data/

Code Structure Overview
main.py → CLI menu system
expense.py → Expense class + validation
expense_manager.py → Add/search/delete logic
file_handler.py → JSON & CSV handling
reports.py → Analytics & reports
utils.py → Helper functions

 Architecture Flow
User Input → Main Menu → Expense Manager → File Handler → Reports

Testing

This project uses pytest.

Run tests:
pytest
Test coverage:
Expense validation
File read/write
Report calculations
Category breakdown logic

Example Output
PERSONAL FINANCE TRACKER
========================================
1. Add New Expense
2. View All Expenses
3. Search Expenses
4. Generate Monthly Report
5. Category Breakdown
6. Set Budget
7. Export CSV
8. Statistics
0. Exit


Technical Details
Data Structures:
List → store expenses
Dictionary → each expense record
JSON → persistent storage
Concepts Used:
Object-Oriented Programming (OOP)
File Handling
Exception Handling
Data Aggregation
Modular Programming

Error Handling

Handles:

Invalid inputs
Missing files
Empty datasets
File permission issues

 Export Features
CSV export for Excel
JSON backup system
Auto folder creation for exports


