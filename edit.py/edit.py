#opening and editing files in python
role_file=open("roles.txt","r")
print(role_file.readline())

#close file
role_file.close()

file=open("roles.txt","w")
file.write("i love python")
file.close()

#append

file=open("roles.text","a")
file.write("i also love gaming")
file.close()

print("\n")