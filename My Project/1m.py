import pprint

# Marks.sort()
# Names1 =    {'Tanishka':28,'Ashish':43,'Vipul':31,'Arpit':39,'Krishna':45,
#             'Vinay':21,'Sidharth':38,'Rishikesh':25,'Anushka':15,'Anmol':19}
#      a     =    {['Tanishka','Ashish','Vipul','Arpit','Krishna','Vinay','Sidharth','Rishikesh','Anushka','Anmol']}
Names =    ['Tanishka','Ashish','Vipul','Arpit','Krishna','Vinay','Sidharth','Rishikesh','Anushka','Anmol']
Marks =    [28,43,31,39,45,21,38,25,15,19]
Updates =  [-5,+2,-9,-7,+9,-1,-7,-3,-6,+3]
updated_m = []
d=dict(zip(Names,Marks))
print(d)
for i in range(len(Names)):
    print(f"{i+1}. Name: {Names[i]} Marks: {Marks[i]}")
    updated_m += [Marks[i] + Updates[i]]
print(updated_m)


    
for i in range(len(Marks)):
    print(f"Name: {Names[i]} Marks: {Marks[i]} Updates: {updated_m[i]}")
    
    
    
# for i in range(10):
#     print(f"{Names1[i]},{Marks[i]} {Updates[i]}")
# for i,j in zip(Names,Marks):
#     print(f'{i} got {j} marks')
# for i in Names.values():
