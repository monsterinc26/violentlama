# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:20:11 2019

@author: Ravi
"""

try:
    
    k=["sunnyyes@gmail.com","snickette@hotmail.com"]
    
    import smtplib
    
    import time
    
    from smtplib import SMTP
    
    while 1:
        
        
        for i in k:
            
            time.sleep(3)
            
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            
            s.login("rvsingh567@gmail.com","ravisingh1234")
            
            
            msg="Subject: Grab dinner this weekend?\n\nHow about dinner this weekend at 5PM?"
            
            s.sendmail("rvsingh567@gmail.com",i,msg)
            
            print(i)
            
            s.quit()
        
        z=input("Do you want to continue sending mails? ")
        
        if z=="no":
          break


except Exception as e:
    print("Password is wrong, please enter again",e)
finally:
    print("Mails sent successfully")
    
    
import smtplib
from smtplib import SMTP
s=smtplib.SMTP(smtp.gmail.com,587)
s.starttls()
s.login("rvsingh567@gmail.com","ravisingh1234")
message="Subject: Trip", "body=Wanna go on a trip?"
s.sendmail("rvsingh567@gmail,com","snickette@gmail.com",msg=message)
s.quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    