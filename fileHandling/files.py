# r = Read
# w = Write
# a = Append
# r+ = Read and Write
# x = Create
import os
print(os.getcwd())

f  = open("./fileHandling/names.txt")
# print(f.read()) 
# print(f.read(4)) 
# print(f.read(8)) 

# for line  in f:
#     print(line)


try:
    f = open("./fileHandling/names.txt")
    print(f.read())
except:
    print("File not found")
finally:
    f.close

# Append - creates the file if it does not exist
f = open("./fileHandling/names.txt","a")
f.write("James\n")
f.close()

f = open("./fileHandling/names.txt")
print(f.read())

f.close()

# overWrite existing file
f = open("./fileHandling/context.txt","w")
f.write('The file has been updated')
f.close()

f = open("./fileHandling/context.txt")
print(f.read())

f.close()


# Two wayss to create a file

# opens a file for writing, creates the file if it does not exist
# and we have to pass 'w' as the second argument

f = open("./fileHandling/context2.txt","w")

if not os.path.exists("./fileHandling/context3.txt"):
    f = open("./fileHandling/dave.txt","w")
    f.close()

if os.path.exists("./fileHandling/dave.txt"):
    os.remove("./fileHandling/dave.txt")
else:
    print("The file you want to delete, does not exist")

with open("./fileHandling/names.txt") as f:
    content = f.read()

with open("./fileHandling/context.txt","w") as f:
    f.write(content)
    f.close()