a = [1,2,3,4,5]
print(a)
a.append(6)
a.append(7)
a.append("mohan")
print(a)
a.pop(7)
print(a)
a.pop(6)
print(a)
a.pop()
print(a)
b = [11,12,13,14,15]
a.extend(b)
print(a)


a=(1,2,3,4)
b = list(a)
b.pop()
print(b)


a = {1,2,3,4,5,2,4}
print(a)
a.add(100)
print(a)
a.remove(100)
print(a)
a.pop()
print(a)


a = {
    "name" : "mohan",
    "age" : 20,
    "location" : "hosur" ,
    "domain" : {"al and ml" , "full-stack deeloper"}
}
print(a)
#print(a.keys())
#print(a.values())
a["color"] = "blue"
print(a)

a.update({"age": 21})
print(a)

del a["domain"]
print(a)

a.pop("age")
print(a)

a.clear()
print(a)