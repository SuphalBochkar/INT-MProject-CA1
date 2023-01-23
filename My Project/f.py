print()
names = ['Tanishka','Ashish','Vipul','Arpit','Krishna','Vinay','Sidharth','Rishikesh','Anushka','Anmol']
marks = [91,82,46,67,52,36,47,54,75,34]
updates = [-26,-12,-20,-14,17,-24,-6,19,-4,8]
a={}
um=[]
ua={}
for i in range (len(names)):
    a[names[i]]=marks[i]
    um=um+[marks[i]+updates[i]]
    ua[names[i]]=um[i] 
   
b=sorted(a.items(), key=lambda z:(z[1],z[0]), reverse=True)
c=sorted(ua.items(), key=lambda z:(z[1],z[0]),reverse=1)
print(b)
print(c)

# # !Top Ranker in one row

for i in range(len(b)):
    if c[0][0] == b[i][0] :
        print(f"Name: {c[0][0]}, New Marks {c[0][1]}, New Rank: 1, Old Marks {b[i][1]}, Old Rank: {i+1}  Rank Jump: {i}" ) 
print()

# ! Print All Students 
for i in range(len(c)):
    print(f"Rank: {i+1} ")
    print(f"Name: {c[i][0]}")
    print(f"New Marks: {c[i][1]}")
    for j in range(len(b)):
        if c[i][0] == b[j][0]:
                print(f"Rank Jump: {(j-i)}")
                print(f"Old rank: {j+1}")
                print(f"Old Marks: {b[j][1]}")
    print()
