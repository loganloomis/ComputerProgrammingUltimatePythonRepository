import random
def number_guesser():
    number = random.randint(0,10)
    response =  int(input("enter a number 1-10: "))
    while response != number:
        print("Wrong,try again")
        response =  int(input("enter a number 1-10: "))
    else:
        print("Correct")

print("######################")

def number_guesser_with_lives():
    lives = 3
    number = random.randint(1,10)
    response = int(input("enter a number 1-10: "))
    
    if lives == 0:
        print("Game over")


    while response != number and lives > 0:
        print("Wrong, Try again")
        response = int(input("enter a number 1-10: "))
        lives = lives - 1
        print("you have",lives,"live(s) left")
        if lives < 1:
            print("game over")
        elif lives == 0:
             print("game over")
    else:
            print("Correct")

#print(number_guesser_with_lives())
    

def vending_machine():
    print("Enter 50 cents")
    amountLeft = 50
    coin = int(input("Enter change: "))
    while coin > 0:
        if amountLeft < 1:
            print("Your change back is",abs(amountLeft))        
            if coin == 25 or coin == 10 or coin == 5:
                amountLeft = amountLeft - coin
                print("amount left",amountLeft,"cents")
                coin = int(input("Enter change: "))
    
         

print(vending_machine())
         













    

