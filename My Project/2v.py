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
