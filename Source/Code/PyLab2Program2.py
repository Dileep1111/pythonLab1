# reading the text from file 1
file1 = open("pylab2txt1","r")
my_string1 = file1.read()
# reading the text from file 2
file2 = open("pylab2txt2","r")
my_string2 = file2.read()


string1_lst = my_string1.split()
string2_lst = my_string2.split()
string3_lst =[ ]
# removes the text of file2 in file1
for item1 in string1_lst:
    if item1.lower() not in string2_lst:
        # string3_lst + item1
        string3_lst.append(item1)


print(my_string1 + "/n")
print(string1_lst)
print(my_string2 + "/n")
print(string2_lst)
print("\n")
print("New modified string is :")
print(" ".join(string3_lst))

