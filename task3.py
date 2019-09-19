courses = {'python': 1500, 'java': 1000, 'c': 800, 'c++': 1200}

sorted_dictionary = sorted((value,key) for (key,value) in courses.items())
c={}
for i in sorted_dictinoary:
    c[i[1]]=i[0]

print(c)
