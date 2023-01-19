name=['Tanishka','Ashish','Vipul','Arpit','Krishna']
marks=[28,43,31,39,45]

d=dict(zip(name,marks))

def ranking(d):
    l=[]
    
    for j in range(1,len(d)+1):
        l.append(j)
        
    rank=list(sorted(d.items(),key=lambda x:x[1],reverse=True))
    print(rank)
    
    for i in range(len(d)):
        print("Rank",l[i],":",rank[i][0],"l",rank[i])
            
        
        
ranking(d)






















M=max(d.items(),key=lambda x:x[1])
print("\nMax Marks",*M,sep=" : ")

print("\n")

update=[-5,+2,-9,-7,+9]

print("\n")
