
#dictionaries in python
mydict={
"book":"dynamics",
"publisher":"longhorn",
"year":2001
}
#accessing item
x=mydict["year"]
print (x)

#accessing using get()
y=mydict.get
print(y)

#all keys
x=mydict.keys()
print(x)

#all values
x=mydict.values

#printing all items in a dictionary
x=mydict.items()
print(x)

#checking if key exist
if "publisher" in mydict:
    print("publisher is one of the keys")
print (len(mydict))

#dictionaries can hold different data types
mydict={
    "book":"dynamics",
    "publisher":"longhorn",
    "year":2001,
    "authours":["john","mike","ike"]
}