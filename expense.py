# Define a class named Expense
class Expense:
    
    # Constructor method (called automatically when a new object is created)
    # It initializes the expense with name, category, and amount
    def __init__(self, name, category, amount) -> None:
        self.name = name          # Name of the expense (e.g., "Groceries")
        self.category = category  # Category of expense (e.g., "Food")
        self.amount = amount      # Amount spent (numeric value)

    # Special method that defines how the object is represented
    # This is used when you print the object or inspect it
    def __repr__(self):
        # Returns a formatted string showing expense details
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"