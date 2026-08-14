print('Welcome to Expense Tracker')


def add_expense(name, amount, category):
    expense = {
        'name': name,
        'amount': amount,
        'category': category
    }
    return expense


def display_expenses(expenses):
    print('\nExpenses:')
    
    for expense in expenses:
        print(
            f"Name: {expense['name']}, "
            f"Amount: {expense['amount']}, "
            f"Category: {expense['category']}"
        )


expenses_list = []


def get_expense():
    expense_name = input('Enter your expense name: ')
    print('Your expense name:', expense_name)

    amount = float(input('Enter the amount spent: '))
    print('Amount spent:', amount)

    category = input(
        'Enter the category of the expense '
        '(e.g., Food, Transport, Entertainment): '
    )
    print('Expense category:', category)

    expense = add_expense(expense_name, amount, category)

    expenses_list.append(expense)

    print('Expense added:', expense)


# Add the first expense
get_expense()


# Ask if the user wants to add more expenses
while True:
    choice = input(
        'Do you want to add another expense? (yes/no): '
    )

    if choice == 'yes':
        get_expense()
    else:
        break


# Display all expenses at the end
display_expenses(expenses_list)