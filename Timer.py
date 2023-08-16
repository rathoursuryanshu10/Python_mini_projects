import time
set_timer=int(input("Enter the time(in sec) for timer :: "))
for x in range(set_timer,0,-1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time is UP!")
