myset = {"apple", "banana", "kiwi", "orange", "banana"}
print(myset)

thisset = {"apple", "banana", "kiwi", "orange", True, False, 1, 0}
print(thisset)

for i in thisset:
    print(i)

print("banana" not in thisset)
mynewset = {"apple", "banana", "kiwi", "orange", "banana"}
tropical = {"pineapple", "mango", "papaya"}
tropical2 = [1, 2, 3, 4, 5]
mynewset.add("lemon")
mynewset.update(tropical, tropical2)
print(mynewset)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#set1.intersection_update(set2)
#print(set1)
#set4 = set1 & set2
#print(set4)

set5 = set1.difference(set2)
print(set5)

set6 = set1.symmetric_difference(set2)
print(set6)