# Basic Expense Tracker Application

A simple command-line based Expense Tracker built using basic Python concepts such as functions, lists, file handling, and user input.

This project allows users to:

1. Add expenses
2. Categorize spending
3. View summaries
4. Track budget usage

---

## Features

1. Add new expense records
2. Categorize expenses (Food, Home, Work, Fun, Misc)
3. Store data in a CSV file
4. View expense summary by category
5. Calculate total spending
6. Track remaining budget
7. Daily budget calculation based on remaining days

---

## Concepts Used

This project is built using basic Python only:

1. Variables
2. Functions
3. Lists & Dictionaries
4. File Handling (`.csv`)
5. Loops (`for`, `while`)
6. Conditional Statements (`if-else`)
7. User Input (`input()`)

---

## Project Structure

expense-tracker/
│
├── expense_tracker.py   # Main program
├── expense.py           # Expense class definition
├── expenses.csv         # Data storage file
└── images/              # (Optional) screenshots

---

## Setup Instructions

### 1. Install Python
Download and install Python from:
https://www.python.org/downloads/

Make sure to check:
-> Add Python to PATH

---

### 2. Clone Repository
git clone https://github.com/Ashu11122000/Expense-Tracker-App.git
cd Expense-Tracker-App

---

### 3. Run the Program
python expense_tracker.py

---

## How It Works
1. User enters:
   -> Expense name
   -> Amount
   -> Category

2. Expense is saved into: expenses.csv

3. Program:
   -> Reads all expenses
   -> Groups by category
   -> Calculates:
     -> Total spent
     -> Remaining budget
     -> Daily budget

---

## Example Output
Expenses By Category:
  Food: $500.00
  Work: $300.00
  Total Spent: $800.00
  Budget Remaining: $1200.00
  Budget Per Day: $40.00
```

---

## Future Improvements
1. Add menu-based navigation
2. Add delete/edit expense feature
3. Use JSON instead of CSV
4. Convert to FastAPI backend

---
