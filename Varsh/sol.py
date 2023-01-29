        if c[i][0] in b[j]:
            if i != 0:
                print(f"Old rank: {j+1}")
                print(f"Old Marks: {b[j][1]}")
            else:
                print(f"Name: {c[i][0]}, New Marks {c[i][1]}, New Rank: {i+1}, Old Marks {b[j][1]}, Old Rank: {j+1}")
    print()
    
    
    
