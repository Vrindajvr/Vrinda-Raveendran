import time
import math
office=None
health=None
sleep=None
travel=None
print("enter your name")
name=input()
print("\n")
print("enter your schedule")
print("\n")
print("How many hours you stayed in office")
try:
    office1=int(input("enter day 1\n"))
    office2=int(input("enter day 2\n"))
    office3=int(input("enter day 3\n"))
    office=int((office1+office2+office3)/3)
    

    
except ValueError:
    print("Error! This is not a number. Try again.")
    exit(0)
    
print("\n")    
print("How many hours you spent at home excluding sleeping hours")
try:
    
    home1=int(input("enter day 1\n"))
    home2=int(input("enter day 2\n"))
    home3=int(input("enter day 3\n"))
    home=int((home1+home2+home3)/3)
except ValueError:
    print("Error! This is not a number. Try again.")
    exit(0)

print("\n")    
print("how many hours did you play or did excercise")
try:
    #health=int(input())
    health1=int(input("enter day 1\n"))
    health2=int(input("enter day 2\n"))
    health3=int(input("enter day 3\n"))
    health=int((health1+health2+health3)/3)
except ValueError:
    print("Error! This is not a number. Try again.")
    exit(0)

print("\n")    
print("how many hours did you sleep")
try:
    #sleep=int(input())
    sleep1=int(input("enter day 1\n"))
    sleep2=int(input("enter day 2\n"))
    sleep3=int(input("enter day 3\n"))
    sleep=int((sleep1+sleep2+sleep3)/3)
except ValueError:
    print("Error! This is not a number. Try again.")
    exit(0)
#time.sleep(100)

print("\n")    
print("how many hours did you travel")
try:
    #travel=int(input())
    travel1=int(input("enter day 1\n"))
    travel2=int(input("enter day 2\n"))
    travel3=int(input("enter day 3\n"))
    travel=int((travel1+travel2+travel3)/3)
except ValueError:
    print("Error! This is not a number. Try again.")
    exit(0)

names = [name,'home', 'health','sleep','travel']
weights = [office]
costs = [home]
heights=[health]
snooze=[sleep]
traffic=[travel]

print("\n")
if(office+home+health+sleep+travel>24):
    print("check the input you entered and try again")
    exit(0)
else:
    print("\n")
    print("this was your shedule")
print("\n")
titles = ['user','office', 'home', 'health','sleep','travel']
data = [titles] + list(zip(names, weights, costs, heights,snooze,traffic))

for i, d in enumerate(data):
    line = '|'.join(str(x).ljust(12) for x in d)
    print(line)
    if i == 0:
        print('-' * len(line))

print("\n")
print("here are some tips for you")        

print("\n")
if(office>10):
    print("Try to reduce working hours, try to have a work life balance")

print("\n")
if(health<2):
    print("Try out doing excersise or yoga to relax yourself")

print("\n")
if(sleep<8):
    print("Try to relax yourself by having a good sleep, a good sleep can give you a good start")

print("\n")
if(sleep>9):
    print("Try to be more active, a long time in bed make your day a dull day")

print("\n")
if(travel>4):
    print("Start early and save your precious time")

print("\n")
if(office<10 and health>=2 and sleep==9 and travel<=4):
    print("you have a perfect schedule in your life")

else:
    print("Try out the given tips to improve your daily schedule")

"""elif(office<>12 and health<>2 and sleep<>10 and travel<>5):
    print("Try to follow the tips given to have a better schedule in life")"""
"""example(sleep)
def example(slef,int):
    
            if(sleep>9):
                print("dear ",name," you slept quiet a lot")
            elif (sleep==9):
                print("dear ",name," you slept for a perfect time")
            else:
                print("dear ",name," you need to sleep more")
            

example()  """
