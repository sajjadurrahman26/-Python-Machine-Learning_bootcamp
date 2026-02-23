**Question 4: Conditional Statements  Intermediate**

# Age Checker
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age > 18:
    print("You are an adult")
elif 13 <= age <= 17:
    print("You are a teenager")
else:
    print("You are a child")

#Even / Odd using a ternary operator in a single line:
num = int(input("Enter a number: "))
print("This is an even number" if num % 2 == 0  else "This is an odd number")

#Grade Calculator
mark=int(input("Enter your mark:"))

if mark < 0 or mark > 100:
  result="Invalid mark"
elif mark >= 90 and mark <= 100:
  result="A+"
elif mark >= 80 and mark <= 89:
  result="A"
elif mark >= 70 and mark <= 79:
  result="B"
elif mark >= 60 and mark <= 69:
  result="C"
elif mark >= 50 and mark <= 59:
  result="D"
else:
  result="F __Failed"

print(f"Your grade is {result}")


# Login System
correct_username = "admin"
correct_password = "1234"

attempts = 0
max_attempts = 3 #counter

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print(f"Login successful! Welcome, {username}.")
        break
    elif username == correct_username and password != correct_password:
        print("Incorrect password. Try again.")
    else:
        print("User not found.")

    attempts = attempts+1

if attempts == max_attempts:
    print("Account locked.")

