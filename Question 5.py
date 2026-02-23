**Question 5: ATM Simulation**

#an ATM program with the following variables: pinNumber, balance, and request:
pinNumber = 1111
balance = 5000

pin = int(input("Enter your PIN: "))

if pin == pinNumber:
    request = int(input("Enter withdrawal amount: "))

    if request > 500 and request <= balance:
        balance = balance - request
        print("Withdrawal successful.")
        print(f"Remaining balance:{balance}")
    elif request > balance:
        print("Insufficient balance.")
    else:
        print("Withdrawal amount must be greater than 500.")
else:
    print("Wrong PIN.")

#an attempts counter
pinNumber = 1111
balance = 5000
attempts = 3 #counter

while attempts > 0:
    pin = int(input("Enter your PIN: "))

    if pin == pinNumber:
        request = int(input("Enter withdrawal amount: "))

        if request > 500 and request <= balance:
            balance = balance - request
            print("Withdrawal successful.")
            print(f"Remaining balance: {balance}")
        elif request > balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than 500.")
        break
    else:
        attempts = attempts - 1
        print(f"Wrong pin. Attempts remaining: {attempts}")

        if attempts == 0:
            print("Card blocked.")

#Login System before the ATM:
correct_username = "admin"
correct_password = "1234"

is_active = True #flag

username = input("Enter username: ")
password = input("Enter password: ")

if username=="admin" and password=="1234" and is_active:
  print("Login successful. Proceed to ATM pin check...")
else:
  print("Account is disabled.")
