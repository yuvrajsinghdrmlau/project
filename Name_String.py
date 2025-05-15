name = input("Please, Enter Your Name: \n")
print("upper case: ",name.upper())
print("lower case: ",name.lower())
print("length : ",len(name))
if "a" in name.lower():
    print("replaced A : ", name.replace("a","@"))
print("replaced _: ", name.replace(" ", "_"))

print("first 3 : ", name[0:3])

