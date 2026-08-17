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
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense('amount')
    return total
while True:
    print('\n===== EXPENSE TRACKER =====')
    print('1. Add Expense')
    print('2. Display Expenses')
    print('3. Total Spending')
    print('4. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        get_expense()

    elif choice == '2':
        display_expenses(expenses_list)

    elif choice == '3':
     total = calculate_total(expenses_list)
     print('Total Spending:', total)

    elif choice == '4':
        print("okay Goodbye!")
        break    

    else:
        print('Invalid choice. Please choose 1, 2, or 3.')