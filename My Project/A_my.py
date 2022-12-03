names=['Tanishka','Ashish  ','Vipul   ','Arpit   ','Krishna ']
marks=[28,43,31,39,45]
# name_list=names.split(",")
# marks=marks.split(",")
d=dict(zip(names,marks))
print(d)
marks2=input("enter the updated marks: ")
mark2_list=marks2.split(",")
new_marks=[]
for i in range(0,len(marks)):
    new_marks=int(marks[i])+int(mark2_list[i])
max=max(new_marks)
d2=dict(zip(str(new_marks),names))
for x,y in d2.items():
    if x==max(d2):
        print("maximum marks is got by:",y)