# BANK module
class Customer:
    def __init__(self, name, account_number, balance_amount):
        self.name = name
        self.account_number = account_number
        self.balance_amount = balance_amount

def create_customer_list(n):
    customer_list = []
    for i in range(n):
        name = input("Enter the customer name: ")
        account_number = input("Enter the customer account number: ")
        balance_amount = float(input("Enter the customer balance amount: "))
        customer = Customer(name, account_number, balance_amount)
        customer_list.append(customer)
    return customer_list

# TRANSACTION module
def credit(customer_list, account_number, deposit_amount):
    for customer in customer_list:
        if customer.account_number == account_number:
            customer.balance_amount += deposit_amount
            break
    print("Deposit operation successful.")

def debit(customer_list, account_number, debit_amount):
    for customer in customer_list:
        if customer.account_number == account_number:
            if customer.balance_amount >= debit_amount:
                customer.balance_amount -= debit_amount
                print("Withdraw operation successful.")
            else:
                print("Insufficient funds.")
            break

def order_by_balance(customer_list):
    for i in range(len(customer_list) - 1):
        for j in range(i + 1, len(customer_list)):
            if customer_list[i].balance_amount > customer_list[j].balance_amount:
                customer_list[i], customer_list[j] = customer_list[j], customer_list[i]

# MAIN program
customer_list = create_customer_list(int(input("Enter the number of customers: ")))

# Perform bank transaction operations
print("Choose an operation:")
print("1. Credit")
print("2. Debit")
print("3. Order customer list by balance")
choice = int(input("Enter your choice: "))

if choice == 1:
    account_number = input("Enter the account number to credit: ")
    deposit_amount = float(input("Enter the deposit amount: "))
    credit(customer_list, account_number, deposit_amount)
elif choice == 2:
    account_number = input("Enter the account number to debit: ")
    debit_amount = float(input("Enter the debit amount: "))
    debit(customer_list, account_number, debit_amount)
elif choice == 3:
    order_by_balance(customer_list)
    print("Customer list ordered by balance:")
    for customer in customer_list:
        print(customer.name, customer.account_number, customer.balance_amount)
else:
    print("Invalid choice.")
