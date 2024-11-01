mytuple = ("apple", "banana", "orange", "kiwi")
#mytuple[2]="mandarin"
print(mytuple[2])

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
if "apple" in thistuple:
    print("yes apple is in the list")

x = ("apple", "banana", "orange", "kiwi")
y = list(x)
y[1]= "lemon"
x=tuple(y)
print(x)

z = ("mandarin",)
x += z
print(x)

x = ("apple", "banana", "orange", "kiwi", 1, 2, 3, 4, 5, 6, 7, 8)

first, second, third, *others = x

print(first)
print(second)
print(third)
print(others)

first, *second, third, others = x

print(first)
print(second)
print(third)
print(others)

i = 0

while i < len(thistuple):
    print(thistuple[i])
    i += 1 

for i in thistuple:
    print(i)

