"""
x = "Mhretab"
y = "Sbhatu"
z= 1.002
#Sum = x + y

print(x, y)
"""
my_first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_second_list = ["apple", "banana", "orange", "kiwi", "cherry"]
#print(my_first_list)
print("----------------------------------------------------")
#my_first_list.append(2)
#my_first_list.append(True)
#my_first_list.insert(2, 20)
#print(my_first_list)
"""
print("----------------------------------------------------")
my_first_list.extend(my_second_list)
print(my_first_list)
print("----------------------------------------------------")
my_second_list.extend(my_first_list)
print(my_second_list)

"""
#my_first_list = (*my_first_list, *my_second_list)
#print(type(my_first_list))
#x = 10
#y = 9
#z = x+y 
#my_first_list = my_first_list + my_second_list
#print(my_fourt_list)
#my_first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#my_second_list = ["apple", "banana", "orange", "kiwi", "cherry"]
#my_first_list.remove(10)
#my_first_list.pop()
#my_first_list.pop(4)
#print(my_first_list)

i = 0
while i <= 10:
    print(i)
    i = i+1
print("---------------------------------------------")
i = 10
while i >= 0:
    print(i)
    i = i-1
print("---------------------------------------------")


mylist = ["apple", "banana", "orange", "kiwi", "cherry"]
#print(mylist[2])
print(len(mylist))
i = 0
while i <= 4:
    print(mylist[i])
    i = i + 1
print("---------------------------------------------")
i = 0
while i <= len(mylist)-1:
    print(mylist[i])
    i = i+1
print("--------------------for loop-------------------------")
for i in range(10):
    print(i)
print("--------------------2 for loop-------------------------")
for i in range(0, 10, 2):
    print(i)

print("--------------------3 for loop for lists-------------------------")
for i in range(0, len(mylist), 1):
    print(mylist[i])


"""
mylists = [1, 2, 3, 2, 4, 4, 5, 6]

print(mylists)
print(len(mylists))
print(type(mylists))

secondList = list(("banana", "apple", "orange", "kiwi", "lemon"))
secondList.insert(2, "strewbary")
secondList.append("mandarin")

my_third_list = [1, 2, 3, 4, 5]

#secondList = (*secondList, *my_third_list)
secondList.extend(my_third_list)
#secondList.remove("banana")
#secondList.pop(3)
#del secondList[0]
"""
"""
secondList[1] = "blackcurrant"
secondList[2:4] = ["watermelon", "honymelon"]
"""
"""
print(secondList[:])

"""
"""
if "lemon" in secondList:
    print("Yes, apple is in the fruits list")
else:
    print("no, there is no")
"""
"""
print("--------------------------------------------------")
#for i in my_third_list:
 #   print(f"element: {i}")
for i in range(0, len(my_third_list), 1):
    print(f"element: {my_third_list[i]}")

print("--------------------------------------------------")
for i in range(len(my_third_list)-1, -1, -1):
    print(f"element: {my_third_list[i]}")

print("--------------------------------------------------")
for i in range(0, len(my_third_list), 1):
    if my_third_list[i] % 2 == 0:
        print(f"element: {my_third_list[i]}")
print("--------------------------------------------------")

for i in range(0, len(my_third_list), 1):
    if i % 2 == 0:
        print(f"element: {my_third_list[i]}")
print("--------------------------------------------------")
i=0

while i <= len(my_third_list)-1:
    print(my_third_list[i])
    i+=1
print("--------------------------------------------------")

i = len(my_third_list) -1
while i >= 0:
    print(my_third_list[i])
    i-=1

"""