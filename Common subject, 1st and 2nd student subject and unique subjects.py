s1 = {'Math' , 'Physics' , 'Chemistry'}
s2 = {'Physics', 'Biology', 'Math'}

common = s1 & s2
print("common subjects: ", common)

only_s1 = s1 - s2
print("Only first student : ", only_s1)

only_s2 = s2 - s1
print("Only second student: ", only_s2)

unique = s1 | s2 
print("Total unique subjects:" , unique)