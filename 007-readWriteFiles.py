# r read
# w write
# a append

F = open("007-test.txt", "w")
print(F)

F.write("I'm writing to a file\n")
F.write("This is a second line\n")
F.write("This is a third line\n")

F.close()

# \n

F = open("007-test.txt", "r")
#print(F.read())
#F.read(10)
#print(F.readline())
#print(F.readlines())
for line in F:
  print(line)
