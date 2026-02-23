**Question 1: Variables and Data Types**

#(a) Declare the following variables and print their data types using type():
name = "Sajjadur Rahman"
age = 24
gpa = 3.75
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# type conversions and print the results:
# String to integer
num_str = "123"
num_int = int(num_str)
print(num_int)

# Integer to string
num = 456
num_str2 = str(num)
print(num_str2)

# Float to integer
float_num = 3.99
int_num = int(float_num)
print(int_num)
# Explanation: The decimal part is truncated (not rounded)

# Integers to boolean
print(bool(1))  # True
print(bool(0))  # False
