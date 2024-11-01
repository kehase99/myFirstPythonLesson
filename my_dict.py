mydic = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "2017"
}

print(mydic)
print(mydic["model"])

mydict = dict(name = "John", age = 30, city = "Berlin")

print(mydict)

x = mydict["name"]

print(x)

x = mydict.get("age")

print(x)

y = mydict.items()
print(y)
z = mydict.values()
print(z)

mydict.update({"color": ["red", "blue", "yellow"]})

print(mydict)

mydict.update({"name": "Chris"})

print(mydict)

#mydict.pop("age")
#mydict.popitem()
for x,y in mydict.items():
    print(x + ":", y)

for x in mydic.values():
    print(x)

for x in mydic.keys():
    print(x)
#print(mydict)