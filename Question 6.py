**Question 6: Basic Loops**

**For loop**

#Print numbers from 1 to 20
for i in range(1, 21):
    print(i)

#Multiplication table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

#Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total = total + i
print(f"Sum of numbers from 1 to 100: {total}")

#Even numbers between 1 and 50
for i in range(2, 51, 2):
    print(i)

#Fruits list with position
fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

**While loop**

#Print numbers from 10 down to 1
i = 10
while i >= 1:
    print(i)
    i = i - 1

#Sum of positive numbers until 0 or negative is entered
total = 0
while True:
    num = int(input("Enter a number: "))
    if num <= 0:
        break
    total = total + num
print(f"The total sum of all numbers: {total}")

#Countdown with Blast off
count = 10
while count >= 0:
    if count == 0:
        print("Blast off!")
    else:
        print(count)
    count = count - 1

#First 10 multiples of 6
i = 1
while i <= 10:
    print(6 * i)
    i = i + 1
