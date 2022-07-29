# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Sample Input
# 07:05:45PM
    
# Sample Output
# 19:05:45


def timeConversion(time):
    
    a=time[8:10]

    if time[0:2]=="12"and a=="PM":
        new=time
    elif time[0:2]=="12" and a=="AM":
        new=time.replace("12","00")
  
    elif(a=="AM"):
        new=time
    else:
        b=int(time[0:2])+12
        new=time.replace(time[0:2],str(b),1)

    if a=="AM":
        x=new.replace("AM","")
    else:
        x=new.replace("PM","")

    return x
