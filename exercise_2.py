
# Python Code Challenge: Functions and List Comprehensions

# Challenge 1: Define a function that takes a list of numbers and returns a new list containing only the even numbers.
# The function should use list comprehension.
print("-----------------------1 even-----------------------")
#def even_numbers(i):
    #even_number_list=[x for  x in i if x % 2 == 0]
   # return even_number_list
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list_of_numbers[2:12])

def even_numbers(num):
    result = []
    for x in num:
        print(x)
        if x % 2 == 0: # != not equal == equal 2 === 2
            result.append(x)
    print(result)

    for x in range(0, 12, 2): # <
        print(num[x])



#def odd_numbers(x):
    #odd_number_list = [i for i in range(0, len(x), 1) if i % 2 != 0]
    #print(odd_number_list) 
print("-----------------------while start-----------------------")
#i = 0

#while i < 10:
   # i=i+1
  #  print(i)
    
print("-----------------------while end-----------------------")
even_numbers(list_of_numbers)


#print(only_even)

print("-----------------------1 odd-----------------------")

#odd_numbers(list_of_numbers)
#even_number_list=[i for  i in list_of_numbers if i % 2 == 0]
#odd_number_list = [x for x in range(0, len(list_of_numbers), 1) if x % 2 != 0]
#print(even_number_list) # [2, 4, 6, 8, 10, 12]
#print(odd_number_list) # [1, 3, 5, 7, 9, 11]

# Challenge 2: Define a function that takes a list of strings and returns a new list with the strings that have more than 5 characters.
# Use list comprehension for filtering.
print("-----------------------2-----------------------")
'''
def select_names(name):
    name_has_6ormore_carcter = [fname for fname in name if len(fname) > 5]
    print(name_has_6ormore_carcter)
'''
def select_students(student):
    result_student = []
    for fname in student:
       # print(fname)
        if len(fname) > 5:
            result_student.append(fname)
    print(result_student)


students = ["Hans","Tom", "jerry", "seinfeld", "Gebrekidan", "Hagos", "Gebrehans", "Antonios", "Jen", "Christian"]
x = len(students[3])
print(x)

select_students(students)
#select_names(students)

# Challenge 3: Write a function that takes a list of integers and returns a list of their squares.
# Use list comprehension to achieve this.
print("-----------------------3-----------------------")

def square(x):
    y = [i**2 for i in x]
    return y

list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_of_intigers = square(list_of_integers)

print(square_of_intigers)

print("--------------or------------")

def square(x):
    squered = map(lambda y: y**2, x)
    return list(squered)
square_of_intigers = square(list_of_integers)

print(square_of_intigers)
# Challenge 4: Write a function that accepts two lists of the same length and returns a list of tuples,
# where each tuple contains elements from the two lists at the corresponding positions. Use list comprehension.
print("-----------------------4-----------------------")

def mix_list1_and_list2(list1, list2)->list[tuple]:
    result = list(zip(list1, list2))
    # for elem_1, elem_2 in zip(list1, list2):
    #     result.append((elem_1, elem_2))
   
    # for index in range(0, len(list1), 1):
    #     result.append((list1[index], list2[index]))

    return result
     
first_list_ch4 = [1, 2, 3, 4, 5, 6]
second_list_ch4 = [10, 20, 30, 40, 50, 60]
print(mix_list1_and_list2(first_list_ch4, second_list_ch4))
# Challenge 5: Create a function that takes a sentence (string) and returns a list of the lengths of each word in the sentence.
# Use list comprehension to split the sentence and calculate the lengths.
print("-----------------------5-----------------------")

def func_input_sentence(sentence):
    sentence_list = sentence.split()
    #print(sentence_list)
    list_of_words = []

    for words in sentence_list:
        list_of_words.append(len(words))
    return list_of_words


input_any_setentece = input("give any sentence: ")

print(func_input_sentence(input_any_setentece))

'''
myString = "Hello world"
myList = myString.split()

print(myList)
'''
# Challenge 6: Define a function that filters out words from a list that do not start with a vowel.
# Use list comprehension and a helper function that checks if a word starts with a vowel.
print("-----------------------6-----------------------")
def func_filter_vowls(filters):
    #filter_the_words = filters.split()
    result = []
    vowles = tuple("aeiouAEIOU")
    #print(vowles)
    for words in filters:
        #words.lower() == words.upper()
        if words.startswith(vowles) == True:
            result.append(words)
    return result

    '''
    filter_the_words = filters.split()
    result = []
    vowles = tuple("aeiouAEIOU")
    print(vowles)
    for words in filter_the_words:
        #words.lower() == words.upper()
        if words.startswith(vowles) == False:
            result.append(words)
    return result
    '''
  


filter_wowls = ["apple", "kiwi", "orange", "lemon", "banana", "Olive"]
#filter_the_vowels = input("give any words in a sentence: ")
#filter_for_test = ["kehase", "teklay", "Michael", "oliver", "anton", "urlich", "imely", "Emenm", "Hans"]
print(func_filter_vowls(filter_wowls))
# Challenge 7: Write a function that takes a list of numbers and returns a list of booleans indicating whether each number is greater than 10.
# Use list comprehension for this task.
print("-----------------------7-----------------------")
def filter_numbers(numbers):
    result_num = [num for num in numbers if num > 10]
    return result_num

list_numbers = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(filter_numbers(list_numbers))
# Challenge 8: Create a function that takes a list of dictionaries and returns a list of the values for a given key.
# Use list comprehension to extract the values.

print("-----------------------8-----------------------")
def extract(li_dict):
    your_key = input("give your key in sting: ")
    result = []
    
    for x in li_dict:
        for key, value in x.items():
            if key == your_key:
                result.append(f"{value}")
    return result
    
    '''
    for x in li_dict:
        result = [result.append(value) for key, value in x.items() if key == your_key]
                
    return result
    '''
list_of_dict = [

    {
       "name":  "John",
       "age" : 30,
       "city": "Berlin"
    },
    {
        "name": "Chris",
        "age" : 25,
        "city": "Paris"
    },
    {
        "name": "Seinfeld",
        "age" : 45,
        "city": "New York"
    }
]

print(extract(list_of_dict))
# Challenge 9: Write a function that accepts a list of words and returns a list of the words with their first letter capitalized.
# Use list comprehension to achieve this.

print("-----------------------9-----------------------")

def func_capitalize(filter_words):
    split_sentence = filter_words.split()
    #result_capi = [words.capitalize() for words in split_sentence]
    
    result_capi = []
    for word in split_sentence:
        first_letter_capi = word.capitalize()
        result_capi.append(first_letter_capi)
    return result_capi

    
give_you_words = input("inter you words hier in small letter: ")

print(func_capitalize(give_you_words))
# Challenge 10: Write a function that returns the common elements between two lists.
# Use list comprehension and the "in" operator to find common elements.
print("-----------------------10-----------------------")

def func_common_ele(element1, element2):
    result_ele = [element for element in element1 if element in element2]
    return result_ele

first_list_ch10 = ["apple", "banana", "kiwi", "orange"]
second_list_ch10 = ["banana", "kiwi", "strewbery", "mandarin"]

print(func_common_ele(first_list_ch10, second_list_ch10))
