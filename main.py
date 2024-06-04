email=input("Enter your email: ")
k=0
j=0
d=0
if len(email)>6:
        if email[0].isalpha():
           if ('@' in email) and (email.count("@")==1):
                if (email[-4]==".")^ (email[-3]=="."):
                    for a in email:
                        if a==a.isspace():
                            k==1
                        elif a==a.isalpha():
                            if a==a.upper():
                                j==1
                            elif a.isdigit():
                                continue
                            elif a=="_"or a=="." or a=="@":
                                continue

                            else:
                                d==1

                    if k==1 or j==1 or d==1:
                            print("email wrong: 5")
                    else:
                            print("Right email")











                else:
                    print("wrong email: 4")

           else:
               print("wrong email: 3")


        else:
            print("wrong email:2")


else:
    print("wrong email:1")





# email validation using regex



# import re
# email_condition="^[a-z]+[\._]?[a-z,0-9]+[@]\w+[.]\w[a-z]{2,3}$"
# userinput =input("enter your email")
# if re.search(email_condition,userinput):
#     print("your email is right")
# else:
#     print("your email is wrong")