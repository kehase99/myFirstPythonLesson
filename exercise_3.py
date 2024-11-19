import numpy
from scipy import stats
import statistics
# Exercise 3: Advanced Python Challenges  

# 1. Define a function `calculate_statistics` that takes a list of numbers and returns a dictionary containing:
#    a) The mean of the numbers.
#    b) The median of the numbers.
#    c) The mode of the numbers.
#    Use the `statistics` module for these calculations.

# a)
def calculate_statistics(num):
    mean_num = statistics.mean(num)
    #return mean_num
    median_num = statistics.median(num)
    #return median_num
    mode_num = statistics.mode(num)
    #return mode_num

    statistic_dict = {
        "mean": mean_num,
        "median": median_num,
        "mode": mode_num
    }
    return statistic_dict

list_of_numbers = [10, 20, 30, 30, 35, 40, 50, 60]

print(calculate_statistics(list_of_numbers))

# 2. Create a class `Rectangle` that has attributes for `width` and `height`.
#    a) Define a method to calculate the area of the rectangle.
#    b) Define a method to calculate the perimeter of the rectangle.
#    c) Instantiate two rectangles and compare their areas.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def areaRectangle(self):
        area_rect = self.width * self.height
        return area_rect

    def perimeterRectangle(self):
        perimeter_rect = 2*self.width + 2*self.height
        return perimeter_rect

R1 = Rectangle(25, 10)
R2 = Rectangle(15, 5)
a_R1 = R1.areaRectangle()

print(f"area R1: {a_R1}")

p_R1 = R1.perimeterRectangle()

print(f"Perimeter R1: {p_R1}")

a_R2 = R2.areaRectangle()

print(f"area R2: {a_R2}")

p_R2 = R2.perimeterRectangle()  

print(f"Perimeter R2: {p_R2}")

if a_R1 > a_R2:
    print(f"Area of R1 is greater than R2 {a_R1} > {a_R2}")
else:
    print(f"Area of R2 is greater than R1 {a_R2} > {a_R1}")

# 3. Define a function `is_prime` that takes an integer and returns `True` if the number is prime, and `False` otherwise.
# a) Use this function to filter a list of numbers (from 1 to 100) and return only the prime numbers.
def is_prime(n):
    if n <= 1:
        return False

    # range(start, stop, next) 
    #  start 2 , 3
    # stop = int(n **0.5)+1
    for i in range(2, int(n **0.5)+1):
        if n % i == 0:
            return False # break; breaks the loop
    return True
"""
6

"""

    # count = 0
    # result = []
    # for x in prime_num:
    #     for i in range(1, x + 1, 1):
    #         if x % i == 0:
    #             count = count + 1
    #         if count == 2:
    #             result.append(x)
    # return result


        #if x % 2 :
           # return
    


list_of_1_to_100 = []
for i in range(1, 101):
    list_of_1_to_100.append(i)

#print(list_of_1_to_100)
print(is_prime(9))
# 4. Define a function `merge_dictionaries` that accepts two dictionaries and merges them.
#   a) If both dictionaries have the same key, sum the values of that key.
#   b) Otherwise, combine the keys and values into the resulting dictionary.

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()

    for key in dict2:
        if key in merged:
            merged.update({key:merged[key] + dict2[key]})

        elif key not in merged:
            merged.update({key: dict2[key]})
    return merged


first_dict_ch4 = {
            "first": 10,
            "second": 20,
            "third": 30,
            "year": 2024
}
second_dict_ch4 = {
        "first": 10,
        "second": 20,
        "city": "Berlin",
        "counry": "Germany"
}

print(merge_dictionaries(first_dict_ch4, second_dict_ch4))

# 5. Create a generator function `fibonacci` that yields an infinite sequence of Fibonacci numbers.
#   a) Use a `for` loop to print the first 20 Fibonacci numbers.

def fibonacci(n):
    
    if n in {0, 1}:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    

print([fibonacci(n) for n in range(20)])
#num = [number for number in range(20)]
#print(fibonacci(num))
# 6. Define a function `matrix_transpose` that takes a 2D list (matrix) and returns its transpose.
#    a) The function should work for any matrix size.

def matrix_transpose(tr_m):
    mtr_result = []
    tr_matrix = zip(*tr_m)
    for row in tr_matrix:
        mtr_result.append(row)
    return mtr_result
    




matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix_transpose(matrix))



# 7. Write a function `analyze_text` that takes a string and returns:
#    a) The number of words in the string.
#    b) The number of unique words.
#    c) A dictionary of word frequencies.
#    d) The longest word in the string.
from collections import Counter
def analyze_text(text_ana):
    list_of_word = text_ana.split()
    num_words = len(list_of_word)

    num_unique_words = len(set(list_of_word))
    count_words = Counter(list_of_word)


    return F"number Of words: {num_words}\n number Of unique words: {num_unique_words}\ {count_words}"
    
    #print(text_ana.split())
    


my_string = "I am a student of a Full stack developer"
#analyze_text(my_string)
print(analyze_text(my_string))
# 8. Define a function `group_by_length` that takes a list of strings and returns a dictionary where:
#    a) The keys are string lengths.
#    b) The values are lists of strings with that length.

# 9. Define a recursive function `factorial` that calculates the factorial of a given number.
#    a) Use it to calculate the factorial of numbers from 1 to 10.

# 10. Define a function `flatten_list` that takes a nested list and returns a flat list.
#     a) Use recursion to handle arbitrarily nested lists.
#     Example: flatten_list([1, [2, [3, 4], 5]]) -> [1, 2, 3, 4, 5]

# 11. Write a function `reverse_string_recursive` that reverses a given string using recursion.
#     Example: reverse_string_recursive("hello") -> "olleh"

# 12. Define a higher-order function `apply_twice` that takes another function `f` as input and applies it twice to a given argument.
#     Example: apply_twice(lambda x: x * 2, 5) -> 20

# 13. Define a function `read_file_lines` that reads the contents of a file line by line and returns a list of the lines.
#     a) Handle file not found errors gracefully by printing a message.

# 14. Define a function `write_even_numbers` that writes only the even numbers from a list into a text file.
#     a) Ensure that the file is created and written to safely.

def write_even_numbers(num: list[int]):
    result_num = []
    for number in num:
        if number % 2 == 0:
            result_num.append(number)
    return result_num
    


#with open('even-number.txt', 'w') as file: file.write(str(number))
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(write_even_numbers(list_num))

def write_even_numbers(some_filename: str, some_numbers: list) -> None:
    with open(some_filename, "w") as file:
        file.writelines(f"{number}" for number in some_numbers if number % 2 == 0)
    
    


filename = "list_of_numbers.txt"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
write_even_numbers(some_filename = filename, some_numbers = numbers)

# 15. Define a function `memoized_fibonacci` that returns the nth Fibonacci number, using memoization to optimize the computation.
#     a) Ensure the function computes the nth Fibonacci efficiently by storing already computed values.

# 16. Create a decorator `time_execution` that measures and prints the execution time of any function it decorates.
#     a) Use it on the `fibonacci` function to measure how long it takes to compute the 30th Fibonacci number.

# 17. Define a function `unique_permutations` that takes a list and returns all unique permutations of the elements in the list.
#     a) Use the `itertools` module to simplify the task.

# 18. Define a function `safe_division` that performs division but catches division by zero errors.
#     a) If an error occurs, return "Undefined" instead of raising an exception.

# 19. Create a class `BankAccount` with attributes for `balance` and methods `deposit` and `withdraw`.
#     a) Ensure `withdraw` raises an error if there are insufficient funds.
#     b) Create a method `transfer` to transfer money between two bank accounts.

# 20. **New Challenge: Complex Data Manipulation**
#     Define a function `merge_sort` that implements the merge sort algorithm recursively.
#     a) The function should take a list of numbers and return a sorted list.
#     b) Ensure the function is efficient and works on lists of large size.
#     c) Use this function to sort a list of 1000 random numbers.

# 21. Define a function `json_to_yaml` that converts a JSON object to a YAML file.
#     a) The JSON object should contain key-value pairs.
#     b) Use the `yaml` module to write the data to a YAML file.

# 22. Define a function `yaml_to_json` that converts a YAML file to a JSON object.
#     a) Ensure the function reads the YAML file and outputs the equivalent JSON structure.

# 23. Define a function `yaml_to_csv` that converts a YAML file to a CSV file.
#     a) The YAML file should contain structured data (e.g., dictionaries or lists).
#     b) Use the `csv` module to write the data to a CSV file.

# 24. Define a function `csv_to_yaml` that converts a CSV file to a YAML file.
#     a) The CSV file should contain rows of data.
#     b) Ensure the function reads the CSV and outputs the equivalent YAML structure.
