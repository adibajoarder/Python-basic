txt = "The best things in life are free!"
print("free" in txt)



b = "Hello, World!"
print(b[-5:-2])



a = "Hello, world!"
print(a.replace("H", "j"))



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


x = ("apple","apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
y.remove("apple")
thistuple = tuple(y)
print(x)


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car.update({"year": 2020})
x = car.values()
print(x) 
car["color"] = "red"
print(x)


import math
x = math.sqrt(64)
print(x)


price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)


print("Enter your name:")
name = input()
print(f"Hello {name}")

   

