from datetime import datetime

date_format = "%d-%m-%Y"
categories = {"I": "Income", "E" : "Expense"}

# different functions for the tracker

def get_date(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:  # if user didnt gave any input
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format, Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)  # recursive func till we get actual date

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()      

def get_category():
    category = input("Enter the category ('I' for Income, 'E' for Expense): ").upper()
    if category in categories:
        return categories[category]
    print("Invalid category, Please enter again: ")
    return get_category()

def get_description():
    return input("Enter a description(optional): ")