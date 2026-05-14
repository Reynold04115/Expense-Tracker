# 🎓 ANNOTATED VERSION - Learn by Reading
# PROJECT 1: PERSONAL EXPENSE TRACKER

"""
This tracker teaches you how to handle NUMBERS (floats), 
how to SUM things up, and how to FILTER data by categories.
"""

import json  # Built-in library for working with .json files
import os    # Built-in library for working with files/folders
from datetime import datetime  # Library for working with dates and times

# ==============================================================================
# PART 1: FILE HANDLING - SAVING & LOADING DATA
# ==============================================================================

DATA_FILE = "expenses_data.json"

def load_expenses():
    """
    Reads the saved expenses.
    Notice we return an empty LIST [] instead of an empty dictionary {} this time.
    Why? Because expenses are a sequence of events, not unique named items.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
            
    return []  # Return an empty list if no file exists yet


def save_expenses(expenses):
    """Saves the list of expenses to our JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=2)


# ==============================================================================
# PART 2: DISPLAYING THE MENU
# ==============================================================================

def display_menu():
    print("\n" + "=" * 50)
    print("💰 PERSONAL EXPENSE TRACKER")
    print("=" * 50)
    print("1️⃣  Add a new expense")
    print("2️⃣  View ALL expenses & Total Balance")
    print("3️⃣  View expenses by Category (Filtering)")
    print("4️⃣  Exit")
    print("=" * 50)


# ==============================================================================
# PART 3: ADDING AN EXPENSE - MATH & ERROR CATCHING
# ==============================================================================

def add_expense(expenses):
    """
    This function lets the user log money they spent.
    NEW CONCEPT: Using float() for decimals and try/except for math errors!
    """
    
    print("\n--- 📝 Log an Expense ---")
    description = input("What did you buy? (e.g., Coffee, Gas): ").strip()
    category = input("What category? (e.g., Food, Transport): ").strip().title() # .title() capitalizes it
    
    # We use a 'while True' loop just for the amount. 
    # It keeps asking until they type a real number!
    while True:
        amount_input = input("How much did it cost? $").strip()
        try:
            # float() converts text like "5.50" into a decimal number we can do math with
            amount = float(amount_input) 
            break  # If successful, break out of this mini-loop!
        except ValueError:
            print("❌ Please enter a valid number (e.g., 15.99). No letters!")

    # Create a dictionary for this ONE specific expense
    new_expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "category": category,
        "amount": amount
    }
    
    # Add it to our master list and save
    expenses.append(new_expense) # .append() adds an item to the end of a list
    save_expenses(expenses)
    
    # The :.2f ensures it prints like $5.50 instead of $5.5
    print(f"✅ Added: {description} for ${amount:.2f} in {category}!")


# ==============================================================================
# PART 4: VIEWING ALL EXPENSES - SUMMING NUMBERS
# ==============================================================================

def view_all_expenses(expenses):
    """
    Loops through the list, prints each item, and adds up the total.
    """
    if not expenses:
        print("❌ No expenses logged yet!")
        return

    print("\n--- 🧾 ALL EXPENSES ---")
    
    total_spent = 0.0  # We start our counter at zero
    
    # Loop through our list of dictionaries
    for i, exp in enumerate(expenses, 1):
        # We access dictionary values using their keys (e.g., exp["description"])
        print(f" {i}. [{exp['date']}] {exp['description']} - ${exp['amount']:.2f} ({exp['category']})")
        
        # Add this expense's amount to our running total
        # += is a shortcut for: total_spent = total_spent + exp['amount']
        total_spent += exp["amount"]
        
    print("-" * 30)
    print(f"💸 TOTAL SPENT: ${total_spent:.2f}")


# ==============================================================================
# PART 5: VIEWING BY CATEGORY - FILTERING DATA
# ==============================================================================

def view_by_category(expenses):
    """
    NEW CONCEPT: Filtering! We only show and add up expenses 
    if they match the category the user asks for.
    """
    if not expenses:
        print("❌ No expenses logged yet!")
        return

    # First, let's find out what categories actually exist
    # We use a 'set' because sets automatically remove duplicates!
    unique_categories = set()
    for exp in expenses:
        unique_categories.add(exp["category"])
        
    print(f"\n📂 Available Categories: {', '.join(unique_categories)}")
    
    # Ask the user what they want to see
    chosen_category = input("Enter category to view: ").strip().title()
    
    print(f"\n--- 🧾 EXPENSES FOR: {chosen_category.upper()} ---")
    
    category_total = 0.0
    found_any = False
    
    # Loop through all expenses again
    for exp in expenses:
        # Check if the category matches what they typed
        if exp["category"] == chosen_category:
            print(f" - {exp['date']}: {exp['description']} (${exp['amount']:.2f})")
            category_total += exp["amount"]
            found_any = True
            
    if not found_any:
        print(f"❌ No expenses found in '{chosen_category}'.")
    else:
        print("-" * 30)
        print(f"💸 TOTAL IN {chosen_category.upper()}: ${category_total:.2f}")


# ==============================================================================
# PART 6: THE MAIN LOOP
# ==============================================================================

def main():
    print("🚀 Welcome to Personal Expense Tracker!")
    
    while True:
        expenses = load_expenses()
        display_menu()
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            print("\n👋 Keep an eye on your budget! See you next time! 💵")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()