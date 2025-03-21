import sys
import random
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

print("Welcome to dice rolling simulator")
print("Do you want to roll the dice?y/n")
x=input()
if(x=="y"):
    while(True):
        print(random.randint(1,6))
        print("Do you wnat to continue?y/n")
        c=input()
        if(c=="y"):
            continue
        else:
            print("Thank you for playing")
            break
else:
    print("Thank you")