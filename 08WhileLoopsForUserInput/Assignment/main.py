import random

#number = random.randint(0,10)
#response =  int(input("enter a number 1-10: "))
#while response != number:
    #print("Wrong,try again")
    #response =  int(input("enter a number 1-10: "))
#else:
    #print("Correct")

print("######################")
lives = 3
print("lives",lives)
number2 = random.randint(0,10)
response2 =  int(input("enter a number 1-10: "))

while response2 != number2:
    
    

    
    if lives < 1:
            
        print("Wrong,try again")
        lives = lives - 1
        print("lives",lives)
        response2 =  float(input("enter a number 1-10: "))
    
else:
    print("Correct")
    print("Game over")

