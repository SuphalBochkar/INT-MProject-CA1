name=input("Enter Student Names: ").split(",")
marks=map(int,input("Enter Marks: ").split(","))

print("\n")

d=dict(zip(name,marks))

def ranking(d):
    l=[]
    for j in range(1,len(d)+1):
        l.append(j)

    rank=list(sorted(d.items(),key=lambda x:x[1],reverse=True))

    for i in range(len(d)):
        print("Rank",l[i],":",rank[i][0])

ranking(d)

M=max(d.items(),key=lambda x:x[1])
print("\nMax Marks",*M,sep=" : ")

print("\n")

update=map(int,input("Enter Updated Marks: ").split(","))

print("\n")

d.update(dict(zip(name,update)))

ranking(d)

M=max(d.items(),key=lambda x:x[1])
print("\nMax Marks",*M,sep=" : ")