# f1= open("one.text","w")
# f1.write("welcome to File Handling \n")
# f1.write("File with write operation \n")

# for i in range(1,6):
#      print(f1.readlines(i))

# f1.write("welcome \n")
# f1.close()

f1 = open("one.text", "r")
for i in range(1, 4):
    print(f1.readlines(i))
f1.close()
