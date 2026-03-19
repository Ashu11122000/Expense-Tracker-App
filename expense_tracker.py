# Import the Expense class from expense.py file
# This allows us to create Expense objects in this program
from expense import Expense

# Import calendar module (used to get number of days in a month)
import calendar

# Import datetime module (used to get current date and time)
import datetime


# Main function (this is where the program starts running)
def main():
    
    # Print message showing program has started
    print(f"🎯 Running Expense Tracker!")
    
    # File name where expenses will be saved
    expense_file_path = "expenses.csv"
    
    # Monthly budget limit set to 2000
    budget = 2000                       

    # Call function to get expense details from user
    expense = get_user_expense()

    # Save the entered expense into the CSV file
    save_expense_to_file(expense, expense_file_path)

    # Read saved expenses and display summary
    summarize_expenses(expense_file_path, budget)


# Function to collect expense details from user
def get_user_expense():
    
    # Print message indicating expense input process started
    print(f"🎯 Getting User Expense")
    
    # Ask user to enter expense name
    expense_name = input("Enter expense name: ")
    
    # Ask user to enter expense amount and convert it to float (decimal number)
    expense_amount = float(input("Enter expense amount: "))

    # List of predefined categories
    expense_categories = [
        "Food",   # Category 1
        "Home",   # Category 2
        "Work",   # Category 3
        "Fun",    # Category 4
        "Misc",   # Category 5: Miscellaneous
    ]

    # Loop runs until user selects valid category
    while True:
        
        # Ask user to select category
        print("Select a category: ")
        
        # Display category options with numbering
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        # Show valid number range
        value_range = f"[1 - {len(expense_categories)}]"
        
        # Take user input and subtract 1 (because list index starts from 0)
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        # Check if selected number is valid
        if selected_index in range(len(expense_categories)):
            
            # Get selected category name
            selected_category = expense_categories[selected_index]
            
            # Create a new Expense object using user input
            new_expense = Expense(
                name=expense_name,           # Set expense name
                category=selected_category,  # Set expense category
                amount=expense_amount        # Set expense amount
            )
            
            # Return the created Expense object
            return new_expense
        
        else:
            # If invalid number entered, show error message
            print("Invalid category. Please try again!")


# Function to save expense into file
def save_expense_to_file(expense: Expense, expense_file_path):
    
    # Print confirmation message
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    
    # Open file in append mode ("a") → adds new data without deleting old data
    with open(expense_file_path, "a") as f:
        
        # Write expense data in CSV format (comma separated)
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


# Function to read expenses and display summary
def summarize_expenses(expense_file_path, budget):
    
    # Print message indicating summary process started
    print(f"🎯 Summarizing User Expense")
    
    # Create empty list to store Expense objects
    expenses: list[Expense] = []

    # Open file in read mode ("r")
    with open(expense_file_path, "r") as f:
        
        # Read all lines from file
        lines = f.readlines()

        # Loop through each line in file
        for line in lines:
            
            # Remove newline and split values by comma
            expense_name, expense_amount, expense_category = line.strip().split(",")

            # Create Expense object from file data
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),   # Convert amount to float
                category=expense_category,
            )
            
            # Add object to expenses list
            expenses.append(line_expense)

    # Dictionary to store total amount per category
    amount_by_category = {}

    # Loop through each expense object
    for expense in expenses:
        
        # Get category of expense
        key = expense.category

        # If category already exists in dictionary, add amount
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            # If category not exists, create new entry
            amount_by_category[key] = expense.amount

    # Print expenses grouped by category
    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    # Calculate total spent by summing all expense amounts
    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")

    # Calculate remaining budget
    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    # Get current date and time
    now = datetime.datetime.now()

    # Get total number of days in current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate remaining days in month
    remaining_days = days_in_month - now.day

    # Calculate daily budget for remaining days
    daily_budget = remaining_budget / remaining_days

    # Print daily budget in green color
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))


# Function to print text in green color in terminal
def green(text):
    
    # \033[92m makes text green
    # \033[0m resets text color back to normal
    return f"\033[92m{text}\033[0m"


# This ensures main() runs only if this file is executed directly
# It prevents automatic execution if file is imported elsewhere
if __name__ == "__main__":
    main()