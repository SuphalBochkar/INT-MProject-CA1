names =    ['Tanishka','Ashish','Vipul','Arpit','Krishna','Vinay','Sidharth','Rishikesh','Anushka','Anmol']
marks =    [28,43,31,39,28,21,38,25,15,19]
updates =  [-5,-22,-9,-7,+9,-1,-7,-3,-6,+3]
a = {}
ua = {}
um = []
for i in range(len(names)):
    a[names[i]] = marks[i]
    um += [marks[i]+updates[i]]
    ua[names[i]] = um[i]
b = sorted(a.items(), key=lambda k:(k[1], k[0]), reverse=True)
c = sorted(ua.items(), key=lambda k:(k[1], k[0]), reverse=True)

# ! List Explore
# print("Old Ranking")
# for i in range(len(b)):
#     print(f"{i+1}. Names: {b[i][0]}, Marks: {b[i][1]}")
# print("New Ranking")
# for i in range(len(c)):
#     print(f"{i+1}. Names: {c[i][0]}, Marks: {c[i][1]}")


