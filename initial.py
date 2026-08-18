import csv
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

def category_spending(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense['category']
        amount = expense['amount']

        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount

    print('\nSpending by Category:')

    for category, total in category_totals.items():
        print(f'{category}: Rs. {total}')


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense['amount']
    return total

def delete_expense(expenses):
    if not expenses:
        print('\nThere are no expenses to delete.')
        return

    print('\nExpenses:')

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} - "
            f"Rs. {expense['amount']} - "
            f"{expense['category']}"
        )

    choice = int(input('Enter expense number to delete: '))

    if 1 <= choice <= len(expenses):
        deleted_expense = expenses.pop(choice - 1)
        print(f"Deleted: {deleted_expense['name']}")
    else:
        print('Invalid expense number.')

def save_expenses_to_csv(expenses, filename='expenses.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(
            file,
            fieldnames=['name', 'amount', 'category']
        )
        writer.writeheader()
        writer.writerows(expenses)

    print('CSV file saved successfully!')
    print('File location:', filename)

while True:
    print('\n===== EXPENSE TRACKER =====')
    print('1. Add Expense')
    print('2. Display Expenses')
    print('3. Total Spending')
    print('4. Spending by Category')
    print('5. Delete Expense')
    print('6. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        get_expense()

    elif choice == '2':
        display_expenses(expenses_list)

    elif choice == '3':
        total = calculate_total(expenses_list)
        print('Total Spending:', total)

    elif choice == '4':
        category_spending(expenses_list)

    elif choice == '5':
        delete_expense(expenses_list)

    elif choice == '6':
        save_expenses_to_csv(expenses_list)
        print('Expenses saved. Goodbye!')
        break

    else:
        print('Invalid choice. Please choose 1, 2, 3, 4, 5, or 6.')