name=['sai','shiva','bochkar']
marks=[10,20,30]
updates=[1,2,3]

# Combine And make dictionary of Names and Marks
n_m=dict(zip(name,marks))

# Make list of 1..2..3.. to print Ranks
l=[]
for j in range(1,len(n_m)+1):
    l.append(j)