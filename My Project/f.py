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

