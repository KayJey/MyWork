print("Please think of a number between 0 and 100!")
low = 1
high = 99
mid = (low + high )// 2
c = input("Is your secret number" + str(mid) + "?" "\n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
while ( c != 'c' ):
    if c =='h' :
        high = mid-1
        mid = (low + high ) // 2
        c = input("Is your secret number" + str(mid) + "?" "\n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
    elif c == 'l' :
        low = mid +1
        mid = (low + high ) // 2
        c = input("Is your secret number" + str(mid) + "?" "\n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
    else :
        print("Sorry, I did not understand your input.")
        c = input("Is your secret number" + str(mid) + "?" "\n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
print("Game over. Your secret number was:" + str(mid))

