# Random Password Generator
    # The properties to be followed for a strong password are:
    # At least 12 characters.
    # A mixture of both uppercase and lowercase letters.
    # A mixture of letters and numbers. 
    # Inclusion of at least one special character, e.g., @ #?]
    # Note: do not use < or > in your password, as both can cause problems in Web browsers.
import random
from sys import exit
# range(start,end,incriment)
a=range (0,10)
b =random.randint(1,60)
while 1:
    print(b)