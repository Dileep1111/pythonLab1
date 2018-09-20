python_lst = ['Alex','Amir','Ajith','Mbappe','Antone']
web_lst = ['Alex','Mbappe','Munir','Hexam','lexica']
new_lst = []
for item in python_lst:
    if item not in web_lst:
        new_lst.append(item)

print(f'the student list who are attending only python class : {new_lst} \n')
print(f'the student list who attending  python class : {python_lst} \n')
print(f'the student list who are attending web class : {web_lst} \n ')