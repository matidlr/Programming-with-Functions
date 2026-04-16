import unittest
import os
from budget_tracker import (
    read_expenses,
    calculate_total,
    calculate_category_totals,
    calculate_average
)

class TestBudgetTracker(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_expenses.csv"

        with open(self.test_file, "w") as f:
            f.write("2024-01-01,Lunch,Food,10.5\n")
            f.write("2024-01-02,Bus,Transport,2.5\n")
            f.write("2024-01-03,Dinner,Food,20\n")
            f.write("bad,row\n")  # inválida

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_expenses(self):
        expenses = read_expenses(self.test_file)

        self.assertEqual(len(expenses), 3)
        self.assertEqual(expenses[0]["description"], "Lunch")
        self.assertEqual(expenses[0]["category"], "Food")
        self.assertEqual(expenses[0]["amount"], 10.5)

    def test_calculate_total(self):
        expenses = [
            {"amount": 10},
            {"amount": 20},
            {"amount": 5}
        ]
        self.assertEqual(calculate_total(expenses), 35)

    def test_category_totals(self):
        expenses = [
            {"category": "Food", "amount": 10},
            {"category": "Food", "amount": 5},
            {"category": "Transport", "amount": 3}
        ]

        result = calculate_category_totals(expenses)

        self.assertEqual(result["Food"], 15)
        self.assertEqual(result["Transport"], 3)

    def test_average(self):
        expenses = [
            {"amount": 10},
            {"amount": 20}
        ]
        self.assertEqual(calculate_average(expenses), 15)

    def test_average_empty(self):
        self.assertEqual(calculate_average([]), 0)

    def test_file_not_found(self):
        expenses = read_expenses("archivo_inexistente.csv")
        self.assertEqual(expenses, [])


if __name__ == "__main__":
    unittest.main()