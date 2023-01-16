names = ['sai','shiva','bochkar']
marks = [56,20,84]
updates = [32,74,-52]
a={}                        # Making The dictionary
ua={}                       # Arranging the names in order
um=[]                       # Updating the marks    
for i in range (len(names)):
    a[names[i]]=marks[i]                  # Making the Dictionary of Names and Marks 
    um=um+[marks[i]+updates[i]]           # Updating the marks    
    ua[names[i]]=um[i]                    # Making the Dictionary of Names and Updated-Marks 
    
b=sorted(a.items(), key=lambda z:(z[1],z[0]),reverse=1)             # Arranging the Dictionary of Names and Marks
c=sorted(ua.items(), key=lambda z:(z[1],z[0]),reverse=1)            # Arranging the Dictionary of Names and Updated-Marks

# # !All in one
# for i in range(len(b)):
#     if b[i][0] == c[0][0]:                          # Printing the highest ranker
#         print(f"Name: {c[0][0]}, New Marks: {c[0][1]}, New Rank: 1, Old Marks {b[i][1]}, Old Rank: {i+1}")

# # !Induvidual Old and New , Marks and Rank
# for i in range(len(b)):
#     if b[i][0] == c[0][0]:
#         print(f"{c[0][0]} New: {c[0][1]} Old: {b[i][1]}")
#         print(f"{c[0][0]} New: 1 Old: {i+1}")

# # !Print Old Row
# print("Old Ranking\n")
# for i in range (len(names)):
#     print(f"{i+1}. Names: {names[i]}  Marks:  {marks[i]}\n")

# # !Print New Row
# print("New Ranking")
# for i in range(len(b)):
#     print(f"{i+1}. Names: {b[i][0]}, Marks: {b[i][1]}\n")
# print()
