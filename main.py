import random
c,r=0,0
for i in range(10):
    a=random.randint(1,100)
    b=random.randint(1,100)
    try:
        answer = int(input("{} * {} = ?\nWhat is the answer? ".format(a,b)))
        if answer == a*b:
            c+=1
            print("Correct!")
        else:
            r+=1
            print("Incorrect!")
    except KeyboardInterrupt:
        print("\nExiting the quiz.")
        break
    except:
        r+=1
        print("Incorrect!")
print("You got {} questions correct.\nYou got {} questions incorrect.".format(c,r))