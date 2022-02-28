                                    #Email Validation - Mini Project Using Python.

"""Using Python to check whether a given email is valid or not : Email-Validation Mini Project
   Conditions:
   1)Must contain an '@'.
   2)Must Contain length of minimum 6 letters.
   3)Use basic If-Else ladder to create. 
   4) Use String Functions to create.:)
"""

email=input("Enter your Email : ")   #eg: g@g.in, hisses@gmail.com
k,j,d=0,0,0
if len(email)>=6:#1st condition.
    if email[0].isalpha():#2nd condition.
        if ("@" in email) and (email.count("@")==1):#3rd condition.
            if(email[-4]==".") ^ (email[-3]=="."):#4th condition.
                for i in email:
                    if i==i.isspace():  #Checks for space between if any.->#5.1 (5th condition)
                        k=1#portrays space 
                    elif i.isalpha():    #Condition for checking alphabets.
                        if i==i.upper(): #Checks for upercase letters.->#5.2 (5th condition)
                            j=1#shows upercase
                    elif i.isdigit(): #Condition for checking digits.
                        continue
                    elif i=="_" or i=="." or i=="@": #Checking for the presence of underscore("_"),dot(".") or attherate("@").
                        continue
                    else: #->5.3 (5th condition).
                        d==1#If any other special character found.       
                if(k==1 or j==1 or d==1):
                    print("Wrong Email based on 5th condition")
                else:
                    print("Right Email")
            else:
                print("Wrong Email based on 4th condition")
        else:
            print("Wrong Email based on 3rd condition")
    else:
        print("Wrong Email based on 2nd condition")
else:
    print(" Wrong Email based on 1st condition ")
