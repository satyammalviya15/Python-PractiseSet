from functools import reduce
from datetime import datetime
import time

# ----- Decorator to log function run time -----
def log_run_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"\nExecuting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Completed in {time.time() - start:.4f} seconds\n")
        return result
    return wrapper

# ----- Sample expense data -----
expenses = [
    {"amount": 250, "category": "Groceries", "date": "2025-05-01"},
    {"amount": 120, "category": "Transport", "date": "2025-05-02"},
    {"amount": 300, "category": "Rent", "date": "2025-05-01"},
    {"amount": 75,  "category": "Entertainment", "date": "2025-05-03"},
    {"amount": 50,  "category": "Transport", "date": "2025-05-03"},
    {"amount": 100, "category": "Groceries", "date": "2025-05-04"},
]

# ----- Generator for expenses -----
def expense_generator(expense_list):
    for exp in expense_list:
        yield exp

# ----- Filter expenses by category -----
def filter_by_category(expenses, category):
    return list(filter(lambda e: e['category'].lower() == category.lower(), expenses))

# ----- Map to extract amounts -----
def get_amounts(expenses):
    return list(map(lambda e: e['amount'], expenses))

# ----- Reduce to get total -----
def total_expense(amounts):
    return reduce(lambda a, b: a + b, amounts, 0)

# ----- Main processor -----
@log_run_time
def summarize_expenses(expense_list, category=None):
    gen = expense_generator(expense_list)
    filtered = filter_by_category(gen, category) if category else list(gen)
    amounts = get_amounts(filtered)
    total = total_expense(amounts)
    print(f"Category: {category or 'All'} | Total Expenses: ${total}")
    print("Details:")
    for item in filtered:
        print(f"- {item['date']} | {item['category']} | ${item['amount']}")

# ----- Test calls -----
summarize_expenses(expenses)
summarize_expenses(expenses, "Transport")
summarize_expenses(expenses, "Groceries")