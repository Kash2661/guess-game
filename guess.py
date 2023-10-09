import random
randnumber = random.randint(1,10)
print (randnumber)

usernumb= int(input("enter a number of your choices from 1 to 10 : "))

if usernumb==randnumber:
    print (f"you win , correct guess {randnumber}")
else:
    print (f"you lose , the correct number is {randnumber}")
