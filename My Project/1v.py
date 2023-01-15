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

