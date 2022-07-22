import pyautogui
import time

script=open(r'C:\Users\Kulka\OneDrive\Documents\GitHub\python\my_spam_bot\scriptt.txt')

read_it=script.read()

write=read_it.split()

print('YOU HAVE 5 SECONDS TO CLICK ON THE TYPE MESSEAGE IN WHATSAPP!!')

count=5

while(count!=0):
    print(count)
    time.sleep(1)
    count=count-1


for i in range(0,len(write)):
    pyautogui.typewrite(write[i]+'\n')
    time.sleep(0.3)
