import random


def run_game():
#get random numbers
    digits = []
    # random_digit = random.randint(1,8)
    while len(digits) != 4:
        x = digits.append(random.randint(1,8))
        if x in digits:
            continue
        # digits == [x]
    # print(digits)

    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
#get user input and make sure that there are no 9's and 0's and the number of digits should be 4
    lives = 12
    while lives > 0: 
        while True:
            guess = input("Input 4 digit code: ")
            if guess.isdigit() == False:
                print("Please enter exactly 4 digits.")
                continue
            else:
                pass
            if len(guess) != 4 or '9' in str(guess) or '0' in str(guess):
                print("Please enter exactly 4 digits.")
                continue
            break
            
            
        #guesses = str(list(guess))
        
        count1 = 0 #to check if the number is in the awnser
        count2 = 0 #to check if the number is in the right place

#check the number of digit in the correct place or not        
        for i,j in enumerate(digits):
            if int(guess[i]) == j:
                count1 += 1
            elif str(j) in guess:
                count2 += 1
        print("Number of correct digits in correct place:    ",count1)
        print("Number of correct digits not in correct place:",count2)

        answer = ""
        for A1 in digits:
            answer = answer + str(A1)
        if guess == answer:
            print("Congratulations! You are a codebreaker!")
            print("The code was: " + answer)
            break
    
        lives -= 1
        print("Turns left:", lives)

    # if lives == 0:
    #     print("Game Over")

        
if __name__ == "__main__":
    run_game()
