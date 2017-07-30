import random
secret = random.randint(1, 20)
print("......Billy Studio........")
print("Random guess game......There is a random number between 1-20, Billy and Shirley select a number seperately,/n if the sum of your number equal to the random number, game over!")
billyguess = int(input("Billy's number pls:"))
shirleyguess = int(input("Shirley select a number pls:"))
while (billyguess + shirleyguess) != secret:
    print("You are wrong! Guess again!")
    billyguess = int(input("Billy select a number again pls:"))
    shirleyguess = int(input("Shirley select a number again pls:"))
    if (billyguess + shirleyguess) == secret:
        print("You are right!？")
    else:
        if (billyguess + shirleyguess) > secret:
            print("大了")
        else:
            print("小了")
print("game over!")
