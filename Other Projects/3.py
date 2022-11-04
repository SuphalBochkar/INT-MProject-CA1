# Email Slicer
    # Email Slicer is just a simple tool that will take multiple email address as an input and slice it to produce the username 
    # and the domain associated with it. The email must be divided into two strings by using ‘@’ as the separator.
    # So, user provides n number of email addresses and you have to design a logic to slice the username 
    # and the domain out of those email addresses. The domain part must print in capitals.
    # Note: Email addresses must be stored first in some container and then operate the required logic on it.
    # EX: abc@gmail.com    xyz@yahoo.com
    # after slicing
    # username :abc and domain: GMAIL.COM    username: xyz and domain: YAHOO.COM

email=str(input("Enter th E-Mail:"))
# list('hello')
# ['h', 'e', 'l', 'l', 'o']
# list=list(email)
# print(list)
# print(str(list))
# for i in list:
#     if i == '@':
#         break
#     print('a')
# x = email.index('@')
# slice=list(email)
# user=print(email[4,x])
for i in email:
    print(i)
