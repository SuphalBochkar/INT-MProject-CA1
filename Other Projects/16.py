# Number To Roman
    # Design an application where user will input two dates.
    # His/her date of birth in DD/MM/YY format.
    # Current (Present day) date in DD/MM/YY format.
    # Your app will calculate and let the user know how many days that person survived in this world.
    # Note: Your calculation must be accurate and you have to consider leap and non-leap years separately.
    # Project 17: (Converter to convert given Roman to integer)
    # Editorial/Explanation about Roman numbers: Roman numerals are represented by seven different symbols:I,V,X,L,C,D,M.
    # Symbol Value: I 1 V 5 X 10 L 50 C 100 D 500 M 1000
    # For example, 2 is written as II in Roman numeral, just two ones added together.12 written as XII,which is simply X+II.
    # The number 27 is written as XXVII, which is XX + V + II.
    # Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
    # Instead, the number four is written as IV. Because the one is before the five, we subtract it making four.
    # The same principle applies to the number nine,which is written as IX.There are six instances where subtraction is used:
    # I can be placed before V (5) and X (10) to make 4 and 9.
    # X can be placed before L (50) and C (100) to make 40 and 90.
    # C can be placed before D (500) and M (1000) to make 400 and 900.
    # Your task is create a converter which converts given roman numeral to an integer.
    
x=int(input())
r=x%5
r=0
if x <= 5:
    if x==1:
        print('I')
    if x==2:
        print('II')
    if x==3:
        print('III')
    if x==4:
        print('VI')
    if x==5:
        print('V')

        
