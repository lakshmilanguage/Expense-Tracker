expenses = []

while True:

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        category = input("Enter Category: ")

        amount = float(
            input("Enter Amount: ")
        )

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense Added Successfully")

    elif choice == "2":

        if len(expenses) == 0:

            print("No Expenses Found")

        else:

            print("\nExpenses:")

            for i in range(len(expenses)):

                print(
                    i + 1,
                    expenses[i]["category"],
                    expenses[i]["amount"]
                )

    elif choice == "3":

        total = 0

        for expense in expenses:

            total += expense["amount"]

        print("Total Expense =", total)

    elif choice == "4":

        if len(expenses) == 0:

            print("No Expenses Available")

        else:

            expense_no = int(
                input("Enter Expense Number: ")
            )

            expenses.pop(expense_no - 1)

            print("Expense Deleted")

    elif choice == "5":

        print("Thank You")

        break

    else:

        print("Invalid Choice")