import time

print("Countdown Timer In Seconds:\n")
xtime = int(input("Enter time in seconds: "))

for xtime in range(xtime, 0, -1):
    seconds = xtime % 60
    minutes = int(xtime / 60) % 60
    hours = int(xtime / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    xtime = time.sleep(1)

# another function completed on 10/14/24:
#import time

#sec = int(input("Enter the number of seconds: "))

#while sec > 0:
    #seconds = sec % 60
    #minutes = int((sec / 60) % 60)
    #hours = int(((sec / 3600) % 60) % 24)
    #days = int((((sec / 86400) % 60) % 24) % 365)
    #print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    #sec -= 1
    #x = time.sleep(1)

# another function revised on 10/18/24:
#import time

#sec = int(input("Enter the number of seconds: "))

#while sec > 0:
    #seconds = sec % 60
    #minutes = int(sec / 60) % 60
    #hours = int(sec / 3600) % 24
    #days = int(sec / 86400)
    #print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    #sec -= 1
    #x = time.sleep(1)