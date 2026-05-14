# 💰 Personal Expense Tracker: CLI Budgeting App

A lightweight, functional Command Line Interface (CLI) application built in Python to help track daily spending. This project focuses on handling lists of complex data, performing mathematical operations, and filtering information dynamically.

## ✨ Features

- **Log Expenses:** Quickly add new expenses with a description, category, and precise dollar amount.
- **Dynamic Totals:** Automatically calculates and displays your total overall spending.
- **Category Filtering:** Sort and view your expenses by specific categories (e.g., "Food", "Transport", "Entertainment") to see exactly where your money is going.
- **Input Validation:** Prevents crashes by ensuring users enter valid numbers (decimals) when logging costs.
- **Data Persistence:** All logged expenses are safely stored in a local JSON file, so your data is never lost when the program closes.

## 🧠 What I Learned

Building this project reinforced several core Python concepts:

* **Lists of Dictionaries:** Storing multiple events (expenses) by appending individual dictionaries to a master list.
* **Type Conversion & Math:** Using `float()` to convert text input into decimal numbers, and using the `+=` operator to calculate running totals.
* **Data Filtering:** Iterating through a list to pull out specific data points based on user conditions (e.g., matching a category string).
* **Using Sets:** Utilizing Python's `set()` data structure to automatically filter out duplicate categories and display a clean menu of available categories to the user.
* **Error Catching:** Implementing `try/except ValueError` blocks to catch typos and prevent the program from crashing if a user types a letter instead of a number.

## 🚀 How to Run the App

### Prerequisites
You need Python 3.x installed on your computer. No external libraries or frameworks are required!

### Instructions
1. Clone this repository or download the files.
2. Open your terminal or command prompt.
3. Navigate to the folder where the file is located.
4. Run the script using Python:

```bash
python expense_tracker.py
