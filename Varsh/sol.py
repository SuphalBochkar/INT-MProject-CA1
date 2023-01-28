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




for i in range(len(b)):
    if b[i][0] == c[0][0]:
        print(f"Name: {c[0][0]}, New Marks {c[0][1]}, New Rank: 1, Old Marks {b[i][1]}, Old Rank: {i+1}")


for i in range(len(c)):
    if i != 0:
        print(f"Rank: {i+1} ")
        print(f"Names: {c[i][0]}")
        print(f"Marks: {c[i][1]}")
    for j in range(len(b)):
        if c[i][0] in b[j]:
            if i != 0:
                print(f"Old rank: {j+1}")
                print(f"Old Marks: {b[j][1]}")
            else:
                print(f"Name: {c[i][0]}, New Marks {c[i][1]}, New Rank: {i+1}, Old Marks {b[j][1]}, Old Rank: {j+1}")
    print()
    
    
    
# for i in range(len(b)):
#     if b[i][0] == c[0][0]:
#         print(f"{c[0][0]} New: {c[0][1]} Old: {b[i][1]}")
#         print(f"{c[0][0]} New: 1 Old: {i+1}")