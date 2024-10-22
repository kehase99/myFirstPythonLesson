# 1. Define two variables, x and y, with values 5 and 10.
#    Perform the following operations and print the results:
#    a) Sum of x and y
#    b) Difference of y and x
#    c) Product of x and y
#    d) Quotient of y by x

x = 5
y = 10

Sum = x + y 
print(Sum)
diff = y - x
print(diff)
product = x * y 
print(product)
Quotient = y / x
print(Quotient)


# 2. Define a list of fruits containing "apple", "banana", and "cherry".
#    a) Add "orange" to the list.
#    b) Remove "banana" from the list.
#    c) Print the first and last elements of the list.

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print(fruits[0], fruits[-1])

# 3. Define a set of numbers containing 1, 2, 3, 4, and 5.
#    a) Add the number 6 to the set.
#    b) Remove the number 3 from the set.
#    c) Check if the numbers 5 and 7 are in the set, and print the results.

numbers_set = {1, 2, 3, 4, 5}
numbers_set.add(6)
numbers_set.remove(3)
if 5 and 7 in numbers_set:
    print("yes, 5 and 7 are a member of the group")
else:
    print("no, they are not")
"""
num5 = [5]
num7 = [7]
check5 = num5.issubset(numbers_set)
print(check5)
check7 = num7.issubset(numbers_set)
print(check7)
"""
# 4. Define a tuple representing coordinates (10.5, 20.7).
#    a) Print the x (first) and y (second) coordinates separately.

coordinates = (10.5, 20.7)
print(coordinates[0], coordinates[1])

# 5. Define a dictionary of student grades, where:
#    - "Alice" has a grade of 85
#    - "Bob" has a grade of 90
#    - "Charlie" has a grade of 78
#    a) Add a new student "David" with a grade of 88.
#    b) Update Alice's grade to 95.
#    c) Print Bob's grade.

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
#grades["David"] = 88 # it works or
grades.update({"David": 88})
print(grades)

# 6. Define a variable called `age` with a value of 18.
#    a) Write an if/else statement that checks if the age is 18 or above. 
#    If true, print "You are eligible to vote", otherwise print "You are not eligible to vote".

age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# 7. Define a list of fruits: ["apple", "orange", "grape"].
#    a) Use a `for` loop to print each fruit in the list.

fruits = ["apple", "orange", "grape"]

for i in fruits:
    print(i)
    #or
for i in range(0, len(fruits), 1):
    print(fruits[i])

# 8. Define a variable `count` with a value of 5.
#    a) Use a `while` loop to print a countdown from 5 to 1.

count = 5
while count > 0:
    print(count)
    count = count -1

# 9. Challenge: Combine lists, sets, dictionaries, and loops.
#    a) Define a list of numbers from 1 to 10.
#    b) Create a set of even numbers from the list using a `for` loop or comprehension.
#    c) Create a dictionary that maps each even number to its square.
#    d) Print the set of even numbers and the dictionary.
print("--------------------9b)----------------------------")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers=[]
for i in numbers:
   if i % 2 == 0:
    even_numbers.append(i)

even_numbers_set= set(even_numbers)
print(even_numbers_set)
print("-----------------------9b) or----------------------")
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number_set = set({})
for i in numbers:
   if i % 2 == 0:
    even_number_set.add(i)

print(even_number_set)
print("-----------------------9c)----------------------")
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number_dict = {}
for i in numbers:
   if i % 2 == 0:
    even_number_dict.update({i:i**2})

print(even_number_dict)

# 10. Conversion between List, Set, and Tuple
#     a) Convert the list of fruits to a set and print the result.
#     b) Convert the set of even numbers to a tuple and print the result.
#     c) Convert the tuple of coordinates to a list and print the result.

# Conversion between list, set, and tuple examples:
# fruits -> set
# even_numbers (from challenge) -> tuple
# coordinates (tuple) -> list
print("------------------------convert list to set---------------------------")
set_of_fruits = set(fruits)
print(set_of_fruits)
print("------------------------convert set to tuple---------------------------")
tuple_even_nambers= tuple(even_number_set)
print(tuple_even_nambers)
print("------------------------convert tuple to list---------------------------")
tuple_to_list = list(tuple_even_nambers)
print(tuple_to_list)

# 11. Dictionary Keys and Values
#     a) Print the list of dictionary keys from the `grades` dictionary.
#     b) Print the list of dictionary values from the `grades` dictionary.
#     c) Loop through the dictionary and print each student name (key) and their grade (value).

# Dictionary keys and values
# grades -> keys() -> list
# grades -> values() -> list
# loop through dictionary

#grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("----------------11.--------------------")
keys = grades.keys()
values = grades.values()
print(keys)
print(values)
print("----------------11c--------------------")
for keys, values in zip(keys, values):
    print(keys,":",values)

print("------------or----11c--------------------")

for k, v in grades.items():
    print(k,":",v)