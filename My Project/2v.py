names = ['sai','shiva','bochkar']
marks = [56,20,84]
updates = [32,74,-52]
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
# !Final Print 
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

# # !Top Ranker in one row
for i in range(len(b)):
    if c[1][0] == b[i][0] :
        print(f"Name: {c[0][0]}, New Marks {c[0][1]}, New Rank: 1, Old Marks {b[i][1]}, Old Rank: {i+1}  Rank Jump: {i+1}" ) 

                             




















# ! Full List Explore
print("Old Ranking")
for i in range(len(b)):
    print(f"{i+1}. Names: {b[i][0]}, Marks: {b[i][1]}")
print("New Ranking")
for i in range(len(c)):
    print(f"{i+1}. Names: {c[i][0]}, Marks: {c[i][1]}")

# # !Print Old Row
# print("Old Ranking\n")
# for i in range (len(names)):
#     print(f"{i+1}. Names: {names[i]}  Marks:  {marks[i]}")

# # !Print New Row
# print("New Ranking")
# for i in range(len(b)):
#     print(f"{i+1}. Names: {b[i][0]}, Marks: {b[i][1]}\n")


# !Final Print 
# for i in range(len(c)):
#     if i != 0:
#         print(f"Rank: {i+1} ")
#         print(f"Names: {c[i][0]}")
#         print(f"Marks: {c[i][1]}")
#     for j in range(len(b)):
#         if c[i][0] in b[j]:
#             if i != 0:
#                 print(f"Old rank: {j+1}")
#                 print(f"Old Marks: {b[j][1]}")
#             else:
#                 print(f"Name: {c[i][0]}, New Marks {c[i][1]}, New Rank: {i+1}, Old Marks {b[j][1]}, Old Rank: {j+1}")
#     print()
