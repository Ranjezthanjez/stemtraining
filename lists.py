#lists
words =["apple", "love," "peopple,"]
print(words[0])
print(words[1])
print(words)

#list can stoe any data type
dat =["a" ,1 ,1, "foo" ,6 , 7 ,"hey"]
print(dat[1])

#nested lists
m = [
   [5,6,7,],
   [8,9,1,]
 ]
print(m)

print(m)

#strings-can also be indexed as lists
str ="hello class"
print (str[5])
print (str [6])
print (str[7-3])

strg=["Hello","class","123","51","abc","hey","b","a"]
print(strg)
print(strg[5])
print(strg[6])
print(strg[7-3])
strg[0]=strg[7-2]
print(strg)

#lists indexes can be readdressed
subjects=["maths", "science","religious",]
subjects[2]="mechanics"
print (subjects)