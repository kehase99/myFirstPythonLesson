 my_list = [1, 2, 3, 4, 5]
            
print("Original list:", my_list)
"""
   i = 4 => since len(my_list) = 5 but real array length is 5-1 = 4 because of 0 indexing
first iteration:
  range(len(my_list)-1, -1, -1) 
    i = 4
    my_list[4] = 5
second iteration
  range(len(my_list)-1, -1, -1) 
  i = 4-1 = 3  my_list[3] = 4

third iteration
  range(len(my_list)-1, -1, -1) 
  i = 3-1 = 2 my_list[3] = 3
  
fourth iteration
  range(len(my_list)-1, -1, -1) 
  i = 2-1 = 1 my_list[1] = 2
  
five iteration
  range(len(my_list)-1, -1, -1) 
  i = 1-1 = 0 my_list[0] = 1
  break
"""
# array_length = len(my_list)-1
# for i in range(array_length, -1, -1):
#     print(my_list[i])
    
# for element in my_list:
#     print(f" element: {element}")
    
# for index,  _ in enumerate(my_list):
#     print(f" element: {my_list[index]}")


# Creating a set
# my_set = {1, 2, 3, 4, 5}
# print("Original set:", my_set)
 
# # for element in reversed(list(my_set)):
# #     print(element)
# for i in range(len(my_set)-1, -1, -1):
#     print(list(my_set)[i])

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# keys = list(my_dict.keys())
# for key in keys:
#     print(my_dict[key])

# values = list(my_dict.values())
# for value in values:
#     print(value)
"""  
for k, v in zip(keys, value)
keys = ["name", "age", "city"]
value = [ "John", 30, "New York"]
1s iteration 
 key, value = ("name", "John")
     name: john
     
2nd iteration
  key, value = ("age", 30)
     
2nd iteration
  key, value = ("city", "New York")
# """
values = list(my_dict.values()) # = [ "John", 30, "New York"]
keys = list(my_dict.keys()) # = ["name", "age", "city"]
# for key, value in zip(keys, values):  
#     print(f"{key}: {value}")
  
zipped = zip(values, keys) # [("John", "name"), (30,"age"), ("New York", "city")]

for element in zipped:
    value, key = element # ("John", "name")
    print(f"{key}: {value}")
    
# key, value =   ("name", "John")
# print(key)
# print(value)
# keys = []
# value = []
# my_dict = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
[17.10.2024 21:22] Adam Fuzum Tewelde: i = 0

while i < 10:
    i+=2
    print(f"element {i}")
    # i=i+1
    
while i < 10: 
    if i%2 == 0 and i != 0 and i !=10:
        print(f"element {i}")
    i=i+1


i = 10 

while i > -1:
    print(f"element {i}")
    i-=1

for i in range(10):
    print(f"element {i}")

for i in range(2, 10, 2):
    print(f"element {i}")

for i in range(10):
    if i%2 == 0 and i != 0:
        print(f"element {i}")

for i in range(10, -1, -1):
    print(f"element {i}")
 
my_list = [1, 2, 3, 4, 5]
 
length_of_my_list = len(my_list)-1

print(f"length of array {length_of_my_list}")

for i in range(length_of_my_list):
    print(f"elements {my_list[i]}")
    
for element in my_list:
    print(element)
    

my_tuple = tuple(my_list)

print(my_tuple)


for element in my_tuple:
    print(element)
    

my_set = set(my_list)

print(my_set)

for element in my_set:
    print(element)


my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

keys = list(my_dict.keys())
values = list(my_dict.values())


print(f"keys: {keys}")
print(f"values: {values}")

for key in keys:
    print(f"key: {key}")
    
for value in values:
    print(f"value: {value}")
    
keys_n_values = zip(keys, values)

for key,value in keys_n_values:
    print(f"{key}: {value}")

for key,value in zip(keys, values):
    print(f"{key}: {value}")
    
for key,value in my_dict.items(): # zip(keys, values)
    print(f"{key}: {value}")