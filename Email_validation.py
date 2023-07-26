from time import *

print(time())
email = input("Enter Your Email: ")
k,j,d = 0,0,0
if len(email)>=6: # 01 Wrong
    if email[0].isalpha():# 02 worng
        if ("@" in email) and (email.count("@")==1): # 03 wrong
            if (email[-4]==".")^(email[-3]=="."):# 04 wrong
                for i in email :
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1: # 05 wrong
                    print("wrong Email 5")
            else:
                print("wrong Email 4")
        else:
            print("wrong Email 3")
    else:
        print( " wrong Email 2")
else:
    print(" wrong Email 1")
    