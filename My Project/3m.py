Names =    ['Tanishka','Ashish  ','Vipul   ','Arpit   ','Krishna ']
Marks =    [28,43,31,39,45]
Updates =  [-5,+2,-9,-7,+9]
print("Rank     Name        Marks")
updated_m = []
d=dict(zip(Marks,Names))
for i in range(len(Names)):
    print(f"{i+1}        {Names[i]}    {Marks[i]}")
    updated_m += [Marks[i] + Updates[i]]
    

# print(sorted(d))
# print(Marks)
# print(updated_m)
# print(sorted(updated_m))
print(dict(d).update(updated_m))