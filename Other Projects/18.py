# Clock Angle Problem
    # Given time in hh:mm format in 24-hour notation, calculate the shorter angle between the hour 
    # and minute hand in an analog clock.
    # Input: 5:30
    # Output: 15°
    # Input: 21:00
    # Output: 90°
    # Input: 12:00
    # Output: 0°

a=input("enter time")
b=a.split(" ",)
print(b)

h=int(input())
m=int(input())
if 0<= h <=12 and 0<= m <= 60:
    h=h%12
    if m ==60:
        h+=1
        m==0
    h=h+m/60
    u=abs(h-m/(60/12))
    a
    
    
    
else :
    print("Enter Valid Time"())