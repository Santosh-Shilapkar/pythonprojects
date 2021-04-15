import os 
import time
def blocksite():
    hostpath='C:\Windows\System32\drivers\etc\hostscopy'
    redirect="127.0.0.1"
    websites=[]
    no=int(input("how many sites do you want to block:"))
    for i in range(no):
        x=input("Enter the site to be blocked:")
        websites.append(x)
    print("Sites to be blocked are:",websites)
    for i in range(len(websites)):
        data=open(hostpath,'r+')
        content=data.read()
        if websites[i] not in content:
            data.write(str(redirect)+" "+str(websites[i])+'\n')
    print("All sites are blocked")

#driver code
os.system('cls')
print("--------------------------------------------------------------")
time.sleep(1)
print("Want to stay away from the social media sites while working ????")
time.sleep(1)
print("Let's find the solution-----")
time.sleep(1)
blocksite()