print()
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

# # !Top Ranker in one row
